# Content from https://www.alibabacloud.com/blog/announcing-hanguang-800-alibabas-first-ai-inference-chip_595482

*Retrieved: 2025-09-15T05:46:31.886242*

---

<!DOCTYPE html>
<html lang="en" class="sub-site-nav alicloud-header alicloud-footer">
<head>
  <meta charset="UTF-8">
  <title>Announcing Hanguang 800: Alibaba&#039;s First AI-Inference Chip - Alibaba Cloud Community</title>
  <link rel="shortcut icon" href="https://img.alicdn.com/tfs/TB1ugg7M9zqK1RjSZPxXXc4tVXa-32-32.png" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="keywords" content="performance,AI,Wujian,Hanguang 800,Aspara Conference,Computing Power,Xuantie" />
  <meta name="description" content="Although new at the chip-making game, Alibaba are showing that there&#039;s loads of innovation to be made in AI-centric chip manufacturing and development.">
  <meta name="csrf-param" content="yunqi_csrf"/>
  <meta name="csrf-token" content="UJAB0ZF69A"/>
  <meta name="data-spm" content="a2c65">
    <meta name="aplus-rhost-v" content="sg.mmstat.com">
  <meta name="aplus-rhost-g" content="sg.mmstat.com">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
 <link rel="stylesheet" type="text/css" href="//g.alicdn.com/??alicloud-components/alicloud-ui3/0.0.7/acUI.css,alicloud-components/acApp/0.0.3/app.css,alicloud-components/i18n/0.0.29/css/en-us/index.css,alicloud-components/iconfont/0.0.7/product-icon.css">
  <link rel="stylesheet" type="text/css" href="//g.alicdn.com/aliyun-international/blog-assert/0.0.23/css/detail.css">
  <link rel="stylesheet" type="text/css" href="//g.alicdn.com/aliyun-international/blog-assert/0.0.23/css/nav.css">
      <link rel="stylesheet" type="text/css" href="//g.alicdn.com/aliyun-international/blog-assert/0.0.23/fonts/iconfont.css">
  <link rel="stylesheet"  type="text/css" href="https://g.alicdn.com/ali-mod/b-alicloud-v3-bottom/0.0.19/index.css">
      <link rel="stylesheet" type="text/css" href="//g.alicdn.com/aliyun-international/blog-assert/0.0.23/fonts/iconfont.css">
    <meta property="og:url" content="https://www.alibabacloud.com/blog/announcing-hanguang-800-alibabas-first-ai-inference-chip_595482">
    <meta property="og:site_name" content="Alibaba Cloud Community">
    <meta property="og:title" content="Announcing Hanguang 800: Alibaba&#039;s First AI-Inference Chip">
    <meta property="og:description" content="Although new at the chip-making game, Alibaba are showing that there&#039;s loads of innovation to be made in AI-centric chip manufacturing and development.">
    <meta property="og:image" content="https://yqintl.alicdn.com/783df73e7f6c3d0b35afbce68219fcef4dafeb3c.jpeg">    <meta property="og:image:type" content="image/png">
    <meta property="twitter:creator" content="Alibaba Cloud Community">
    <meta property="twitter:card" content="summary_large_image">
    <meta property="twitter:title" content="Announcing Hanguang 800: Alibaba&#039;s First AI-Inference Chip">
    <meta property="twitter:description" content="Although new at the chip-making game, Alibaba are showing that there&#039;s loads of innovation to be made in AI-centric chip manufacturing and development.">
    <meta property="twitter:image:src" content="https://yqintl.alicdn.com/783df73e7f6c3d0b35afbce68219fcef4dafeb3c.jpeg">  <script src="//g.alicdn.com/??alicloud-components/kloud/0.0.31/vendor/requirejs/require.js,alicloud-components/kloud/0.0.1/scripts/vendor/jquery/jquery.min.js,alicloud-components/common/scripts/layout.js,alicloud-components/alicloud-ui3/0.0.7/acUI.js"></script>
  <script src="//g.alicdn.com/aliyun-international/blog-assert/0.0.23/js/layout.js"></script>
</head>

<body data-spm="11461447"><script type="text/javascript">
(function (d) {
var t=d.createElement("script");t.type="text/javascript";t.async=true;t.id="tb-beacon-aplus";
t.setAttribute("exparams","category=&userid=&aplus&yunid=&yunpk=&channel=&cps=");
t.src="//g.alicdn.com/alilog/mlog/aplus_v2.js";
d.getElementsByTagName("head")[0].appendChild(t);
})(document);
</script>

<div class="blog-nav">
    <div class="container">
      <div class="row">
        <h1>
          Community
        </h1>
        <main class="blog-nav-center">
          <a href="https://www.alibabacloud.com/blog/" class="bg">
             Blog
          </a>

          <a href="https://resource.alibabacloud.com/event/index">
             Events
          </a>
          <a href="https://resource.alibabacloud.com/webinar/index.htm">
             Webinars
          </a>

          <a href="https://community.alibabacloud.com/tags/type_blog-tagid_28404/">
              Tutorials
          </a>
          <a href="https://www.alibabacloud.com/forum">
              Forum
          </a>
        </main>

        <ul class="blog-nav-right">
          <li class="search"><input type="text" placeholder="Search" id="search">
          <i class="search-btn k-iconfont icon-sousuo1"></i>
           <div class="close-box"><img data-original="https://img.alicdn.com/tfs/TB1BIBBsbPpK1RjSZFFXXa5PpXa-24-24.png"
                                data-toggle="lazy-loading" class="off" /><img data-original="https://img.alicdn.com/tfs/TB1vrJ2shnaK1RjSZFBXXcW7VXa-24-24.png"
                                data-toggle="lazy-loading" class="on" /></div>

                        </li>
                       </ul>

        <div class="blog-nav-right-m">
          <i class="k-iconfont icon-sousuo1 show-search"></i>
          <i class="show-more"></i>
        </div>
      </div>
      <div class="blog-nav-main-m">
        <ol>
          <li><a href="https://community.alibabacloud.com">Blog</a></li>
           <li>
            <a href="https://resource.alibabacloud.com/event/index">
             Events
            </a>
           </li>
           <li>
             <a href="https://resource.alibabacloud.com/webinar/index.htm">
              Webinars
             </a>
           </li>
           <li>
             <a href="https://www.alibabacloud.com/getting-started/projects">
               Tutorials
             </a>
           </li>
           <li>
              <a href="https://www.alibabacloud.com/forum">
                Forum
              </a>
           </li>
                  </ol>
        <div class="btn-box">
                    <a href="https://account.alibabacloud.com/register/register.htm?from_type=yqclub&amp;oauth_callback=https%3A%2F%2Fwww.alibabacloud.com%2Fblog%2Fannouncing-hanguang-800-alibabas-first-ai-inference-chip_595482%3Fdo%3Dlogin" class="free" style="display: block;">
             Create Account
          </a>
          <a href="https://account.alibabacloud.com/login/login.htm?from_type=yqclub&amp;oauth_callback=https%3A%2F%2Fwww.alibabacloud.com%2Fblog%2Fannouncing-hanguang-800-alibabas-first-ai-inference-chip_595482%3Fdo%3Dlogin" class="login" style="display: block;">
             Log In
          </a>
                  </div>
      </div>
      <div class="container blog-nav-search-m">
        <div class="blog-nav-search-m-top">
          <input type="text" placeholder="Search" class="int-search">
          <button>
            <i class="k-iconfont icon-sousuo1"></i>
          </button>
          <span>
             ×
          </span>
        </div>

      </div>
    </div>
  </div>
      <div class="wrap container">
        <div class="wrap-top">
            <a href="https://community.alibabacloud.com">Community</a>
            <i class="icon icon-more"></i>
            <a href="https://www.alibabacloud.com/blog/">Blog</a>
            <i class="icon icon-more"></i>
            Announcing Hanguang 800: Alibaba&#039;s First AI-Inference Chip
        </div>
        <div class="wrap-main">
            <div class="col-md-8">
                <div class="wrap-main-left">
                    <h1>
                                                Announcing Hanguang 800: Alibaba&#039;s First AI-Inference Chip
                                            </h1>
                    <aside>
                        <main>
                            <a href="https://community.alibabacloud.com/users/5040995529404844">Alibaba Clouder</a>
                            <span>October 28, 2019</span>
                            <span>
                                <img src="https://img.alicdn.com/tfs/TB19L9AbXuWBuNjSspnXXX1NVXa-40-26.png" alt=""> 38,324
                            </span>
                            <a href="#comment">
                                <i class="icon icon-pinglun"></i><b class="comments-num">0</b>
                            </a>
                        </main>
                        <div>
                                                                                                                                </div>
                    </aside>
                    <div class="wrap-main-left-abstract">
                        Although new at the chip-making game, Alibaba are showing that there&#039;s loads of innovation to be made in AI-centric chip manufacturing and development.
                    </div>
                    <div class="wrap-main-left-article markdown-body">

<blockquote><p>Relive the best moments of the Apsara Conference 2019 at <a href="https://www.alibabacloud.com/apsara-conference-2019" target="_blank">https://www.alibabacloud.com/apsara-conference-2019</a>.</p></blockquote>
<p><img src="https://yqintl.alicdn.com/d80fe435eaca2a3b6be61c50249d3a5272615283.jpeg" alt="1" title="1"></p>
<p>Jeff Zhang, Dean of <a href="https://damo.alibaba.com/?spm=a2c65.11461447.0.0.1d7c4baed1M3OY" target="_blank">Alibaba DAMO Academy</a>, unveiled Alibaba's first AI inference chip, Hanguang 800, during Apsara Conference on September 25, 2019. Hanguang 800 is the world's most powerful AI inference chip. In the Resnet-50 industry test, the peak performance of the new chip reached a whopping 78,563 images per second, which is four times higher than the second best AI chip in the world. The peak efficiency of the chip also reached 500 IPS/W, which is 3.3 times higher than the second best option.</p>
<p><img src="https://yqintl.alicdn.com/d86844ec4f12aca9690739132f0a489a55d641a9.jpeg" alt="2" title="2"></p>
<p>"Alibaba is a new player in the chip industry. The launches of <a href="https://www.alibabacloud.com/blog/alibaba-is-showing-the-world-that-a-good-swordsman-doesnt-need-a-sword_595376" target="_blank">XuanTie</a> 910 and now Hanguang 800 are only the first steps towards a new chip revolution," Jeff Zhang said in a statement.</p>
<p>Hanguang, roughly translated as Sword of Light, is named after a legendary sword from Chinese mythology, said to be invisible but provide the swordsman wielding it with incredible power. A Hanguang 800 chip can offer the computing power equivalent to 10 traditional GPUs. Something that has been wholly confirmed from initial tests and application in the Hangzhou <a href="https://www.alibabacloud.com/et/city?spm=a2c65.11461447.0.0.1d7c4baed1M3OY" target="_blank">City Brian</a> project.</p>
<p><img src="https://yqintl.alicdn.com/d1a016eeee82963797c513247e063cda02726720.jpeg" alt="3" title="3"></p>
<p><img src="https://yqintl.alicdn.com/333dd716a8e49f00702fd0184366f71f315e798c.jpeg" alt="4" title="4"></p>
<p>Hanguang 800 is the result of a culmination of both software and hardware development. In terms of hardware, it uses an in-house designed chip that takes advantage of such technologies as <a href="https://medium.com/syncedreview/deep-learning-in-real-time-inference-acceleration-and-continuous-training-17dac9438b0b" target="_blank">inference acceleration</a>, which can help to resolve traditional performance bottlenecks. Next, on the software side, the chip is integrated with several algorithms developed at the DAMO Academy, which are specifically optimized for <a href="https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53" target="_blank">convolutional neural network</a> (CNN) and computer vision algorithms, granting the tiny neural processing unit (NPU) the capacity to complete the computing operations of a large neural network.</p>
<p><img src="https://yqintl.alicdn.com/dc24935dd73121e02fb5c69fc624c41d814ac433.jpeg" alt="5" title="5"></p>
<p><img src="https://yqintl.alicdn.com/c1bdef080b9577e493a95fb9c09b980476e2e98f.jpeg" alt="6" title="6"></p>
<p>The chip has already been applied and tested in some of the core business units of Alibaba Group. At the conference, it was revealed that the new chip was used in the City Brain project in Hangzhou to excellent results. For the project, previously 40 GPUs were needed to process the video feeds generated from the main urban districts of Hangzhou, but the same job could be done with only 4 Hanguang 800 chips. Also, at the same time, with the new chip, latency could be reduced from 300 to 150 milliseconds.</p>
<p>An AI cloud service developed based on Hanguang 800 was also launched on the same day in this year's Apsara Conference. Powered by the new chip, the service offers a much higher cost-performance ratio, with up to 100% in performance increases, compared to traditional GPUs. </p>
<p>Connected with these announcements, Alibaba's semiconductor subsidiary <a href="https://www.eenewsanalog.com/news/alibaba-forms-chip-subsidiary-pingtouge" target="_blank">Pingtouge</a> over the past six months has also launched the <a href="https://www.techrepublic.com/article/alibaba-releases-their-first-risc-v-cpu-as-open-source-solution-for-5g-ai/" target="_blank">XuanTie 910</a> processor and <a href="https://www.alibabacloud.com/blog/alibaba-is-showing-the-world-that-a-good-swordsman-doesnt-need-a-sword_595376" target="_blank">Wujian SoC chip platform</a>. The launch of Hanguang 800 marks Alibaba as being well on its way to providing an innovative chip suite for cloud and edge computing scenarios—one that covers chip processors, all-in-one chip development platforms, and, as of now, AI inference chips.</p>
<p><img src="https://yqintl.alicdn.com/381df0744ac8aa0b282695f0a902242ccb615d96.jpeg" alt="7" title="7"></p>

</div>
                                        <div class="wrap-main-left-bar">
                                                <span><a href="https://community.alibabacloud.com/tags/type_blog-tagid_2512/">performance</a></span>
                                            <span><a href="https://community.alibabacloud.com/tags/type_blog-tagid_3219/">AI</a></span>
                                            <span><a href="https://community.alibabacloud.com/tags/type_blog-tagid_29808/">Wujian</a></span>
                                            <span><a href="https://community.alibabacloud.com/tags/type_blog-tagid_29858/">Hanguang 800</a></span>
                                            <span><a href="https://community.alibabacloud.com/tags/type_blog-tagid_30059/">Aspara Conference</a></span>
                                            <span><a href="https://community.alibabacloud.com/tags/type_blog-tagid_30060/">Computing Power</a></span>
                                            <span><a href="https://community.alibabacloud.com/tags/type_blog-tagid_30061/">Xuantie</a></span>
                                        </div>
                                        <div class="wrap-main-left-action">
                        <main>
                            <a href="#comment">
                                <i class="icon icon-pinglun"></i>
                                0
                            </a>
                            <span class="action-zan" data-islogin="false" data-id="595482" data-already="false" rel="nofollow">
                                <i class="icon icon-zan"></i>
                                <b>0</b>
                            </span>
                            <span class="action-love" data-islogin="false" data-id="595482" data-already="false" rel="nofollow">
                                <i class="icon icon-love"></i>
                                <b>0</b>
                            </span>
                        </main>
                        <div>
                            <b>Share on</b>
                            <a href="javascript:;" class="sharer" data-sharer="linkedin" data-url="" title="Announcing Hanguang 800: Alibaba&#039;s First AI-Inference Chip">
                                <i class="icon icon-linkedin1"></i>
                            </a>
                            <a href="javascript:;" class="sharer" data-sharer="facebook" data-url="" title="Announcing Hanguang 800: Alibaba&#039;s First AI-Inference Chip">
                                <i class="icon icon-lianshu1"></i>
                            </a>
                            <a href="javascript:;" class="sharer" data-sharer="twitter" data-url="" title="Announcing Hanguang 800: Alibaba&#039;s First AI-Inference Chip">
                                <i class="icon icon-twitter1"></i>
                            </a>
                                                                                                                </div>
                    </div>
                    <div class="wrap-main-left-read">
                                                <main>
                            <h2>
                                Read previous post:
                            </h2>
                            <p>
                                <a href="/blog/how-to-deploy-a-node-js-application-on-centos-with-alibaba-cloud-starter-package_595481">
                                    How to Deploy a Node.js Application on CentOS with Alibaba Cloud Starter Package
                                </a>
                            </p>
                        </main>
                                                                        <main>
                            <h2>
                                Read next post:
                            </h2>
                            <p>
                                <a href="/blog/alibaba-reveals-its-true-power-as-an-ai-machine_595483">
                                    Alibaba Reveals Its True Power as an AI Machine
                                </a>
                            </p>
                        </main>
                                            </div>
                    <div class="wrap-main-right-user wrap-main-right-user-mobile">
                        <dl>
                            <dt>
                                <a href="https://community.alibabacloud.com/users/5040995529404844">
                                <img src="https://yqintl.alicdn.com/img_572d495de1d399a4388a7656634ed8c7.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="">
                                </a>
                            </dt>
                            <dd>
                                <h1>
                                <a href="https://community.alibabacloud.com/users/5040995529404844">
                                    Alibaba Clouder
                                </a>
                                </h1>
                                <p>
                                    2,593 posts | 784 followers
                                </p>
                                                                                                        <a href="#" class="follow-btn" data-islogin="false" data-uid="5040995529404844" data-isfollowed="false" id="follow-btn" rel="nofollow">Follow</a>
                                                                                                </dd>
                        </dl>
                    </div>
                                        <h3>
                        You may also like
                    </h3>
                    <ul class="wrap-main-left-list">
                                                <li>
                            <span></span>
                            <a href="/blog/accelerate-deep-neural-network-with-ai-chips_595507">
                                Accelerate Deep Neural Network with AI Chips
                            </a>
                            <p>
                                Alibaba Clouder - November 1, 2019
                            </p>
                        </li>
                                                <li>
                            <span></span>
                            <a href="/blog/new-alibaba-ai-chip-with-10-times-the-computing-power-of-traditional-gpus_595464">
                                New Alibaba AI Chip with 10 Times the Computing Power of Traditional GPUs
                            </a>
                            <p>
                                Alibaba Clouder - October 22, 2019
                            </p>
                        </li>
                                                <li>
                            <span></span>
                            <a href="/blog/some-of-the-major-topics-from-apsara-conference-2019_595477">
                                Some of the Major Topics from Apsara Conference 2019
                            </a>
                            <p>
                                Alibaba Clouder - October 28, 2019
                            </p>
                        </li>
                                                <li>
                            <span></span>
                            <a href="/blog/alibaba-unveils-ai-chip-to-enhance-cloud-computing-power_595409">
                                Alibaba Unveils AI Chip to Enhance Cloud Computing Power
                            </a>
                            <p>
                                Alibaba Clouder - September 29, 2019
                            </p>
                        </li>
                                                <li>
                            <span></span>
                            <a href="/blog/alibaba-cloud-ai-tops-dawn-deep-learning-benchmark-dawnbench_596130">
                                Alibaba Cloud AI Tops DAWN Deep Learning Benchmark (DAWNBench)
                            </a>
                            <p>
                                Alibaba Cloud ECS - April 17, 2020
                            </p>
                        </li>
                                                <li>
                            <span></span>
                            <a href="/blog/alibaba-sets-new-record-on-inference-performance-5x-faster-than-nearest-rival_596266">
                                Alibaba Sets New Record on Inference Performance, 5x Faster than Nearest Rival
                            </a>
                            <p>
                                Alibaba Cloud ECS - June 4, 2020
                            </p>
                        </li>
                                            </ul>
                                                            <h3 id="comment">
                        Comments
                    </h3>
                                                            <div class="wrap-main-left-comments">

<span class="hidden" id="pageCount" data-pageCount="0"></span>

</div>
                    <div class="page parent-page"></div>
                    <div class="write-comments">
                        <textarea name="" id="" cols="30" rows="10" placeholder="Write your comment..."></textarea>
                        <div class="write-comments-btn">
                            <button class="btn btn-primary add-parent-comment">Post</button>
                        </div>
                    </div>
                                    </div>
                <div class="wrap-main-iconBox">
                    <a href="javascript:;" class="bg sharer" data-sharer="linkedin" data-url="https://www.alibabacloud.com/blog/announcing-hanguang-800-alibabas-first-ai-inference-chip_595482" title="Announcing Hanguang 800: Alibaba&#039;s First AI-Inference Chip">
                        <i class="icon icon-linkedin1"></i>
                    </a>
                    <a href="javascript:;" class="sharer" data-sharer="facebook" data-url="https://www.alibabacloud.com/blog/announcing-hanguang-800-alibabas-first-ai-inference-chip_595482" title="Announcing Hanguang 800: Alibaba&#039;s First AI-Inference Chip">
                        <i class="icon icon-lianshu1"></i>
                    </a>
                    <a href="javascript:;" class="sharer" data-sharer="twitter" data-url="https://www.alibabacloud.com/blog/announcing-hanguang-800-alibabas-first-ai-inference-chip_595482" title="Announcing Hanguang 800: Alibaba&#039;s First AI-Inference Chip">
                        <i class="icon icon-twitter1"></i>
                    </a>
                                                                                </div>
            </div>
            <div class="wrap-main-right col-md-4">
                <div class="wrap-main-right-user wrap-main-right-user-pc">
                    <dl>
                        <dt>
                            <a href="https://community.alibabacloud.com/users/5040995529404844">
                            <img src="https://yqintl.alicdn.com/img_572d495de1d399a4388a7656634ed8c7.png?x-oss-process=image/resize,m_fixed,h_64,w_64" alt="">
                            </a>
                        </dt>
                        <dd>
                            <h1>
                            <a href="https://community.alibabacloud.com/users/5040995529404844">
                                Alibaba Clouder
                            </a>
                            </h1>
                            <p>
                            2,593 posts | <span class="followers-num">784</span> followers
                            </p>
                                                                                            <a href="#" class="follow-btn" data-islogin="false" data-uid="5040995529404844" data-isfollowed="false" id="follow-btn" rel="nofollow">Follow</a>
                                                                                    </dd>
                    </dl>
                </div>
                                <div class="wrap-main-right-box">
                    <h1>
                         Related Products
                    </h1>
                    <ul>
                                            <li>
                            <h2>
                                                                <a href="https://community.alibabacloud.com/go/1/430">
                                                                    <img src="https://yqintl.alicdn.com/img_cbd4d27e1328d0e09a905d724297644c.png" alt="">
                                    AI Acceleration Solution
                                </a>
                            </h2>
                            <p>
                            Accelerate AI-driven business and AI model training and inference with Alibaba Cloud GPU technology
                            </p>
                                                        <a href="https://community.alibabacloud.com/go/1/430" class="btn btn-default">
                                                             Learn More
                            </a>
                        </li>
                                            <li>
                            <h2>
                                                                <a href="https://community.alibabacloud.com/go/1/472">
                                                                    <img src="https://yqintl.alicdn.com/img_64019d83e954a3adb7de16d47d249d56.png" alt="">
                                    Tongyi Qianwen (Qwen)
                                </a>
                            </h2>
                            <p>
                            Top-performance foundation models from Alibaba Cloud
                            </p>
                                                        <a href="https://community.alibabacloud.com/go/1/472" class="btn btn-default">
                                                             Learn More
                            </a>
                        </li>
                                            <li>
                            <h2>
                                                                <a href="https://community.alibabacloud.com/go/1/334">
                                                                    <img src="https://yqintl.alicdn.com/img_5bd05d4d2cfbe86c4c101a13e0992e8d.png" alt="">
                                    Elastic High Performance Computing Solution
                                </a>
                            </h2>
                            <p>
                            High Performance Computing (HPC) and AI technology helps scientific research institutions to perform viral gene sequencing, conduct new drug research and development, and shorten the research and development cycle.
                            </p>
                                                        <a href="https://community.alibabacloud.com/go/1/334" class="btn btn-default">
                                                             Learn More
                            </a>
                        </li>
                                            <li>
                            <h2>
                                                                <a href="https://community.alibabacloud.com/go/1/463">
                                                                    <img src="https://yqintl.alicdn.com/img_8f1b834802042beeaec861ea3104d970.png" alt="">
                                    Alibaba Cloud for Generative AI
                                </a>
                            </h2>
                            <p>
                            Accelerate innovation with generative AI to create new business success
                            </p>
                                                        <a href="https://community.alibabacloud.com/go/1/463" class="btn btn-default">
                                                             Learn More
                            </a>
                        </li>
                                        </ul>
                </div>
                                                <div class="wrap-main-right-list">
                    <div>
                        <p>
                            <b>
                                 More Posts
                            </b>
                            <span>
                                by Alibaba Clouder
                            </span>
                        </p>
                        <main>
                            <span>
                                 <a href="https://community.alibabacloud.com/users/5040995529404844/article">See All</a>
                            </span>
                            <i class="icon icon-more"></i>
                        </main>
                    </div>
                    <ul>
                                                <li>
                            <a href="/blog/mybatis-with-a-more-fluent-experience_598062">MyBatis with a More Fluent Experience</a>
                        </li>
                                                <li>
                            <a href="/blog/alibaba-cloud-sustainability-report-2021_598055">Alibaba Cloud Sustainability Report 2021</a>
                        </li>
                                                <li>
                            <a href="/blog/comparing-cni-models-in-container-service-for-kubernetes-%E2%80%94-alibaba-cloud-series-part-1_598052">Comparing CNI Models in Container Service for Kubernetes — Alibaba Cloud Series Part 1</a>
                        </li>
                                                <li>
                            <a href="/blog/infographic-5-steps-to-accelerate-your-digitalization-in-asia_598049">[Infographic] 5 Steps to Accelerate Your Digitalization in Asia</a>
                        </li>
                                                <li>
                            <a href="/blog/attackers-use-the-vulnerability-of-showdoc-to-spread-botnets_598047">Attackers Use the Vulnerability of ShowDoc to Spread Botnets</a>
                        </li>
                                                <li>
                            <a href="/blog/powerful-mybatis-and-three-streaming-query-methods_598037">Powerful: MyBatis and Three Streaming Query Methods</a>
                        </li>
                                                <li>
                            <a href="/blog/what-is-the-difference-between-spring-boot-and-spring_598036">What is the Difference between Spring Boot and Spring?</a>
                        </li>
                                                <li>
                            <a href="/blog/what-are-the-differences-and-functions-of-the-redo-log-undo-log-and-binlog-in-mysql_598035">What are the Differences and Functions of the Redo Log, Undo Log, and Binlog in MySQL?</a>
                        </li>
                                                <li>
                            <a href="/blog/on-the-in-depth-cluster-scheduling-and-management_598012">On the In-Depth Cluster Scheduling and Management</a>
                        </li>
                                                <li>
                            <a href="/blog/alibaba-technological-practices-experiences-in-cloud-resource-scheduling_598011">Alibaba Technological Practices: Experiences in Cloud Resource Scheduling</a>
                        </li>
                                            </ul>
                </div>
                            </div>

</div>

</div>

<script type="text/javascript"  nonce="YIEQTN2ZKK">
    window.localconfigs = {
        'aid': 595482
    };
  </script>

<script type="text/javascript"  nonce="YIEQTN2ZKK">
  window.configs = {
      "csrf-param": "yunqi_csrf",
      "csrf-token": "UJAB0ZF69A",
      "islogin": false,
      "registerurl": "https://account.alibabacloud.com/register/register.htm?from_type=yqclub&oauth_callback=https%3A%2F%2Fwww.alibabacloud.com%2Fblog%2Fannouncing-hanguang-800-alibabas-first-ai-inference-chip_595482%3Fdo%3Dlogin",
      "loginurl": "https://account.alibabacloud.com/login/login.htm?from_type=yqclub&oauth_callback=https%3A%2F%2Fwww.alibabacloud.com%2Fblog%2Fannouncing-hanguang-800-alibabas-first-ai-inference-chip_595482%3Fdo%3Dlogin",
      "isNeedNickname": false,
      "baseurl": "/blog"
  };
  </script>

<script src="//g.alicdn.com/aliyun-international/blog-assert/0.0.23/js/detail.js"></script>
  <script src="//g.alicdn.com/aliyun-international/blog-assert/0.0.23/js/nav.js"></script>
  <script type="text/javascript"  nonce="YIEQTN2ZKK">
    (function (i, s, o, g, r, a, m) {
      i['GoogleAnalyticsObject'] = r;
      i[r] = i[r] || function () {
        (i[r].q = i[r].q || []).push(arguments)
      }, i[r].l = 1 * new Date();
      a = s.createElement(o),
        m = s.getElementsByTagName(o)[0];
      a.async = 1;
      a.src = g;
      m.parentNode.insertBefore(a, m)
    })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

ga('create', 'UA-86123020-1', 'auto');
    ga('send', 'pageview');
  </script>
</body>
</html>
