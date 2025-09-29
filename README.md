# Sliding-Window-Slicing-and-AI-Summary
## Project Overview
This project is an intelligent text summarization system based on large language models, specifically designed for automated summarization of long-form content. The system first divides documents into appropriate slices, then applies two different large-model summarization methods to each slice, enabling efficient and accurate summary extraction for various types of documents. It is particularly well-suited for processing formal texts such as government documents, news reports, and academic papers.
## Core Function Implementation Process
### 1.Text Preprocessing and Intelligent Segmentation Process
The system first preprocesses the input text using a sliding-window-based intelligent segmentation algorithm. This algorithm not only considers character length constraints but, more importantly, preserves semantic integrity. The implementation process is as follows:

Paragraph-level segmentation: The text is initially segmented by natural paragraphs to maintain logical structure.

Sliding window control: Fine-grained segmentation is performed based on a predefined window size (e.g., 8,000 characters) and overlap size (e.g., 800 characters).

Punctuation-aware splitting: Segmentation occurs at sentence-ending punctuation marks (e.g., period, question mark, exclamation mark) to avoid breaking sentences midway.

Overlap optimization: Appropriate overlap starting points are determined to ensure coherence and contextual integrity between segments.

### 2.Multi-strategy Summary Generation Process
The system provides two core summary generation strategies to adapt to different usage scenarios:

**Iterative Accumulation Strategy:**

First generates an initial summary for the first text fragment

Combines the summary of the previous fragment with the content of the next fragment to generate a new cumulative summary

Iteratively processes all fragments in sequence, eventually forming a complete summary

Advantage: Maintains contextual coherence, suitable for long documents with tight logic

**Fragment Merge Strategy:**

Independently processes each text fragment, generating corresponding fragment summaries

Collects all fragment summaries and connects them with specific separators (###)

Calls the large language model for secondary summarization of all fragment summaries

Advantage: High parallel processing efficiency, suitable for loosely structured document collections
