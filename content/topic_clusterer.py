#!/usr/bin/env python3
"""
Multi-Perspective Summarizer for Atlas

This module implements multi-perspective content summarization capabilities for Atlas,
generating summaries from different viewpoints and angles.
"""

import re
from typing import List, Dict, Any, Optional
from collections import defaultdict, Counter
import math

class MultiPerspectiveSummarizer:
    \"\"\"Multi-perspective content summarizer\"\"\"
    
    def __init__(self):
        \"\"\"Initialize the multi-perspective summarizer\"\"\"
        self.perspectives = {
            'technical': self._technical_perspective,
            'business': self._business_perspective,
            'academic': self._academic_perspective,
            'casual': self._casual_perspective,
            'critical': self._critical_perspective,
            'positive': self._positive_perspective,
            'negative': self._negative_perspective,
            'neutral': self._neutral_perspective
        }
    
    def summarize_multiple_perspectives(self, content: str, 
                                     perspectives: List[str] = None,
                                     summary_length: int = 3) -> Dict[str, str]:
        \"\"\"
        Generate summaries from multiple perspectives
        
        Args:
            content (str): Content to summarize
            perspectives (List[str], optional): Perspectives to use (default: all)
            summary_length (int): Number of sentences in each summary
            
        Returns:
            Dict[str, str]: Summaries by perspective
        \"\"\"
        if perspectives is None:
            perspectives = list(self.perspectives.keys())
        
        summaries = {}
        
        for perspective in perspectives:
            if perspective in self.perspectives:
                try:
                    summary = self.perspectives[perspective](content, summary_length)
                    summaries[perspective] = summary
                except Exception as e:
                    summaries[perspective] = f"Error generating {perspective} summary: {str(e)}"
            else:
                summaries[perspective] = f"Unknown perspective: {perspective}"
        
        return summaries
    
    def _technical_perspective(self, content: str, summary_length: int) -> str:
        \"\"\"
        Generate technical perspective summary
        
        Args:
            content (str): Content to summarize
            summary_length (int): Number of sentences in summary
            
        Returns:
            str: Technical perspective summary
        \"\"\"
        # Extract technical terms and concepts
        technical_terms = self._extract_technical_terms(content)
        
        # Focus on technical aspects
        technical_sentences = []
        sentences = self._split_into_sentences(content)
        
        for sentence in sentences:
            # Check if sentence contains technical terms
            if any(term.lower() in sentence.lower() for term in technical_terms):
                technical_sentences.append(sentence)
        
        # If not enough technical sentences, use all sentences
        if len(technical_sentences) < summary_length:
            technical_sentences = sentences
        
        # Select top sentences based on technical relevance
        scored_sentences = []
        for sentence in technical_sentences:
            score = self._score_technical_relevance(sentence, technical_terms)
            scored_sentences.append((sentence, score))
        
        # Sort by score and select top sentences
        scored_sentences.sort(key=lambda x: x[1], reverse=True)
        selected_sentences = [sentence for sentence, score in scored_sentences[:summary_length]]
        
        # Combine sentences
        summary = ' '.join(selected_sentences)
        
        # Add perspective indicator
        return f"[Technical Perspective] {summary}"
    
    def _business_perspective(self, content: str, summary_length: int) -> str:
        \"\"\"
        Generate business perspective summary
        
        Args:
            content (str): Content to summarize
            summary_length (int): Number of sentences in summary
            
        Returns:
            str: Business perspective summary
        \"\"\"
        # Extract business-related terms
        business_terms = self._extract_business_terms(content)
        
        # Focus on business aspects
        business_sentences = []
        sentences = self._split_into_sentences(content)
        
        for sentence in sentences:
            # Check if sentence contains business terms
            if any(term.lower() in sentence.lower() for term in business_terms):
                business_sentences.append(sentence)
        
        # If not enough business sentences, use all sentences
        if len(business_sentences) < summary_length:
            business_sentences = sentences
        
        # Select top sentences based on business relevance
        scored_sentences = []
        for sentence in business_sentences:
            score = self._score_business_relevance(sentence, business_terms)
            scored_sentences.append((sentence, score))
        
        # Sort by score and select top sentences
        scored_sentences.sort(key=lambda x: x[1], reverse=True)
        selected_sentences = [sentence for sentence, score in scored_sentences[:summary_length]]
        
        # Combine sentences
        summary = ' '.join(selected_sentences)
        
        # Add perspective indicator
        return f"[Business Perspective] {summary}"
    
    def _academic_perspective(self, content: str, summary_length: int) -> str:
        \"\"\"
        Generate academic perspective summary
        
        Args:
            content (str): Content to summarize
            summary_length (int): Number of sentences in summary
            
        Returns:
            str: Academic perspective summary
        \"\"\"
        # Extract academic-related terms
        academic_terms = self._extract_academic_terms(content)
        
        # Focus on academic aspects
        academic_sentences = []
        sentences = self._split_into_sentences(content)
        
        for sentence in sentences:
            # Check if sentence contains academic terms
            if any(term.lower() in sentence.lower() for term in academic_terms):
                academic_sentences.append(sentence)
        
        # If not enough academic sentences, use all sentences
        if len(academic_sentences) < summary_length:
            academic_sentences = sentences
        
        # Select top sentences based on academic relevance
        scored_sentences = []
        for sentence in academic_sentences:
            score = self._score_academic_relevance(sentence, academic_terms)
            scored_sentences.append((sentence, score))
        
        # Sort by score and select top sentences
        scored_sentences.sort(key=lambda x: x[1], reverse=True)
        selected_sentences = [sentence for sentence, score in scored_sentences[:summary_length]]
        
        # Combine sentences
        summary = ' '.join(selected_sentences)
        
        # Add perspective indicator
        return f"[Academic Perspective] {summary}"
    
    def _casual_perspective(self, content: str, summary_length: int) -> str:
        \"\"\"
        Generate casual perspective summary
        
        Args:
            content (str): Content to summarize
            summary_length (int): Number of sentences in summary
            
        Returns:
            str: Casual perspective summary
        \"\"\"
        # Split into sentences
        sentences = self._split_into_sentences(content)
        
        # Select sentences that are easier to understand
        casual_sentences = []
        for sentence in sentences:
            # Check if sentence is relatively simple
            if self._is_casual_sentence(sentence):
                casual_sentences.append(sentence)
        
        # If not enough casual sentences, use all sentences
        if len(casual_sentences) < summary_length:
            casual_sentences = sentences
        
        # Select top sentences based on readability
        scored_sentences = []
        for sentence in casual_sentences:
            score = self._score_readability(sentence)
            scored_sentences.append((sentence, score))
        
        # Sort by readability score and select top sentences
        scored_sentences.sort(key=lambda x: x[1], reverse=True)
        selected_sentences = [sentence for sentence, score in scored_sentences[:summary_length]]
        
        # Combine sentences
        summary = ' '.join(selected_sentences)
        
        # Add perspective indicator
        return f"[Casual Perspective] {summary}"
    
    def _critical_perspective(self, content: str, summary_length: int) -> str:
        \"\"\"
        Generate critical perspective summary
        
        Args:
            content (str): Content to summarize
            summary_length (int): Number of sentences in summary
            
        Returns:
            str: Critical perspective summary
        \"\"\"
        # Extract critical terms
        critical_terms = self._extract_critical_terms(content)
        
        # Focus on critical aspects
        critical_sentences = []
        sentences = self._split_into_sentences(content)
        
        for sentence in sentences:
            # Check if sentence contains critical terms
            if any(term.lower() in sentence.lower() for term in critical_terms):
                critical_sentences.append(sentence)
        
        # If not enough critical sentences, use all sentences
        if len(critical_sentences) < summary_length:
            critical_sentences = sentences
        
        # Select top sentences based on critical relevance
        scored_sentences = []
        for sentence in critical_sentences:
            score = self._score_critical_relevance(sentence, critical_terms)
            scored_sentences.append((sentence, score))
        
        # Sort by score and select top sentences
        scored_sentences.sort(key=lambda x: x[1], reverse=True)
        selected_sentences = [sentence for sentence, score in scored_sentences[:summary_length]]
        
        # Combine sentences
        summary = ' '.join(selected_sentences)
        
        # Add perspective indicator
        return f"[Critical Perspective] {summary}"
    
    def _positive_perspective(self, content: str, summary_length: int) -> str:
        \"\"\"
        Generate positive perspective summary
        
        Args:
            content (str): Content to summarize
            summary_length (int): Number of sentences in summary
            
        Returns:
            str: Positive perspective summary
        \"\"\"
        # Extract positive terms
        positive_terms = self._extract_positive_terms(content)
        
        # Focus on positive aspects
        positive_sentences = []
        sentences = self._split_into_sentences(content)
        
        for sentence in sentences:
            # Check if sentence contains positive terms
            if any(term.lower() in sentence.lower() for term in positive_terms):
                positive_sentences.append(sentence)
        
        # If not enough positive sentences, use all sentences
        if len(positive_sentences) < summary_length:
            positive_sentences = sentences
        
        # Select top sentences based on positive relevance
        scored_sentences = []
        for sentence in positive_sentences:
            score = self._score_positive_relevance(sentence, positive_terms)
            scored_sentences.append((sentence, score))
        
        # Sort by score and select top sentences
        scored_sentences.sort(key=lambda x: x[1], reverse=True)
        selected_sentences = [sentence for sentence, score in scored_sentences[:summary_length]]
        
        # Combine sentences
        summary = ' '.join(selected_sentences)
        
        # Add perspective indicator
        return f"[Positive Perspective] {summary}"
    
    def _negative_perspective(self, content: str, summary_length: int) -> str:
        \"\"\"
        Generate negative perspective summary
        
        Args:
            content (str): Content to summarize
            summary_length (int): Number of sentences in summary
            
        Returns:
            str: Negative perspective summary
        \"\"\"
        # Extract negative terms
        negative_terms = self._extract_negative_terms(content)
        
        # Focus on negative aspects
        negative_sentences = []
        sentences = self._split_into_sentences(content)
        
        for sentence in sentences:
            # Check if sentence contains negative terms
            if any(term.lower() in sentence.lower() for term in negative_terms):
                negative_sentences.append(sentence)
        
        # If not enough negative sentences, use all sentences
        if len(negative_sentences) < summary_length:
            negative_sentences = sentences
        
        # Select top sentences based on negative relevance
        scored_sentences = []
        for sentence in negative_sentences:
            score = self._score_negative_relevance(sentence, negative_terms)
            scored_sentences.append((sentence, score))
        
        # Sort by score and select top sentences
        scored_sentences.sort(key=lambda x: x[1], reverse=True)
        selected_sentences = [sentence for sentence, score in scored_sentences[:summary_length]]
        
        # Combine sentences
        summary = ' '.join(selected_sentences)
        
        # Add perspective indicator
        return f"[Negative Perspective] {summary}"
    
    def _neutral_perspective(self, content: str, summary_length: int) -> str:
        \"\"\"
        Generate neutral perspective summary
        
        Args:
            content (str): Content to summarize
            summary_length (int): Number of sentences in summary
            
        Returns:
            str: Neutral perspective summary
        \"\"\"
        # Split into sentences
        sentences = self._split_into_sentences(content)
        
        # Select sentences that are neutral in tone
        neutral_sentences = []
        for sentence in sentences:
            # Check if sentence is neutral
            if self._is_neutral_sentence(sentence):
                neutral_sentences.append(sentence)
        
        # If not enough neutral sentences, use all sentences
        if len(neutral_sentences) < summary_length:
            neutral_sentences = sentences
        
        # Select top sentences based on neutrality
        scored_sentences = []
        for sentence in neutral_sentences:
            score = self._score_neutrality(sentence)
            scored_sentences.append((sentence, score))
        
        # Sort by neutrality score and select top sentences
        scored_sentences.sort(key=lambda x: x[1], reverse=True)
        selected_sentences = [sentence for sentence, score in scored_sentences[:summary_length]]
        
        # Combine sentences
        summary = ' '.join(selected_sentences)
        
        # Add perspective indicator
        return f"[Neutral Perspective] {summary}"
    
    def _split_into_sentences(self, content: str) -> List[str]:
        \"\"\"
        Split content into sentences
        
        Args:
            content (str): Content to split
            
        Returns:
            List[str]: List of sentences
        \"\"\"
        # Simple sentence splitting (in a real implementation, use NLTK or similar)
        sentences = re.split(r'[.!?]+', content)
        sentences = [s.strip() for s in sentences if s.strip()]
        return sentences
    
    def _extract_technical_terms(self, content: str) -> List[str]:
        \"\"\"
        Extract technical terms from content
        
        Args:
            content (str): Content to analyze
            
        Returns:
            List[str]: Extracted technical terms
        \"\"\"
        # Common technical terms
        technical_terms = [
            'python', 'javascript', 'java', 'go', 'rust', 'c++', 'c#',
            'react', 'vue', 'angular', 'django', 'flask', 'express',
            'docker', 'kubernetes', 'aws', 'gcp', 'azure',
            'postgresql', 'mongodb', 'redis', 'mysql',
            'tensorflow', 'pytorch', 'scikit-learn', 'machine learning',
            'api', 'database', 'framework', 'library', 'package',
            'algorithm', 'data structure', 'authentication', 'security',
            'encryption', 'hashing', 'cryptography', 'ssl', 'tls',
            'http', 'https', 'rest', 'graphql', 'websocket',
            'git', 'github', 'ci/cd', 'devops', 'agile',
            'oop', 'functional programming', 'design patterns',
            'testing', 'unit testing', 'integration testing', 'tdd',
            'microservices', 'serverless', 'cloud computing',
            'big data', 'data science', 'artificial intelligence',
            'natural language processing', 'computer vision',
            'blockchain', 'cryptocurrency', 'smart contracts',
            'iot', 'internet of things', 'embedded systems',
            'mobile development', 'web development', 'frontend', 'backend',
            'fullstack', 'responsive design', 'ux/ui',
            'cybersecurity', 'penetration testing', 'vulnerability assessment',
            'compliance', 'gdpr', 'hipaa', 'sox',
            'performance optimization', 'scalability', 'reliability',
            'monitoring', 'logging', 'observability',
            'debugging', 'profiling', 'troubleshooting'
        ]
        
        # Find terms in content
        content_lower = content.lower()
        found_terms = [term for term in technical_terms if term in content_lower]
        
        return list(set(found_terms))  # Remove duplicates
    
    def _extract_business_terms(self, content: str) -> List[str]:
        \"\"\"
        Extract business terms from content
        
        Args:
            content (str): Content to analyze
            
        Returns:
            List[str]: Extracted business terms
        \"\"\"
        # Common business terms
        business_terms = [
            'business', 'company', 'corporation', 'enterprise', 'startup',
            'revenue', 'profit', 'loss', 'income', 'expense',
            'market', 'marketing', 'sales', 'customer', 'client',
            'product', 'service', 'solution', 'strategy', 'tactic',
            'competition', 'competitive', 'advantage', 'differentiation',
            'growth', 'expansion', 'scaling', 'scale', 'roi', 'return on investment',
            'cost', 'budget', 'investment', 'funding', 'capital',
            'team', 'employee', 'staff', 'workforce', 'talent',
            'leadership', 'management', 'executive', 'director',
            'stakeholder', 'shareholder', 'investor', 'partner',
            'partnership', 'collaboration', 'cooperation', 'alliance',
            'brand', 'branding', 'identity', 'reputation', 'image',
            'customer service', 'support', 'experience', 'ux',
            'innovation', 'innovative', 'creative', 'creativity',
            'efficiency', 'effectiveness', 'productivity', 'performance',
            'quality', 'excellence', 'standard', 'benchmark',
            'risk', 'opportunity', 'challenge', 'problem', 'solution',
            'goal', 'objective', 'target', 'kpi', 'metric',
            'process', 'procedure', 'workflow', 'methodology',
            'culture', 'values', 'ethics', 'integrity', 'transparency'
        ]
        
        # Find terms in content
        content_lower = content.lower()
        found_terms = [term for term in business_terms if term in content_lower]
        
        return list(set(found_terms))  # Remove duplicates
    
    def _extract_academic_terms(self, content: str) -> List[str]:
        \"\"\"
        Extract academic terms from content
        
        Args:
            content (str): Content to analyze
            
        Returns:
            List[str]: Extracted academic terms
        \"\"\"
        # Common academic terms
        academic_terms = [
            'research', 'study', 'experiment', 'analysis', 'evaluation',
            'theory', 'hypothesis', 'methodology', 'approach', 'framework',
            'literature', 'review', 'survey', 'synthesis', 'meta-analysis',
            'data', 'dataset', 'sample', 'population', 'variable',
            'statistic', 'statistical', 'quantitative', 'qualitative',
            'correlation', 'causation', 'regression', 'significance',
            'hypothesis testing', 'p-value', 'confidence interval',
            'publication', 'journal', 'conference', 'proceedings',
            'citation', 'reference', 'bibliography', 'scholarship',
            'peer review', 'academic rigor', 'scientific method',
            'empirical', 'evidence-based', 'theoretical', 'practical',
            'interdisciplinary', 'multidisciplinary', 'transdisciplinary',
            'collaboration', 'collaborative', 'cooperation',
            'innovation', 'novelty', 'originality', 'contribution',
            'implication', 'application', 'implementation',
            'limitation', 'constraint', 'boundary condition',
            'future work', 'recommendation', 'suggestion',
            'conclusion', 'finding', 'result', 'outcome',
            'discussion', 'interpretation', 'explanation',
            'validation', 'verification', 'replication',
            'reliability', 'validity', 'credibility', 'trustworthiness',
            'ethics', 'ethical', 'integrity', 'transparency'
        ]
        
        # Find terms in content
        content_lower = content.lower()
        found_terms = [term for term in academic_terms if term in content_lower]
        
        return list(set(found_terms))  # Remove duplicates
    
    def _extract_critical_terms(self, content: str) -> List[str]:
        \"\"\"
        Extract critical terms from content
        
        Args:
            content (str): Content to analyze
            
        Returns:
            List[str]: Extracted critical terms
        \"\"\"
        # Common critical terms
        critical_terms = [
            'problem', 'issue', 'challenge', 'difficulty', 'obstacle',
            'limitation', 'constraint', 'restriction', 'barrier',
            'weakness', 'flaw', 'defect', 'bug', 'error',
            'failure', 'mistake', 'shortcoming', 'drawback',
            'criticism', 'critique', 'criticize', 'question',
            'concern', 'worry', 'anxiety', 'fear', 'risk',
            'threat', 'danger', 'hazard', 'vulnerability',
            'disadvantage', 'downside', 'pitfall', 'trap',
            'complication', 'complexity', 'difficulty', 'trouble',
            'conflict', 'dispute', 'controversy', 'debate',
            'objection', 'opposition', 'resistance', 'rejection',
            'critique', 'analysis', 'evaluation', 'assessment',
            'scrutiny', 'inspection', 'examination', 'investigation',
            'skepticism', 'doubt', 'uncertainty', 'ambiguity',
            'inconsistency', 'contradiction', 'paradox', 'dilemma',
            'fallacy', 'logical error', 'reasoning flaw',
            'bias', 'prejudice', 'discrimination', 'stereotype',
            'inequality', 'injustice', 'unfairness', 'discrimination',
            'exploitation', 'abuse', 'misuse', 'violation',
            'violation', 'breach', 'infringement', 'trespass'
        ]
        
        # Find terms in content
        content_lower = content.lower()
        found_terms = [term for term in critical_terms if term in content_lower]
        
        return list(set(found_terms))  # Remove duplicates
    
    def _extract_positive_terms(self, content: str) -> List[str]:
        \"\"\"
        Extract positive terms from content
        
        Args:
            content (str): Content to analyze
            
        Returns:
            List[str]: Extracted positive terms
        \"\"\"
        # Common positive terms
        positive_terms = [
            'benefit', 'advantage', 'gain', 'improvement', 'enhancement',
            'success', 'achievement', 'accomplishment', 'milestone',
            'opportunity', 'chance', 'possibility', 'potential',
            'strength', 'asset', 'resource', 'capability', 'capacity',
            'excellence', 'quality', 'standard', 'benchmark',
            'innovation', 'innovative', 'creative', 'creativity',
            'efficiency', 'effectiveness', 'productivity', 'performance',
            'growth', 'expansion', 'scaling', 'scale',
            'profit', 'revenue', 'income', 'return on investment',
            'satisfaction', 'happiness', 'joy', 'pleasure', 'delight',
            'praise', 'commendation', 'recognition', 'award',
            'popularity', 'trend', 'fad', 'vogue', 'fashion',
            'preference', 'favor', 'liking', 'affinity',
            'trust', 'confidence', 'faith', 'belief', 'conviction',
            'loyalty', 'commitment', 'dedication', 'devotion',
            'collaboration', 'cooperation', 'partnership', 'alliance',
            'community', 'network', 'connection', 'relationship',
            'support', 'assistance', 'help', 'aid', 'guidance',
            'mentor', 'teacher', 'coach', 'trainer', 'instructor',
            'learning', 'education', 'knowledge', 'understanding',
            'wisdom', 'insight', 'awareness', 'consciousness'
        ]
        
        # Find terms in content
        content_lower = content.lower()
        found_terms = [term for term in positive_terms if term in content_lower]
        
        return list(set(found_terms))  # Remove duplicates
    
    def _extract_negative_terms(self, content: str) -> List[str]:
        \"\"\"
        Extract negative terms from content
        
        Args:
            content (str): Content to analyze
            
        Returns:
            List[str]: Extracted negative terms
        \"\"\"
        # Common negative terms
        negative_terms = [
            'problem', 'issue', 'challenge', 'difficulty', 'obstacle',
            'limitation', 'constraint', 'restriction', 'barrier',
            'weakness', 'flaw', 'defect', 'bug', 'error',
            'failure', 'mistake', 'shortcoming', 'drawback',
            'criticism', 'critique', 'criticize', 'question',
            'concern', 'worry', 'anxiety', 'fear', 'risk',
            'threat', 'danger', 'hazard', 'vulnerability',
            'disadvantage', 'downside', 'pitfall', 'trap',
            'complication', 'complexity', 'difficulty', 'trouble',
            'conflict', 'dispute', 'controversy', 'debate',
            'objection', 'opposition', 'resistance', 'rejection',
            'damage', 'harm', 'injury', 'loss', 'destruction',
            'decline', 'decrease', 'reduction', 'drop',
            'skepticism', 'doubt', 'uncertainty', 'ambiguity',
            'inconsistency', 'contradiction', 'paradox', 'dilemma',
            'fallacy', 'logical error', 'reasoning flaw',
            'bias', 'prejudice', 'discrimination', 'stereotype',
            'inequality', 'injustice', 'unfairness', 'discrimination',
            'exploitation', 'abuse', 'misuse', 'violation',
            'violation', 'breach', 'infringement', 'trespass'
        ]
        
        # Find terms in content
        content_lower = content.lower()
        found_terms = [term for term in negative_terms if term in content_lower]
        
        return list(set(found_terms))  # Remove duplicates
    
    def _score_technical_relevance(self, sentence: str, technical_terms: List[str]) -> float:
        \"\"\"
        Score sentence based on technical relevance
        
        Args:
            sentence (str): Sentence to score
            technical_terms (List[str]): Technical terms
            
        Returns:
            float: Technical relevance score
        \"\"\"
        sentence_lower = sentence.lower()
        score = 0
        
        for term in technical_terms:
            if term.lower() in sentence_lower:
                score += 1
        
        # Normalize by sentence length
        words = re.findall(r'\b\w+\b', sentence)
        if len(words) > 0:
            score /= len(words)
        
        return score
    
    def _score_business_relevance(self, sentence: str, business_terms: List[str]) -> float:
        \"\"\"
        Score sentence based on business relevance
        
        Args:
            sentence (str): Sentence to score
            business_terms (List[str]): Business terms
            
        Returns:
            float: Business relevance score
        \"\"\"
        sentence_lower = sentence.lower()
        score = 0
        
        for term in business_terms:
            if term.lower() in sentence_lower:
                score += 1
        
        # Normalize by sentence length
        words = re.findall(r'\b\w+\b', sentence)
        if len(words) > 0:
            score /= len(words)
        
        return score
    
    def _score_academic_relevance(self, sentence: str, academic_terms: List[str]) -> float:
        \"\"\"
        Score sentence based on academic relevance
        
        Args:
            sentence (str): Sentence to score
            academic_terms (List[str]): Academic terms
            
        Returns:
            float: Academic relevance score
        \"\"\"
        sentence_lower = sentence.lower()
        score = 0
        
        for term in academic_terms:
            if term.lower() in sentence_lower:
                score += 1
        
        # Normalize by sentence length
        words = re.findall(r'\b\w+\b', sentence)
        if len(words) > 0:
            score /= len(words)
        
        return score
    
    def _is_casual_sentence(self, sentence: str) -> bool:
        \"\"\"
        Check if sentence is casual/simple
        
        Args:
            sentence (str): Sentence to check
            
        Returns:
            bool: True if casual/simple
        \"\"\"
        # Check sentence length
        words = re.findall(r'\b\w+\b', sentence)
        if len(words) > 20:  # Too long
            return False
        
        # Check for complex vocabulary
        complex_words = [
            'comprehensive', 'comprehensively', 'comprehensiveness',
            'implementation', 'implementing', 'implemented',
            'configuration', 'configuring', 'configured',
            'consideration', 'considering', 'considered',
            'characterization', 'characterizing', 'characterized',
            'differentiation', 'differentiating', 'differentiated',
            'identification', 'identifying', 'identified',
            'implementation', 'implementing', 'implemented',
            'investigation', 'investigating', 'investigated',
            'organization', 'organizing', 'organized',
            'presentation', 'presenting', 'presented',
            'representation', 'representing', 'represented',
            'significance', 'significant', 'significantly',
            'specification', 'specifying', 'specified',
            'utilization', 'utilizing', 'utilized'
        ]
        
        sentence_lower = sentence.lower()
        for word in complex_words:
            if word in sentence_lower:
                return False  # Contains complex vocabulary
        
        return True  # Seems casual/simple
    
    def _score_readability(self, sentence: str) -> float:
        \"\"\"
        Score sentence based on readability
        
        Args:
            sentence (str): Sentence to score
            
        Returns:
            float: Readability score
        \"\"\"
        words = re.findall(r'\b\w+\b', sentence)
        if not words:
            return 0.0
        
        # Calculate average word length
        avg_word_length = sum(len(word) for word in words) / len(words)
        
        # Calculate sentence length
        sentence_length = len(words)
        
        # Score based on simplicity (shorter words and sentences = higher readability)
        word_score = max(0.0, 1.0 - (avg_word_length - 5) / 10)  # Prefer words around 5 chars
        length_score = max(0.0, 1.0 - (sentence_length - 10) / 20)  # Prefer sentences around 10 words
        
        return (word_score + length_score) / 2
    
    def _score_critical_relevance(self, sentence: str, critical_terms: List[str]) -> float:
        \"\"\"
        Score sentence based on critical relevance
        
        Args:
            sentence (str): Sentence to score
            critical_terms (List[str]): Critical terms
            
        Returns:
            float: Critical relevance score
        \"\"\"
        sentence_lower = sentence.lower()
        score = 0
        
        for term in critical_terms:
            if term.lower() in sentence_lower:
                score += 1
        
        # Normalize by sentence length
        words = re.findall(r'\b\w+\b', sentence)
        if len(words) > 0:
            score /= len(words)
        
        return score
    
    def _score_positive_relevance(self, sentence: str, positive_terms: List[str]) -> float:
        \"\"\"
        Score sentence based on positive relevance
        
        Args:
            sentence (str): Sentence to score
            positive_terms (List[str]): Positive terms
            
        Returns:
            float: Positive relevance score
        \"\"\"
        sentence_lower = sentence.lower()
        score = 0
        
        for term in positive_terms:
            if term.lower() in sentence_lower:
                score += 1
        
        # Normalize by sentence length
        words = re.findall(r'\b\w+\b', sentence)
        if len(words) > 0:
            score /= len(words)
        
        return score
    
    def _score_negative_relevance(self, sentence: str, negative_terms: List[str]) -> float:
        \"\"\"
        Score sentence based on negative relevance
        
        Args:
            sentence (str): Sentence to score
            negative_terms (List[str]): Negative terms
            
        Returns:
            float: Negative relevance score
        \"\"\"
        sentence_lower = sentence.lower()
        score = 0
        
        for term in negative_terms:
            if term.lower() in sentence_lower:
                score += 1
        
        # Normalize by sentence length
        words = re.findall(r'\b\w+\b', sentence)
        if len(words) > 0:
            score /= len(words)
        
        return score
    
    def _is_neutral_sentence(self, sentence: str) -> bool:
        \"\"\"
        Check if sentence is neutral in tone
        
        Args:
            sentence (str): Sentence to check
            
        Returns:
            bool: True if neutral
        \"\"\"
        sentence_lower = sentence.lower()
        
        # Check for positive and negative terms
        positive_terms = self._extract_positive_terms(sentence)
        negative_terms = self._extract_negative_terms(sentence)
        
        # If roughly equal positive and negative terms, it's likely neutral
        if len(positive_terms) == 0 and len(negative_terms) == 0:
            return True  # No emotional terms
        
        # If difference is small, it's likely neutral
        if abs(len(positive_terms) - len(negative_terms)) <= 1:
            return True
        
        return False
    
    def _score_neutrality(self, sentence: str) -> float:
        \"\"\"
        Score sentence based on neutrality
        
        Args:
            sentence (str): Sentence to score
            
        Returns:
            float: Neutrality score
        \"\"\"
        sentence_lower = sentence.lower()
        
        # Extract positive and negative terms
        positive_terms = self._extract_positive_terms(sentence)
        negative_terms = self._extract_negative_terms(sentence)
        
        # Calculate neutrality score
        total_emotional_terms = len(positive_terms) + len(negative_terms)
        
        if total_emotional_terms == 0:
            return 1.0  # Completely neutral
        
        # Score based on balance of positive and negative terms
        difference = abs(len(positive_terms) - len(negative_terms))
        balance_score = 1.0 - (difference / total_emotional_terms)
        
        return max(0.0, balance_score)
    
    def _calculate_centroid(self, documents: List[Dict]) -> Dict[str, float]:
        \"\"\"
        Calculate centroid of a cluster of documents
        
        Args:
            documents (List[Dict]): List of documents in cluster
            
        Returns:
            Dict[str, float]: Centroid TF-IDF vector
        \"\"\"
        if not documents:
            return {}
        
        # Sum all TF-IDF vectors
        centroid = defaultdict(float)
        term_counts = defaultdict(int)
        
        for doc in documents:
            for term, score in doc['tfidf'].items():
                centroid[term] += score
                term_counts[term] += 1
        
        # Average the scores
        for term in centroid:
            centroid[term] /= len(documents)
        
        return dict(centroid)
    
    def _extract_cluster_keywords(self, documents: List[Dict]) -> List[str]:
        \"\"\"
        Extract keywords representing a cluster
        
        Args:
            documents (List[Dict]): List of documents in cluster
            
        Returns:
            List[str]: Cluster keywords
        \"\"\"
        # Combine all terms from cluster documents
        all_terms = defaultdict(float)
        
        for doc in documents:
            for term, score in doc['tfidf'].items():
                all_terms[term] += score
        
        # Get top terms
        sorted_terms = sorted(all_terms.items(), key=lambda x: x[1], reverse=True)
        keywords = [term for term, score in sorted_terms[:10]]
        
        return keywords
    
    def get_clusters(self) -> List[Dict]:
        \"\"\"
        Get current clusters
        
        Returns:
            List[Dict]: List of clusters
        \"\"\"
        return self.clusters
    
    def get_document_cluster(self, doc_id: str) -> Optional[Dict]:
        \"\"\"
        Get cluster for a specific document
        
        Args:
            doc_id (str): Document ID
            
        Returns:
            Optional[Dict]: Document cluster or None if not found
        \"\"\"
        for cluster in self.clusters:
            if doc_id in cluster['documents']:
                return cluster
        
        return None
    
    def get_cluster_statistics(self) -> Dict[str, Any]:
        \"\"\"
        Get clustering statistics
        
        Returns:
            Dict[str, Any]: Clustering statistics
        \"\"\"
        if not self.clusters:
            return {}
        
        cluster_sizes = [len(cluster['documents']) for cluster in self.clusters]
        
        return {
            'total_documents': len(self.documents),
            'total_clusters': len(self.clusters),
            'avg_cluster_size': sum(cluster_sizes) / len(cluster_sizes),
            'min_cluster_size': min(cluster_sizes),
            'max_cluster_size': max(cluster_sizes),
            'single_doc_clusters': len([c for c in cluster_sizes if c == 1]),
            'multi_doc_clusters': len([c for c in cluster_sizes if c > 1])
        }

def main():
    \"\"\"Example usage of TopicClusterer\"\"\"
    # Create clusterer
    clusterer = TopicClusterer()
    
    # Sample documents
    documents = [
        {
            'id': 'doc1',
            'content': 'Python is a high-level programming language with dynamic semantics. It is used for web development, data science, and automation. Python has a simple syntax similar to English, making it easy to learn. The language supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python has a large standard library and a vibrant community that contributes to thousands of third-party modules and packages. Popular frameworks like Django and Flask make web development with Python straightforward. For data science, libraries like NumPy, Pandas, and Matplotlib provide powerful tools for analysis and visualization. Machine learning practitioners use Python with libraries like TensorFlow, PyTorch, and Scikit-learn. Python is also popular for automation tasks, scripting, and rapid prototyping. The language continues to evolve with regular updates and improvements to performance and features.'
        },
        {
            'id': 'doc2',
            'content': 'Machine learning is a subset of artificial intelligence that provides systems the ability to automatically learn and improve from experience. It focuses on the development of computer programs that can access data and use it to learn for themselves. The process of learning begins with observations or data, such as examples, direct experience, or instruction, in order to look for patterns in data and make better decisions in the future based on the examples that we provide. The primary aim is to allow the computers learn automatically without human intervention or assistance and adjust actions accordingly.'
        },
        {
            'id': 'doc3',
            'content': 'Data science combines statistics, mathematics, and computer science to extract insights from data. It involves data cleaning, data analysis, and data visualization. Popular tools include Python and R. Data scientists use statistical methods to analyze large datasets and identify patterns. They create predictive models to forecast future trends. Data visualization helps communicate findings to stakeholders. The field requires skills in programming, statistics, and domain knowledge. Popular libraries include NumPy, Pandas, Matplotlib, and Scikit-learn. Career opportunities in data science are growing rapidly.'
        },
        {
            'id': 'doc4',
            'content': 'Web development involves creating websites and web applications. Frontend development focuses on user interfaces using HTML, CSS, and JavaScript. Backend development handles server-side logic using languages like Python, Java, or Node.js. Popular frameworks include Django and Flask for Python. Responsive design ensures websites work on all devices. Security is crucial for protecting user data. Performance optimization improves loading times. Testing ensures quality and reliability. Version control with Git helps track changes. Deployment involves putting applications on servers for public access.'
        },
        {
            'id': 'doc5',
            'content': 'Artificial intelligence is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. Colloquially, the term "artificial intelligence" is often used to describe machines that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving". As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect. A quip in Tesler\'s Theorem says "AI is whatever hasn\'t been done yet."'
        }
    ]
    
    # Add documents
    clusterer.add_documents(documents)
    
    # Perform clustering
    clusters = clusterer.cluster_documents()
    
    # Display results
    print("\nClustering Results:")
    for cluster in clusters:
        print(f"\nCluster {cluster['id']}:")
        print(f"  Documents: {cluster['documents']}")
        print(f"  Keywords: {', '.join(cluster['keywords'])}")
    
    # Get statistics
    stats = clusterer.get_cluster_statistics()
    print(f"\nClustering Statistics:")
    print(f"  Total Documents: {stats['total_documents']}")
    print(f"  Total Clusters: {stats['total_clusters']}")
    print(f"  Average Cluster Size: {stats['avg_cluster_size']:.2f}")
    print(f"  Min Cluster Size: {stats['min_cluster_size']}")
    print(f"  Max Cluster Size: {stats['max_cluster_size']}")
    print(f"  Single Doc Clusters: {stats['single_doc_clusters']}")
    print(f"  Multi Doc Clusters: {stats['multi_doc_clusters']}")

if __name__ == "__main__":
    main()