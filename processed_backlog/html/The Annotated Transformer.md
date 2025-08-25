# The Annotated Transformer

**Source:** inputs/New Docs/reader/nlp.seas.harvard.edu_annotated-transformer.html
**Processed:** 2025-08-24T19:14:21.361436

The Annotated Transformer  
  
v2022: Austin Huang, Suraj Subramanian, Jonathan Sum, Khalid Almubarak, and Stella Biderman.  
  
Original: Sasha Rush.  
  
The Transformer has been on a lot of people’s minds over the last year five years. This post presents an annotated version of the paper in the form of a line-by-line implementation. It reorders and deletes some sections from the original paper and adds comments throughout. This document itself is a working notebook, and should be a completely usable implementation. Code is available here.  
  
Table of Contents  
  
Prelims  
  
Skip  
  
# !pip install -r requirements.txt  
  
# # Uncomment for colab # # # !pip install -q torchdata==0.3.0 torchtext==0.12 spacy==3.2 altair GPUtil # !python -m spacy download de\_core\_news\_sm # !python -m spacy download en\_core\_web\_sm  
  
import os from os.path import exists import torch import torch.nn as nn from torch.nn.functional import log\_softmax, pad import math import copy import time from torch.optim.lr\_scheduler import LambdaLR import pandas as pd import altair as alt from torchtext.data.functional import to\_map\_style\_dataset from torch.utils.data import DataLoader from torchtext.vocab import build\_vocab\_from\_iterator import torchtext.datasets as datasets import spacy import GPUtil import warnings from torch.utils.data.distributed import DistributedSampler import torch.distributed as dist import torch.multiprocessing as mp from torch.nn.parallel import DistributedDataParallel as DDP # Set to False to skip notebook execution (e.g. for debugging) warnings.filterwarnings("ignore") RUN\_EXAMPLES = True  
  
# Some convenience helper functions used throughout the notebook def is\_interactive\_notebook(): return \_\_name\_\_ == "\_\_main\_\_" def show\_example(fn, args=[]): if \_\_name\_\_ == "\_\_main\_\_" and RUN\_EXAMPLES: return fn(\*args) def execute\_example(fn, args=[]): if \_\_name\_\_ == "\_\_main\_\_" and RUN\_EXAMPLES: fn(\*args) class DummyOptimizer(torch.optim.Optimizer): def \_\_init\_\_(self): self.param\_groups = [{"lr": 0}] None def step(self): None def zero\_grad(self, set\_to\_none=False): None class DummyScheduler: def step(self): None  
  
My comments are blockquoted. The main text is all from the paper itself.  
  
Background  
  
The goal of reducing sequential computation also forms the foundation of the Extended Neural GPU, ByteNet and ConvS2S, all of which use convolutional neural networks as basic building block, computing hidden representations in parallel for all input and output positions. In these models, the number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions, linearly for ConvS2S and logarithmically for ByteNet. This makes it more difficult to learn dependencies between distant positions. In the Transformer this is reduced to a constant number of operations, albeit at the cost of reduced effective resolution due to averaging attention-weighted positions, an effect we counteract with Multi-Head Attention.  
  
Self-attention, sometimes called intra-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Self-attention has been used successfully in a variety of tasks including reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations. End-to-end memory networks are based on a recurrent attention mechanism instead of sequencealigned recurrence and have been shown to perform well on simple-language question answering and language modeling tasks.  
  
To the best of our knowledge, however, the Transformer is the first transduction model relying entirely on self-attention to compute representations of its input and output without using sequence aligned RNNs or convolution.  
  
Part 1: Model Architecture  
  
Model Architecture  
  
Most competitive neural sequence transduction models have an encoder-decoder structure (cite). Here, the encoder maps an input sequence of symbol representations (x\_1, ..., x\_n) to a sequence of continuous representations \mathbf{z} = (z\_1, ..., z\_n). Given \mathbf{z}, the decoder then generates an output sequence (y\_1,...,y\_m) of symbols one element at a time. At each step the model is auto-regressive (cite), consuming the previously generated symbols as additional input when generating the next.  
  
class EncoderDecoder(nn.Module): """ A standard Encoder-Decoder architecture. Base for this and many other models. """ def \_\_init\_\_(self, encoder, decoder, src\_embed, tgt\_embed, generator): super(EncoderDecoder, self).\_\_init\_\_() self.encoder = encoder self.decoder = decoder self.src\_embed = src\_embed self.tgt\_embed = tgt\_embed self.generator = generator def forward(self, src, tgt, src\_mask, tgt\_mask): "Take in and process masked src and target sequences." return self.decode(self.encode(src, src\_mask), src\_mask, tgt, tgt\_mask) def encode(self, src, src\_mask): return self.encoder(self.src\_embed(src), src\_mask) def decode(self, memory, src\_mask, tgt, tgt\_mask): return self.decoder(self.tgt\_embed(tgt), memory, src\_mask, tgt\_mask)  
  
class Generator(nn.Module): "Define standard linear + softmax generation step." def \_\_init\_\_(self, d\_model, vocab): super(Generator, self).\_\_init\_\_() self.proj = nn.Linear(d\_model, vocab) def forward(self, x): return log\_softmax(self.proj(x), dim=-1)  
  
The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder, shown in the left and right halves of Figure 1, respectively.  
  
Encoder and Decoder Stacks  
  
Encoder  
  
The encoder is composed of a stack of N=6 identical layers.  
  
def clones(module, N): "Produce N identical layers." return nn.ModuleList([copy.deepcopy(module) for \_ in range(N)])  
  
class Encoder(nn.Module): "Core encoder is a stack of N layers" def \_\_init\_\_(self, layer, N): super(Encoder, self).\_\_init\_\_() self.layers = clones(layer, N) self.norm = LayerNorm(layer.size) def forward(self, x, mask): "Pass the input (and mask) through each layer in turn." for layer in self.layers: x = layer(x, mask) return self.norm(x)  
  
We employ a residual connection (cite) around each of the two sub-layers, followed by layer normalization (cite).  
  
class LayerNorm(nn.Module): "Construct a layernorm module (See citation for details)." def \_\_init\_\_(self, features, eps=1e-6): super(LayerNorm, self).\_\_init\_\_() self.a\_2 = nn.Parameter(torch.ones(features)) self.b\_2 = nn.Parameter(torch.zeros(features)) self.eps = eps def forward(self, x): mean = x.mean(-1, keepdim=True) std = x.std(-1, keepdim=True) return self.a\_2 \* (x - mean) / (std + self.eps) + self.b\_2  
  
That is, the output of each sub-layer is \mathrm{LayerNorm}(x + \mathrm{Sublayer}(x)), where \mathrm{Sublayer}(x) is the function implemented by the sub-layer itself. We apply dropout (cite) to the output of each sub-layer, before it is added to the sub-layer input and normalized.  
  
To facilitate these residual connections, all sub-layers in the model, as well as the embedding layers, produce outputs of dimension d\_{\text{model}}=512.  
  
class SublayerConnection(nn.Module): """ A residual connection followed by a layer norm. Note for code simplicity the norm is first as opposed to last. """ def \_\_init\_\_(self, size, dropout): super(SublayerConnection, self).\_\_init\_\_() self.norm = LayerNorm(size) self.dropout = nn.Dropout(dropout) def forward(self, x, sublayer): "Apply residual connection to any sublayer with the same size." return x + self.dropout(sublayer(self.norm(x)))  
  
Each layer has two sub-layers. The first is a multi-head self-attention mechanism, and the second is a simple, position-wise fully connected feed-forward network.  
  
class EncoderLayer(nn.Module): "Encoder is made up of self-attn and feed forward (defined below)" def \_\_init\_\_(self, size, self\_attn, feed\_forward, dropout): super(EncoderLayer, self).\_\_init\_\_() self.self\_attn = self\_attn self.feed\_forward = feed\_forward self.sublayer = clones(SublayerConnection(size, dropout), 2) self.size = size def forward(self, x, mask): "Follow Figure 1 (left) for connections." x = self.sublayer[0](x, lambda x: self.self\_attn(x, x, x, mask)) return self.sublayer[1](x, self.feed\_forward)  
  
Decoder  
  
The decoder is also composed of a stack of N=6 identical layers.  
  
class Decoder(nn.Module): "Generic N layer decoder with masking." def \_\_init\_\_(self, layer, N): super(Decoder, self).\_\_init\_\_() self.layers = clones(layer, N) self.norm = LayerNorm(layer.size) def forward(self, x, memory, src\_mask, tgt\_mask): for layer in self.layers: x = layer(x, memory, src\_mask, tgt\_mask) return self.norm(x)  
  
In addition to the two sub-layers in each encoder layer, the decoder inserts a third sub-layer, which performs multi-head attention over the output of the encoder stack. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization.  
  
class DecoderLayer(nn.Module): "Decoder is made of self-attn, src-attn, and feed forward (defined below)" def \_\_init\_\_(self, size, self\_attn, src\_attn, feed\_forward, dropout): super(DecoderLayer, self).\_\_init\_\_() self.size = size self.self\_attn = self\_attn self.src\_attn = src\_attn self.feed\_forward = feed\_forward self.sublayer = clones(SublayerConnection(size, dropout), 3) def forward(self, x, memory, src\_mask, tgt\_mask): "Follow Figure 1 (right) for connections." m = memory x = self.sublayer[0](x, lambda x: self.self\_attn(x, x, x, tgt\_mask)) x = self.sublayer[1](x, lambda x: self.src\_attn(x, m, m, src\_mask)) return self.sublayer[2](x, self.feed\_forward)  
  
We also modify the self-attention sub-layer in the decoder stack to prevent positions from attending to subsequent positions. This masking, combined with fact that the output embeddings are offset by one position, ensures that the predictions for position i can depend only on the known outputs at positions less than i.  
  
def subsequent\_mask(size): "Mask out subsequent positions." attn\_shape = (1, size, size) subsequent\_mask = torch.triu(torch.ones(attn\_shape), diagonal=1).type( torch.uint8 ) return subsequent\_mask == 0  
  
Below the attention mask shows the position each tgt word (row) is allowed to look at (column). Words are blocked for attending to future words during training.  
  
def example\_mask(): LS\_data = pd.concat( [ pd.DataFrame( { "Subsequent Mask": subsequent\_mask(20)[0][x, y].flatten(), "Window": y, "Masking": x, } ) for y in range(20) for x in range(20) ] ) return ( alt.Chart(LS\_data) .mark\_rect() .properties(height=250, width=250) .encode( alt.X("Window:O"), alt.Y("Masking:O"), alt.Color("Subsequent Mask:Q", scale=alt.Scale(scheme="viridis")), ) .interactive() ) show\_example(example\_mask)  
  
Attention  
  
An attention function can be described as mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key.  
  
We call our particular attention “Scaled Dot-Product Attention”. The input consists of queries and keys of dimension d\_k, and values of dimension d\_v. We compute the dot products of the query with all keys, divide each by \sqrt{d\_k}, and apply a softmax function to obtain the weights on the values.  
  
In practice, we compute the attention function on a set of queries simultaneously, packed together into a matrix Q. The keys and values are also packed together into matrices K and V. We compute the matrix of outputs as:  
  
\mathrm{Attention}(Q, K, V) = \mathrm{softmax}(\frac{QK^T}{\sqrt{d\_k}})V  
  
def attention(query, key, value, mask=None, dropout=None): "Compute 'Scaled Dot Product Attention'" d\_k = query.size(-1) scores = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(d\_k) if mask is not None: scores = scores.masked\_fill(mask == 0, -1e9) p\_attn = scores.softmax(dim=-1) if dropout is not None: p\_attn = dropout(p\_attn) return torch.matmul(p\_attn, value), p\_attn  
  
The two most commonly used attention functions are additive attention (cite), and dot-product (multiplicative) attention. Dot-product attention is identical to our algorithm, except for the scaling factor of \frac{1}{\sqrt{d\_k}}. Additive attention computes the compatibility function using a feed-forward network with a single hidden layer. While the two are similar in theoretical complexity, dot-product attention is much faster and more space-efficient in practice, since it can be implemented using highly optimized matrix multiplication code.  
  
While for small values of d\_k the two mechanisms perform similarly, additive attention outperforms dot product attention without scaling for larger values of d\_k (cite). We suspect that for large values of d\_k, the dot products grow large in magnitude, pushing the softmax function into regions where it has extremely small gradients (To illustrate why the dot products get large, assume that the components of q and k are independent random variables with mean 0 and variance 1. Then their dot product, q \cdot k = \sum\_{i=1}^{d\_k} q\_ik\_i, has mean 0 and variance d\_k.). To counteract this effect, we scale the dot products by \frac{1}{\sqrt{d\_k}}.  
  
Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions. With a single attention head, averaging inhibits this.  
  
\mathrm{MultiHead}(Q, K, V) = \mathrm{Concat}(\mathrm{head\_1}, ..., \mathrm{head\_h})W^O \\ \text{where}~\mathrm{head\_i} = \mathrm{Attention}(QW^Q\_i, KW^K\_i, VW^V\_i)  
  
Where the projections are parameter matrices W^Q\_i \in \mathbb{R}^{d\_{\text{model}} \times d\_k}, W^K\_i \in \mathbb{R}^{d\_{\text{model}} \times d\_k}, W^V\_i \in \mathbb{R}^{d\_{\text{model}} \times d\_v} and W^O \in \mathbb{R}^{hd\_v \times d\_{\text{model}}}.  
  
In this work we employ h=8 parallel attention layers, or heads. For each of these we use d\_k=d\_v=d\_{\text{model}}/h=64. Due to the reduced dimension of each head, the total computational cost is similar to that of single-head attention with full dimensionality.  
  
class MultiHeadedAttention(nn.Module): def \_\_init\_\_(self, h, d\_model, dropout=0.1): "Take in model size and number of heads." super(MultiHeadedAttention, self).\_\_init\_\_() assert d\_model % h == 0 # We assume d\_v always equals d\_k self.d\_k = d\_model // h self.h = h self.linears = clones(nn.Linear(d\_model, d\_model), 4) self.attn = None self.dropout = nn.Dropout(p=dropout) def forward(self, query, key, value, mask=None): "Implements Figure 2" if mask is not None: # Same mask applied to all h heads. mask = mask.unsqueeze(1) nbatches = query.size(0) # 1) Do all the linear projections in batch from d\_model => h x d\_k query, key, value = [ lin(x).view(nbatches, -1, self.h, self.d\_k).transpose(1, 2) for lin, x in zip(self.linears, (query, key, value)) ] # 2) Apply attention on all the projected vectors in batch. x, self.attn = attention( query, key, value, mask=mask, dropout=self.dropout ) # 3) "Concat" using a view and apply a final linear. x = ( x.transpose(1, 2) .contiguous() .view(nbatches, -1, self.h \* self.d\_k) ) del query del key del value return self.linears[-1](x)  
  
Applications of Attention in our Model  
  
The Transformer uses multi-head attention in three different ways: 1) In “encoder-decoder attention” layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder. This allows every position in the decoder to attend over all positions in the input sequence. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models such as (cite).  
  
The encoder contains self-attention layers. In a self-attention layer all of the keys, values and queries come from the same place, in this case, the output of the previous layer in the encoder. Each position in the encoder can attend to all positions in the previous layer of the encoder. Similarly, self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position. We need to prevent leftward information flow in the decoder to preserve the auto-regressive property. We implement this inside of scaled dot-product attention by masking out (setting to -\infty) all values in the input of the softmax which correspond to illegal connections.  
  
Position-wise Feed-Forward Networks  
  
In addition to attention sub-layers, each of the layers in our encoder and decoder contains a fully connected feed-forward network, which is applied to each position separately and identically. This consists of two linear transformations with a ReLU activation in between.  
  
\mathrm{FFN}(x)=\max(0, xW\_1 + b\_1) W\_2 + b\_2  
  
While the linear transformations are the same across different positions, they use different parameters from layer to layer. Another way of describing this is as two convolutions with kernel size 1. The dimensionality of input and output is d\_{\text{model}}=512, and the inner-layer has dimensionality d\_{ff}=2048.  
  
class PositionwiseFeedForward(nn.Module): "Implements FFN equation." def \_\_init\_\_(self, d\_model, d\_ff, dropout=0.1): super(PositionwiseFeedForward, self).\_\_init\_\_() self.w\_1 = nn.Linear(d\_model, d\_ff) self.w\_2 = nn.Linear(d\_ff, d\_model) self.dropout = nn.Dropout(dropout) def forward(self, x): return self.w\_2(self.dropout(self.w\_1(x).relu()))  
  
Embeddings and Softmax  
  
Similarly to other sequence transduction models, we use learned embeddings to convert the input tokens and output tokens to vectors of dimension d\_{\text{model}}. We also use the usual learned linear transformation and softmax function to convert the decoder output to predicted next-token probabilities. In our model, we share the same weight matrix between the two embedding layers and the pre-softmax linear transformation, similar to (cite). In the embedding layers, we multiply those weights by \sqrt{d\_{\text{model}}}.  
  
class Embeddings(nn.Module): def \_\_init\_\_(self, d\_model, vocab): super(Embeddings, self).\_\_init\_\_() self.lut = nn.Embedding(vocab, d\_model) self.d\_model = d\_model def forward(self, x): return self.lut(x) \* math.sqrt(self.d\_model)  
  
Positional Encoding  
  
Since our model contains no recurrence and no convolution, in order for the model to make use of the order of the sequence, we must inject some information about the relative or absolute position of the tokens in the sequence. To this end, we add “positional encodings” to the input embeddings at the bottoms of the encoder and decoder stacks. The positional encodings have the same dimension d\_{\text{model}} as the embeddings, so that the two can be summed. There are many choices of positional encodings, learned and fixed (cite).  
  
In this work, we use sine and cosine functions of different frequencies:  
  
PE\_{(pos,2i)} = \sin(pos / 10000^{2i/d\_{\text{model}}})  
  
PE\_{(pos,2i+1)} = \cos(pos / 10000^{2i/d\_{\text{model}}})  
  
where pos is the position and i is the dimension. That is, each dimension of the positional encoding corresponds to a sinusoid. The wavelengths form a geometric progression from 2\pi to 10000 \cdot 2\pi. We chose this function because we hypothesized it would allow the model to easily learn to attend by relative positions, since for any fixed offset k, PE\_{pos+k} can be represented as a linear function of PE\_{pos}.  
  
In addition, we apply dropout to the sums of the embeddings and the positional encodings in both the encoder and decoder stacks. For the base model, we use a rate of P\_{drop}=0.1.  
  
class PositionalEncoding(nn.Module): "Implement the PE function." def \_\_init\_\_(self, d\_model, dropout, max\_len=5000): super(PositionalEncoding, self).\_\_init\_\_() self.dropout = nn.Dropout(p=dropout) # Compute the positional encodings once in log space. pe = torch.zeros(max\_len, d\_model) position = torch.arange(0, max\_len).unsqueeze(1) div\_term = torch.exp( torch.arange(0, d\_model, 2) \* -(math.log(10000.0) / d\_model) ) pe[:, 0::2] = torch.sin(position \* div\_term) pe[:, 1::2] = torch.cos(position \* div\_term) pe = pe.unsqueeze(0) self.register\_buffer("pe", pe) def forward(self, x): x = x + self.pe[:, : x.size(1)].requires\_grad\_(False) return self.dropout(x)  
  
Below the positional encoding will add in a sine wave based on position. The frequency and offset of the wave is different for each dimension.  
  
def example\_positional(): pe = PositionalEncoding(20, 0) y = pe.forward(torch.zeros(1, 100, 20)) data = pd.concat( [ pd.DataFrame( { "embedding": y[0, :, dim], "dimension": dim, "position": list(range(100)), } ) for dim in [4, 5, 6, 7] ] ) return ( alt.Chart(data) .mark\_line() .properties(width=800) .encode(x="position", y="embedding", color="dimension:N") .interactive() ) show\_example(example\_positional)  
  
We also experimented with using learned positional embeddings (cite) instead, and found that the two versions produced nearly identical results. We chose the sinusoidal version because it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training.  
  
Full Model  
  
Here we define a function from hyperparameters to a full model.  
  
def make\_model( src\_vocab, tgt\_vocab, N=6, d\_model=512, d\_ff=2048, h=8, dropout=0.1 ): "Helper: Construct a model from hyperparameters." c = copy.deepcopy attn = MultiHeadedAttention(h, d\_model) ff = PositionwiseFeedForward(d\_model, d\_ff, dropout) position = PositionalEncoding(d\_model, dropout) model = EncoderDecoder( Encoder(EncoderLayer(d\_model, c(attn), c(ff), dropout), N), Decoder(DecoderLayer(d\_model, c(attn), c(attn), c(ff), dropout), N), nn.Sequential(Embeddings(d\_model, src\_vocab), c(position)), nn.Sequential(Embeddings(d\_model, tgt\_vocab), c(position)), Generator(d\_model, tgt\_vocab), ) # This was important from their code. # Initialize parameters with Glorot / fan\_avg. for p in model.parameters(): if p.dim() > 1: nn.init.xavier\_uniform\_(p) return model  
  
Inference:  
  
Here we make a forward step to generate a prediction of the model. We try to use our transformer to memorize the input. As you will see the output is randomly generated due to the fact that the model is not trained yet. In the next tutorial we will build the training function and try to train our model to memorize the numbers from 1 to 10.  
  
def inference\_test(): test\_model = make\_model(11, 11, 2) test\_model.eval() src = torch.LongTensor([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]) src\_mask = torch.ones(1, 1, 10) memory = test\_model.encode(src, src\_mask) ys = torch.zeros(1, 1).type\_as(src) for i in range(9): out = test\_model.decode( memory, src\_mask, ys, subsequent\_mask(ys.size(1)).type\_as(src.data) ) prob = test\_model.generator(out[:, -1]) \_, next\_word = torch.max(prob, dim=1) next\_word = next\_word.data[0] ys = torch.cat( [ys, torch.empty(1, 1).type\_as(src.data).fill\_(next\_word)], dim=1 ) print("Example Untrained Model Prediction:", ys) def run\_tests(): for \_ in range(10): inference\_test() show\_example(run\_tests)  
  
Example Untrained Model Prediction: tensor([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) Example Untrained Model Prediction: tensor([[0, 3, 4, 4, 4, 4, 4, 4, 4, 4]]) Example Untrained Model Prediction: tensor([[ 0, 10, 10, 10, 3, 2, 5, 7, 9, 6]]) Example Untrained Model Prediction: tensor([[ 0, 4, 3, 6, 10, 10, 2, 6, 2, 2]]) Example Untrained Model Prediction: tensor([[ 0, 9, 0, 1, 5, 10, 1, 5, 10, 6]]) Example Untrained Model Prediction: tensor([[ 0, 1, 5, 1, 10, 1, 10, 10, 10, 10]]) Example Untrained Model Prediction: tensor([[ 0, 1, 10, 9, 9, 9, 9, 9, 1, 5]]) Example Untrained Model Prediction: tensor([[ 0, 3, 1, 5, 10, 10, 10, 10, 10, 10]]) Example Untrained Model Prediction: tensor([[ 0, 3, 5, 10, 5, 10, 4, 2, 4, 2]]) Example Untrained Model Prediction: tensor([[0, 5, 6, 2, 5, 6, 2, 6, 2, 2]])  
  
Part 2: Model Training  
  
Training  
  
This section describes the training regime for our models.  
  
We stop for a quick interlude to introduce some of the tools needed to train a standard encoder decoder model. First we define a batch object that holds the src and target sentences for training, as well as constructing the masks.  
  
Batches and Masking  
  
class Batch: """Object for holding a batch of data with mask during training.""" def \_\_init\_\_(self, src, tgt=None, pad=2): # 2 =  self.src = src self.src\_mask = (src != pad).unsqueeze(-2) if tgt is not None: self.tgt = tgt[:, :-1] self.tgt\_y = tgt[:, 1:] self.tgt\_mask = self.make\_std\_mask(self.tgt, pad) self.ntokens = (self.tgt\_y != pad).data.sum() @staticmethod def make\_std\_mask(tgt, pad): "Create a mask to hide padding and future words." tgt\_mask = (tgt != pad).unsqueeze(-2) tgt\_mask = tgt\_mask & subsequent\_mask(tgt.size(-1)).type\_as( tgt\_mask.data ) return tgt\_mask  
  
Next we create a generic training and scoring function to keep track of loss. We pass in a generic loss compute function that also handles parameter updates.  
  
Training Loop  
  
class TrainState: """Track number of steps, examples, and tokens processed""" step: int = 0 # Steps in the current epoch accum\_step: int = 0 # Number of gradient accumulation steps samples: int = 0 # total # of examples used tokens: int = 0 # total # of tokens processed  
  
def run\_epoch( data\_iter, model, loss\_compute, optimizer, scheduler, mode="train", accum\_iter=1, train\_state=TrainState(), ): """Train a single epoch""" start = time.time() total\_tokens = 0 total\_loss = 0 tokens = 0 n\_accum = 0 for i, batch in enumerate(data\_iter): out = model.forward( batch.src, batch.tgt, batch.src\_mask, batch.tgt\_mask ) loss, loss\_node = loss\_compute(out, batch.tgt\_y, batch.ntokens) # loss\_node = loss\_node / accum\_iter if mode == "train" or mode == "train+log": loss\_node.backward() train\_state.step += 1 train\_state.samples += batch.src.shape[0] train\_state.tokens += batch.ntokens if i % accum\_iter == 0: optimizer.step() optimizer.zero\_grad(set\_to\_none=True) n\_accum += 1 train\_state.accum\_step += 1 scheduler.step() total\_loss += loss total\_tokens += batch.ntokens tokens += batch.ntokens if i % 40 == 1 and (mode == "train" or mode == "train+log"): lr = optimizer.param\_groups[0]["lr"] elapsed = time.time() - start print( ( "Epoch Step: %6d | Accumulation Step: %3d | Loss: %6.2f " + "| Tokens / Sec: %7.1f | Learning Rate: %6.1e" ) % (i, n\_accum, loss / batch.ntokens, tokens / elapsed, lr) ) start = time.time() tokens = 0 del loss del loss\_node return total\_loss / total\_tokens, train\_state  
  
Training Data and Batching  
  
We trained on the standard WMT 2014 English-German dataset consisting of about 4.5 million sentence pairs. Sentences were encoded using byte-pair encoding, which has a shared source-target vocabulary of about 37000 tokens. For English-French, we used the significantly larger WMT 2014 English-French dataset consisting of 36M sentences and split tokens into a 32000 word-piece vocabulary.  
  
Sentence pairs were batched together by approximate sequence length. Each training batch contained a set of sentence pairs containing approximately 25000 source tokens and 25000 target tokens.  
  
Hardware and Schedule  
  
We trained our models on one machine with 8 NVIDIA P100 GPUs. For our base models using the hyperparameters described throughout the paper, each training step took about 0.4 seconds. We trained the base models for a total of 100,000 steps or 12 hours. For our big models, step time was 1.0 seconds. The big models were trained for 300,000 steps (3.5 days).  
  
Optimizer  
  
We used the Adam optimizer (cite) with \beta\_1=0.9, \beta\_2=0.98 and \epsilon=10^{-9}. We varied the learning rate over the course of training, according to the formula:  
  
lrate = d\_{\text{model}}^{-0.5} \cdot \min({step\\_num}^{-0.5}, {step\\_num} \cdot {warmup\\_steps}^{-1.5})  
  
This corresponds to increasing the learning rate linearly for the first warmup\\_steps training steps, and decreasing it thereafter proportionally to the inverse square root of the step number. We used warmup\\_steps=4000.  
  
Note: This part is very important. Need to train with this setup of the model.  
  
Example of the curves of this model for different model sizes and for optimization hyperparameters.  
  
def rate(step, model\_size, factor, warmup): """ we have to default the step to 1 for LambdaLR function to avoid zero raising to negative power. """ if step == 0: step = 1 return factor \* ( model\_size \*\* (-0.5) \* min(step \*\* (-0.5), step \* warmup \*\* (-1.5)) )  
  
def example\_learning\_schedule(): opts = [ [512, 1, 4000], # example 1 [512, 1, 8000], # example 2 [256, 1, 4000], # example 3 ] dummy\_model = torch.nn.Linear(1, 1) learning\_rates = [] # we have 3 examples in opts list. for idx, example in enumerate(opts): # run 20000 epoch for each example optimizer = torch.optim.Adam( dummy\_model.parameters(), lr=1, betas=(0.9, 0.98), eps=1e-9 ) lr\_scheduler = LambdaLR( optimizer=optimizer, lr\_lambda=lambda step: rate(step, \*example) ) tmp = [] # take 20K dummy training steps, save the learning rate at each step for step in range(20000): tmp.append(optimizer.param\_groups[0]["lr"]) optimizer.step() lr\_scheduler.step() learning\_rates.append(tmp) learning\_rates = torch.tensor(learning\_rates) # Enable altair to handle more than 5000 rows alt.data\_transformers.disable\_max\_rows() opts\_data = pd.concat( [ pd.DataFrame( { "Learning Rate": learning\_rates[warmup\_idx, :], "model\_size:warmup": ["512:4000", "512:8000", "256:4000"][ warmup\_idx ], "step": range(20000), } ) for warmup\_idx in [0, 1, 2] ] ) return ( alt.Chart(opts\_data) .mark\_line() .properties(width=600) .encode(x="step", y="Learning Rate", color="model\_size:warmup:N") .interactive() ) example\_learning\_schedule()  
  
Regularization  
  
Label Smoothing  
  
During training, we employed label smoothing of value \epsilon\_{ls}=0.1 (cite). This hurts perplexity, as the model learns to be more unsure, but improves accuracy and BLEU score.  
  
We implement label smoothing using the KL div loss. Instead of using a one-hot target distribution, we create a distribution that has confidence of the correct word and the rest of the smoothing mass distributed throughout the vocabulary.  
  
class LabelSmoothing(nn.Module): "Implement label smoothing." def \_\_init\_\_(self, size, padding\_idx, smoothing=0.0): super(LabelSmoothing, self).\_\_init\_\_() self.criterion = nn.KLDivLoss(reduction="sum") self.padding\_idx = padding\_idx self.confidence = 1.0 - smoothing self.smoothing = smoothing self.size = size self.true\_dist = None def forward(self, x, target): assert x.size(1) == self.size true\_dist = x.data.clone() true\_dist.fill\_(self.smoothing / (self.size - 2)) true\_dist.scatter\_(1, target.data.unsqueeze(1), self.confidence) true\_dist[:, self.padding\_idx] = 0 mask = torch.nonzero(target.data == self.padding\_idx) if mask.dim() > 0: true\_dist.index\_fill\_(0, mask.squeeze(), 0.0) self.true\_dist = true\_dist return self.criterion(x, true\_dist.clone().detach())  
  
Here we can see an example of how the mass is distributed to the words based on confidence.  
  
# Example of label smoothing. def example\_label\_smoothing(): crit = LabelSmoothing(5, 0, 0.4) predict = torch.FloatTensor( [ [0, 0.2, 0.7, 0.1, 0], [0, 0.2, 0.7, 0.1, 0], [0, 0.2, 0.7, 0.1, 0], [0, 0.2, 0.7, 0.1, 0], [0, 0.2, 0.7, 0.1, 0], ] ) crit(x=predict.log(), target=torch.LongTensor([2, 1, 0, 3, 3])) LS\_data = pd.concat( [ pd.DataFrame( { "target distribution": crit.true\_dist[x, y].flatten(), "columns": y, "rows": x, } ) for y in range(5) for x in range(5) ] ) return ( alt.Chart(LS\_data) .mark\_rect(color="Blue", opacity=1) .properties(height=200, width=200) .encode( alt.X("columns:O", title=None), alt.Y("rows:O", title=None), alt.Color( "target distribution:Q", scale=alt.Scale(scheme="viridis") ), ) .interactive() ) show\_example(example\_label\_smoothing)  
  
Label smoothing actually starts to penalize the model if it gets very confident about a given choice.  
  
def loss(x, crit): d = x + 3 \* 1 predict = torch.FloatTensor([[0, x / d, 1 / d, 1 / d, 1 / d]]) return crit(predict.log(), torch.LongTensor([1])).data def penalization\_visualization(): crit = LabelSmoothing(5, 0, 0.1) loss\_data = pd.DataFrame( { "Loss": [loss(x, crit) for x in range(1, 100)], "Steps": list(range(99)), } ).astype("float") return ( alt.Chart(loss\_data) .mark\_line() .properties(width=350) .encode( x="Steps", y="Loss", ) .interactive() ) show\_example(penalization\_visualization)  
  
A First Example  
  
We can begin by trying out a simple copy-task. Given a random set of input symbols from a small vocabulary, the goal is to generate back those same symbols.  
  
Synthetic Data  
  
def data\_gen(V, batch\_size, nbatches): "Generate random data for a src-tgt copy task." for i in range(nbatches): data = torch.randint(1, V, size=(batch\_size, 10)) data[:, 0] = 1 src = data.requires\_grad\_(False).clone().detach() tgt = data.requires\_grad\_(False).clone().detach() yield Batch(src, tgt, 0)  
  
Loss Computation  
  
class SimpleLossCompute: "A simple loss compute and train function." def \_\_init\_\_(self, generator, criterion): self.generator = generator self.criterion = criterion def \_\_call\_\_(self, x, y, norm): x = self.generator(x) sloss = ( self.criterion( x.contiguous().view(-1, x.size(-1)), y.contiguous().view(-1) ) / norm ) return sloss.data \* norm, sloss  
  
Greedy Decoding  
  
This code predicts a translation using greedy decoding for simplicity.  
  
def greedy\_decode(model, src, src\_mask, max\_len, start\_symbol): memory = model.encode(src, src\_mask) ys = torch.zeros(1, 1).fill\_(start\_symbol).type\_as(src.data) for i in range(max\_len - 1): out = model.decode( memory, src\_mask, ys, subsequent\_mask(ys.size(1)).type\_as(src.data) ) prob = model.generator(out[:, -1]) \_, next\_word = torch.max(prob, dim=1) next\_word = next\_word.data[0] ys = torch.cat( [ys, torch.zeros(1, 1).type\_as(src.data).fill\_(next\_word)], dim=1 ) return ys  
  
# Train the simple copy task. def example\_simple\_model(): V = 11 criterion = LabelSmoothing(size=V, padding\_idx=0, smoothing=0.0) model = make\_model(V, V, N=2) optimizer = torch.optim.Adam( model.parameters(), lr=0.5, betas=(0.9, 0.98), eps=1e-9 ) lr\_scheduler = LambdaLR( optimizer=optimizer, lr\_lambda=lambda step: rate( step, model\_size=model.src\_embed[0].d\_model, factor=1.0, warmup=400 ), ) batch\_size = 80 for epoch in range(20): model.train() run\_epoch( data\_gen(V, batch\_size, 20), model, SimpleLossCompute(model.generator, criterion), optimizer, lr\_scheduler, mode="train", ) model.eval() run\_epoch( data\_gen(V, batch\_size, 5), model, SimpleLossCompute(model.generator, criterion), DummyOptimizer(), DummyScheduler(), mode="eval", )[0] model.eval() src = torch.LongTensor([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]) max\_len = src.shape[1] src\_mask = torch.ones(1, 1, max\_len) print(greedy\_decode(model, src, src\_mask, max\_len=max\_len, start\_symbol=0)) # execute\_example(example\_simple\_model)  
  
Part 3: A Real World Example  
  
Now we consider a real-world example using the Multi30k German-English Translation task. This task is much smaller than the WMT task considered in the paper, but it illustrates the whole system. We also show how to use multi-gpu processing to make it really fast.  
  
Data Loading  
  
We will load the dataset using torchtext and spacy for tokenization.  
  
# Load spacy tokenizer models, download them if they haven't been # downloaded already def load\_tokenizers(): try: spacy\_de = spacy.load("de\_core\_news\_sm") except IOError: os.system("python -m spacy download de\_core\_news\_sm") spacy\_de = spacy.load("de\_core\_news\_sm") try: spacy\_en = spacy.load("en\_core\_web\_sm") except IOError: os.system("python -m spacy download en\_core\_web\_sm") spacy\_en = spacy.load("en\_core\_web\_sm") return spacy\_de, spacy\_en  
  
def tokenize(text, tokenizer): return [tok.text for tok in tokenizer.tokenizer(text)] def yield\_tokens(data\_iter, tokenizer, index): for from\_to\_tuple in data\_iter: yield tokenizer(from\_to\_tuple[index])  
  
def build\_vocabulary(spacy\_de, spacy\_en): def tokenize\_de(text): return tokenize(text, spacy\_de) def tokenize\_en(text): return tokenize(text, spacy\_en) print("Building German Vocabulary ...") train, val, test = datasets.Multi30k(language\_pair=("de", "en")) vocab\_src = build\_vocab\_from\_iterator( yield\_tokens(train + val + test, tokenize\_de, index=0), min\_freq=2, specials=["~~", "~~", "", ""], ) print("Building English Vocabulary ...") train, val, test = datasets.Multi30k(language\_pair=("de", "en")) vocab\_tgt = build\_vocab\_from\_iterator( yield\_tokens(train + val + test, tokenize\_en, index=1), min\_freq=2, specials=["~~", "~~", "", ""], ) vocab\_src.set\_default\_index(vocab\_src[""]) vocab\_tgt.set\_default\_index(vocab\_tgt[""]) return vocab\_src, vocab\_tgt def load\_vocab(spacy\_de, spacy\_en): if not exists("vocab.pt"): vocab\_src, vocab\_tgt = build\_vocabulary(spacy\_de, spacy\_en) torch.save((vocab\_src, vocab\_tgt), "vocab.pt") else: vocab\_src, vocab\_tgt = torch.load("vocab.pt") print("Finished.  
  
Vocabulary sizes:") print(len(vocab\_src)) print(len(vocab\_tgt)) return vocab\_src, vocab\_tgt if is\_interactive\_notebook(): # global variables used later in the script spacy\_de, spacy\_en = show\_example(load\_tokenizers) vocab\_src, vocab\_tgt = show\_example(load\_vocab, args=[spacy\_de, spacy\_en])  
  
Finished. Vocabulary sizes: 59981 36745  
  
Batching matters a ton for speed. We want to have very evenly divided batches, with absolutely minimal padding. To do this we have to hack a bit around the default torchtext batching. This code patches their default batching to make sure we search over enough sentences to find tight batches.  
  
Iterators  
  
def collate\_batch( batch, src\_pipeline, tgt\_pipeline, src\_vocab, tgt\_vocab, device, max\_padding=128, pad\_id=2, ): bs\_id = torch.tensor([0], device=device) #  ~~token id eos\_id = torch.tensor([1], device=device) #~~  token id src\_list, tgt\_list = [], [] for (\_src, \_tgt) in batch: processed\_src = torch.cat( [ bs\_id, torch.tensor( src\_vocab(src\_pipeline(\_src)), dtype=torch.int64, device=device, ), eos\_id, ], 0, ) processed\_tgt = torch.cat( [ bs\_id, torch.tensor( tgt\_vocab(tgt\_pipeline(\_tgt)), dtype=torch.int64, device=device, ), eos\_id, ], 0, ) src\_list.append( # warning - overwrites values for negative values of padding - len pad( processed\_src, ( 0, max\_padding - len(processed\_src), ), value=pad\_id, ) ) tgt\_list.append( pad( processed\_tgt, (0, max\_padding - len(processed\_tgt)), value=pad\_id, ) ) src = torch.stack(src\_list) tgt = torch.stack(tgt\_list) return (src, tgt)  
  
def create\_dataloaders( device, vocab\_src, vocab\_tgt, spacy\_de, spacy\_en, batch\_size=12000, max\_padding=128, is\_distributed=True, ): # def create\_dataloaders(batch\_size=12000): def tokenize\_de(text): return tokenize(text, spacy\_de) def tokenize\_en(text): return tokenize(text, spacy\_en) def collate\_fn(batch): return collate\_batch( batch, tokenize\_de, tokenize\_en, vocab\_src, vocab\_tgt, device, max\_padding=max\_padding, pad\_id=vocab\_src.get\_stoi()[""], ) train\_iter, valid\_iter, test\_iter = datasets.Multi30k( language\_pair=("de", "en") ) train\_iter\_map = to\_map\_style\_dataset( train\_iter ) # DistributedSampler needs a dataset len() train\_sampler = ( DistributedSampler(train\_iter\_map) if is\_distributed else None ) valid\_iter\_map = to\_map\_style\_dataset(valid\_iter) valid\_sampler = ( DistributedSampler(valid\_iter\_map) if is\_distributed else None ) train\_dataloader = DataLoader( train\_iter\_map, batch\_size=batch\_size, shuffle=(train\_sampler is None), sampler=train\_sampler, collate\_fn=collate\_fn, ) valid\_dataloader = DataLoader( valid\_iter\_map, batch\_size=batch\_size, shuffle=(valid\_sampler is None), sampler=valid\_sampler, collate\_fn=collate\_fn, ) return train\_dataloader, valid\_dataloader  
  
Training the System  
  
def train\_worker( gpu, ngpus\_per\_node, vocab\_src, vocab\_tgt, spacy\_de, spacy\_en, config, is\_distributed=False, ): print(f"Train worker process using GPU: {gpu} for training", flush=True) torch.cuda.set\_device(gpu) pad\_idx = vocab\_tgt[""] d\_model = 512 model = make\_model(len(vocab\_src), len(vocab\_tgt), N=6) model.cuda(gpu) module = model is\_main\_process = True if is\_distributed: dist.init\_process\_group( "nccl", init\_method="env://", rank=gpu, world\_size=ngpus\_per\_node ) model = DDP(model, device\_ids=[gpu]) module = model.module is\_main\_process = gpu == 0 criterion = LabelSmoothing( size=len(vocab\_tgt), padding\_idx=pad\_idx, smoothing=0.1 ) criterion.cuda(gpu) train\_dataloader, valid\_dataloader = create\_dataloaders( gpu, vocab\_src, vocab\_tgt, spacy\_de, spacy\_en, batch\_size=config["batch\_size"] // ngpus\_per\_node, max\_padding=config["max\_padding"], is\_distributed=is\_distributed, ) optimizer = torch.optim.Adam( model.parameters(), lr=config["base\_lr"], betas=(0.9, 0.98), eps=1e-9 ) lr\_scheduler = LambdaLR( optimizer=optimizer, lr\_lambda=lambda step: rate( step, d\_model, factor=1, warmup=config["warmup"] ), ) train\_state = TrainState() for epoch in range(config["num\_epochs"]): if is\_distributed: train\_dataloader.sampler.set\_epoch(epoch) valid\_dataloader.sampler.set\_epoch(epoch) model.train() print(f"[GPU{gpu}] Epoch {epoch} Training ====", flush=True) \_, train\_state = run\_epoch( (Batch(b[0], b[1], pad\_idx) for b in train\_dataloader), model, SimpleLossCompute(module.generator, criterion), optimizer, lr\_scheduler, mode="train+log", accum\_iter=config["accum\_iter"], train\_state=train\_state, ) GPUtil.showUtilization() if is\_main\_process: file\_path = "%s%.2d.pt" % (config["file\_prefix"], epoch) torch.save(module.state\_dict(), file\_path) torch.cuda.empty\_cache() print(f"[GPU{gpu}] Epoch {epoch} Validation ====", flush=True) model.eval() sloss = run\_epoch( (Batch(b[0], b[1], pad\_idx) for b in valid\_dataloader), model, SimpleLossCompute(module.generator, criterion), DummyOptimizer(), DummyScheduler(), mode="eval", ) print(sloss) torch.cuda.empty\_cache() if is\_main\_process: file\_path = "%sfinal.pt" % config["file\_prefix"] torch.save(module.state\_dict(), file\_path)  
  
def train\_distributed\_model(vocab\_src, vocab\_tgt, spacy\_de, spacy\_en, config): from the\_annotated\_transformer import train\_worker ngpus = torch.cuda.device\_count() os.environ["MASTER\_ADDR"] = "localhost" os.environ["MASTER\_PORT"] = "12356" print(f"Number of GPUs detected: {ngpus}") print("Spawning training processes ...") mp.spawn( train\_worker, nprocs=ngpus, args=(ngpus, vocab\_src, vocab\_tgt, spacy\_de, spacy\_en, config, True), ) def train\_model(vocab\_src, vocab\_tgt, spacy\_de, spacy\_en, config): if config["distributed"]: train\_distributed\_model( vocab\_src, vocab\_tgt, spacy\_de, spacy\_en, config ) else: train\_worker( 0, 1, vocab\_src, vocab\_tgt, spacy\_de, spacy\_en, config, False ) def load\_trained\_model(): config = { "batch\_size": 32, "distributed": False, "num\_epochs": 8, "accum\_iter": 10, "base\_lr": 1.0, "max\_padding": 72, "warmup": 3000, "file\_prefix": "multi30k\_model\_", } model\_path = "multi30k\_model\_final.pt" if not exists(model\_path): train\_model(vocab\_src, vocab\_tgt, spacy\_de, spacy\_en, config) model = make\_model(len(vocab\_src), len(vocab\_tgt), N=6) model.load\_state\_dict(torch.load("multi30k\_model\_final.pt")) return model if is\_interactive\_notebook(): model = load\_trained\_model()  
  
Once trained we can decode the model to produce a set of translations. Here we simply translate the first sentence in the validation set. This dataset is pretty small so the translations with greedy search are reasonably accurate.  
  
Additional Components: BPE, Search, Averaging  
  
So this mostly covers the transformer model itself. There are four aspects that we didn’t cover explicitly. We also have all these additional features implemented in OpenNMT-py.  
  
BPE/ Word-piece: We can use a library to first preprocess the data into subword units. See Rico Sennrich’s subword-nmt implementation. These models will transform the training data to look like this:  
  
▁Die ▁Protokoll datei ▁kann ▁ heimlich ▁per ▁E - Mail ▁oder ▁FTP ▁an ▁einen ▁bestimmte n ▁Empfänger ▁gesendet ▁werden .  
  
Shared Embeddings: When using BPE with shared vocabulary we can share the same weight vectors between the source / target / generator. See the (cite) for details. To add this to the model simply do this:  
  
if False: model.src\_embed[0].lut.weight = model.tgt\_embeddings[0].lut.weight model.generator.lut.weight = model.tgt\_embed[0].lut.weight  
  
Beam Search: This is a bit too complicated to cover here. See the OpenNMT-py for a pytorch implementation.  
  
Model Averaging: The paper averages the last k checkpoints to create an ensembling effect. We can do this after the fact if we have a bunch of models:  
  
def average(model, models): "Average models into model" for ps in zip(\*[m.params() for m in [model] + models]): ps[0].copy\_(torch.sum(\*ps[1:]) / len(ps[1:]))  
  
Results  
  
On the WMT 2014 English-to-German translation task, the big transformer model (Transformer (big) in Table 2) outperforms the best previously reported models (including ensembles) by more than 2.0 BLEU, establishing a new state-of-the-art BLEU score of 28.4. The configuration of this model is listed in the bottom line of Table 3. Training took 3.5 days on 8 P100 GPUs. Even our base model surpasses all previously published models and ensembles, at a fraction of the training cost of any of the competitive models.  
  
On the WMT 2014 English-to-French translation task, our big model achieves a BLEU score of 41.0, outperforming all of the previously published single models, at less than 1/4 the training cost of the previous state-of-the-art model. The Transformer (big) model trained for English-to-French used dropout rate Pdrop = 0.1, instead of 0.3.  
  
With the addtional extensions in the last section, the OpenNMT-py replication gets to 26.9 on EN-DE WMT. Here I have loaded in those parameters to our reimplemenation.  
  
# Load data and model for output checks  
  
def check\_outputs( valid\_dataloader, model, vocab\_src, vocab\_tgt, n\_examples=15, pad\_idx=2, eos\_string="", ): results = [()] \* n\_examples for idx in range(n\_examples): print("  
  
Example %d ========  
  
" % idx) b = next(iter(valid\_dataloader)) rb = Batch(b[0], b[1], pad\_idx) greedy\_decode(model, rb.src, rb.src\_mask, 64, 0)[0] src\_tokens = [ vocab\_src.get\_itos()[x] for x in rb.src[0] if x != pad\_idx ] tgt\_tokens = [ vocab\_tgt.get\_itos()[x] for x in rb.tgt[0] if x != pad\_idx ] print( "Source Text (Input) : " + " ".join(src\_tokens).replace("  
  
", "") ) print( "Target Text (Ground Truth) : " + " ".join(tgt\_tokens).replace("  
  
", "") ) model\_out = greedy\_decode(model, rb.src, rb.src\_mask, 72, 0)[0] model\_txt = ( " ".join( [vocab\_tgt.get\_itos()[x] for x in model\_out if x != pad\_idx] ).split(eos\_string, 1)[0] + eos\_string ) print("Model Output : " + model\_txt.replace("  
  
", "")) results[idx] = (rb, src\_tokens, tgt\_tokens, model\_out, model\_txt) return results def run\_model\_example(n\_examples=5): global vocab\_src, vocab\_tgt, spacy\_de, spacy\_en print("Preparing Data ...") \_, valid\_dataloader = create\_dataloaders( torch.device("cpu"), vocab\_src, vocab\_tgt, spacy\_de, spacy\_en, batch\_size=1, is\_distributed=False, ) print("Loading Trained Model ...") model = make\_model(len(vocab\_src), len(vocab\_tgt), N=6) model.load\_state\_dict( torch.load("multi30k\_model\_final.pt", map\_location=torch.device("cpu")) ) print("Checking Model Outputs:") example\_data = check\_outputs( valid\_dataloader, model, vocab\_src, vocab\_tgt, n\_examples=n\_examples ) return model, example\_data # execute\_example(run\_model\_example)  
  
Attention Visualization  
  
Even with a greedy decoder the translation looks pretty good. We can further visualize it to see what is happening at each layer of the attention  
  
def mtx2df(m, max\_row, max\_col, row\_tokens, col\_tokens): "convert a dense matrix to a data frame with row and column indices" return pd.DataFrame( [ ( r, c, float(m[r, c]), "%.3d %s" % (r, row\_tokens[r] if len(row\_tokens) > r else ""), "%.3d %s" % (c, col\_tokens[c] if len(col\_tokens) > c else ""), ) for r in range(m.shape[0]) for c in range(m.shape[1]) if r < max\_row and c < max\_col ], # if float(m[r,c]) != 0 and r < max\_row and c < max\_col], columns=["row", "column", "value", "row\_token", "col\_token"], ) def attn\_map(attn, layer, head, row\_tokens, col\_tokens, max\_dim=30): df = mtx2df( attn[0, head].data, max\_dim, max\_dim, row\_tokens, col\_tokens, ) return ( alt.Chart(data=df) .mark\_rect() .encode( x=alt.X("col\_token", axis=alt.Axis(title="")), y=alt.Y("row\_token", axis=alt.Axis(title="")), color="value", tooltip=["row", "column", "value", "row\_token", "col\_token"], ) .properties(height=400, width=400) .interactive() )  
  
def get\_encoder(model, layer): return model.encoder.layers[layer].self\_attn.attn def get\_decoder\_self(model, layer): return model.decoder.layers[layer].self\_attn.attn def get\_decoder\_src(model, layer): return model.decoder.layers[layer].src\_attn.attn def visualize\_layer(model, layer, getter\_fn, ntokens, row\_tokens, col\_tokens): # ntokens = last\_example[0].ntokens attn = getter\_fn(model, layer) n\_heads = attn.shape[1] charts = [ attn\_map( attn, 0, h, row\_tokens=row\_tokens, col\_tokens=col\_tokens, max\_dim=ntokens, ) for h in range(n\_heads) ] assert n\_heads == 8 return alt.vconcat( charts[0] # | charts[1] | charts[2] # | charts[3] | charts[4] # | charts[5] | charts[6] # | charts[7] # layer + 1 due to 0-indexing ).properties(title="Layer %d" % (layer + 1))  
  
Encoder Self Attention  
  
def viz\_encoder\_self(): model, example\_data = run\_model\_example(n\_examples=1) example = example\_data[ len(example\_data) - 1 ] # batch object for the final example layer\_viz = [ visualize\_layer( model, layer, get\_encoder, len(example[1]), example[1], example[1] ) for layer in range(6) ] return alt.hconcat( layer\_viz[0] # & layer\_viz[1] & layer\_viz[2] # & layer\_viz[3] & layer\_viz[4] # & layer\_viz[5] ) show\_example(viz\_encoder\_self)  
  
Preparing Data ... Loading Trained Model ... Checking Model Outputs: Example 0 ======== Source Text (Input) :  ~~Zwei Frauen in pinkfarbenen T-Shirts und  unterhalten sich vor einem  .~~  Target Text (Ground Truth) :  ~~Two women wearing pink T - shirts and blue jeans converse outside clothing store .~~  Model Output :  ~~Two women in pink shirts and face are talking in front of a  .~~   
  
Decoder Self Attention  
  
def viz\_decoder\_self(): model, example\_data = run\_model\_example(n\_examples=1) example = example\_data[len(example\_data) - 1] layer\_viz = [ visualize\_layer( model, layer, get\_decoder\_self, len(example[1]), example[1], example[1], ) for layer in range(6) ] return alt.hconcat( layer\_viz[0] & layer\_viz[1] & layer\_viz[2] & layer\_viz[3] & layer\_viz[4] & layer\_viz[5] ) show\_example(viz\_decoder\_self)  
  
Preparing Data ... Loading Trained Model ... Checking Model Outputs: Example 0 ======== Source Text (Input) :  ~~Eine Gruppe von Männern in Kostümen spielt Musik .~~  Target Text (Ground Truth) :  ~~A group of men in costume play music .~~  Model Output :  ~~A group of men in costumes playing music .~~   
  
Decoder Src Attention  
  
def viz\_decoder\_src(): model, example\_data = run\_model\_example(n\_examples=1) example = example\_data[len(example\_data) - 1] layer\_viz = [ visualize\_layer( model, layer, get\_decoder\_src, max(len(example[1]), len(example[2])), example[1], example[2], ) for layer in range(6) ] return alt.hconcat( layer\_viz[0] & layer\_viz[1] & layer\_viz[2] & layer\_viz[3] & layer\_viz[4] & layer\_viz[5] ) show\_example(viz\_decoder\_src)  
  
Preparing Data ... Loading Trained Model ... Checking Model Outputs: Example 0 ======== Source Text (Input) :  ~~Ein kleiner Junge verwendet einen Bohrer , um ein Loch in ein Holzstück zu machen .~~  Target Text (Ground Truth) :  ~~A little boy using a drill to make a hole in a piece of wood .~~  Model Output :  ~~A little boy uses a machine to be working in a hole in a log .~~   
  
Conclusion  
  
Hopefully this code is useful for future research. Please reach out if you have any issues.  
  
Cheers, Sasha Rush, Austin Huang, Suraj Subramanian, Jonathan Sum, Khalid Almubarak, Stella Biderman