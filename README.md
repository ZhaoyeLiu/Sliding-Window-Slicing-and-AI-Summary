# Sliding-Window-Slicing-and-AI-Summary
## Project Overview
This project is an intelligent text summarization system based on large language models, specifically designed for automated summarization of long-form content. The system first divides documents into appropriate slices, then applies two different large-model summarization methods to each slice, enabling efficient and accurate summary extraction for various types of documents. It is particularly well-suited for processing formal texts such as government documents, news reports, and academic papers.
## Core Function Implementation Process
### 1.Text Preprocessing and Intelligent Segmentation Process
The system first preprocesses the input text using a sliding-window-based intelligent segmentation algorithm. This algorithm not only considers character length constraints but, more importantly, preserves semantic integrity. The implementation process is as follows:

**Paragraph-level segmentation:** The text is initially segmented by natural paragraphs to maintain logical structure.\n
**Sliding window control:** Fine-grained segmentation is performed based on a predefined window size (e.g., 8,000 characters) and overlap size (e.g., 800 characters).
**Punctuation-aware splitting:** Segmentation occurs at sentence-ending punctuation marks (e.g., period, question mark, exclamation mark) to avoid breaking sentences midway.
**Overlap optimization:** Appropriate overlap starting points are determined to ensure coherence and contextual integrity between segments.

### 2.Multi-strategy Summary Generation Process
The system provides two core summary generation strategies to adapt to different usage scenarios:

#### Iterative Accumulation Strategy:

First generates an initial summary for the first text fragment
Combines the summary of the previous fragment with the content of the next fragment to generate a new cumulative summary
Iteratively processes all fragments in sequence, eventually forming a complete summary
Advantage: Maintains contextual coherence, suitable for long documents with tight logic

#### Fragment Merge Strategy:

Independently processes each text fragment, generating corresponding fragment summaries
Collects all fragment summaries and connects them with specific separators (###)
Calls the large language model for secondary summarization of all fragment summaries
Advantage: High parallel processing efficiency, suitable for loosely structured document collections

### 3.Multi-backend Service Support Process
The system is designed to support multiple large language model service backends:

#### OpenAI Compatible Interface:

Uses standard OpenAI API protocol
Supports local deployment of open-source large models like Qwen
Provides complete conversational interaction interface
Supports parameter adjustment such as temperature control, maximum tokens, etc.

#### Dify Workflow Engine:

Integrates customized workflows of the Dify platform
Supports multi-step complex processing flows
Provides visual process configuration and management
Has better business process customization capabilities

## Technical Architecture and Implementation
### 1.Core Algorithm Technology

**Sliding Window Algorithm:** Implements intelligent text segmentation, balancing segmentation granularity and semantic integrity
**Regular Expression Processing:** Used for string operations such as punctuation recognition and text segmentation
**Recursive Iterative Processing:** Implements progressive construction of summaries in iterative strategies
**Batch Parallel Processing:** Achieves efficient simultaneous processing of multiple fragments in the fragmentation strategy

### 2.Service Integration Technology

**RESTful API Design:** Unified HTTP interface specification supporting JSON data exchange
**Multiplexing Architecture:** Simultaneously supports both OpenAI and Dify service backends
**Asynchronous Processing Mechanism:** Supports batch processing of large-scale texts
**Error Retry Mechanism:** Automatic retry and degradation handling during network exceptions

### 3.Web Service Framework

**Flask Lightweight Framework:** Provides RESTful API service interface
**Request Validation Mechanism:** Completeness and validity verification of input parameters
**Exception Handling System:** Comprehensive error capture and user-friendly prompts
**Cross-platform Deployment:** Supports deployment on multiple platforms including Windows, Linux, etc.

### 4.Configuration and Extension Technology

**Dynamic Parameter Configuration:** Supports runtime adjustment of parameters such as window size and overlap ratio
**Prompt Template:** Configurable system prompts to adapt to summary requirements in different fields
**Modular Design:** Loose coupling of functional modules, facilitating function expansion and maintenance
**Plugin Architecture:** Supports rapid access to new LLM service backends

## Technical Features and Innovations
### 1.Intelligent Text Segmentation
Breaks through the limitations of traditional fixed-length segmentation. Through semantic-aware segmentation algorithms, it ensures information integrity of each segmented fragment while maintaining reading fluency.

### 2.Progressive Summary Optimization
Achieves progressive improvement in summary quality through iterative strategies, with each step optimizing based on previous results, ultimately generating high-quality complete summaries.

### 3.Multi-level Summary Architecture
Supports multi-level processing from fragment-level summaries to document-level summaries, meeting summary requirements at different granularities.

### 4.Service Fault Tolerance and Degradation
Has a complete exception handling mechanism, can automatically switch to backup solutions when some services are unavailable, ensuring system availability.
