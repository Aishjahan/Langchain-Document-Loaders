🧾 LangChain Document Loaders
=============================

This repository demonstrates how to **ingest and parse data from various sources** like text files, PDFs, CSVs, and web pages using LangChain’s **Document Loaders**.

LangChain provides powerful utilities to load unstructured and structured data into its document format so it can be processed, queried, or used for retrieval-based AI pipelines.

🧠 Why Use Document Loaders?
----------------------------

Document loaders are essential for **Retrieval-Augmented Generation (RAG)** and other AI workflows where you need to:

*   Ingest data from various formats
    
*   Normalize them into a unified LangChain document format
    
*   Use them with tools like vector databases, summarizers, or question-answering systems
    

🧰 Loaders Explained
--------------------

### 🟦 CSV Loader (csv\_loader.py)

*   Loads tabular data as documents.
    
*   Converts each row or selected columns into a document chunk.
    
*   Useful for structured datasets like customer info, product specs, logs, etc.
    

### 🟥 PDF Loader (pdf\_loader.py)

*   Extracts text from PDF files.
    
*   Handles multi-page documents.
    
*   Great for loading contracts, reports, and scanned notes (OCR can be added optionally).
    

### 🟨 Text Loader (text\_loader.py)

*   Loads raw .txt files as a single document or splits it into multiple chunks.
    
*   Commonly used for blog posts, notes, or transcripts.
    

### 🟩 Directory Loader (directory\_loader.py)

*   Recursively loads all documents in a folder.
    
*   Can filter by file type and automatically apply the correct loader.
    
*   Ideal for batch processing of datasets.
    

### 🌐 WebBase Loader (webbase\_loader.py)

*   Fetches content from URLs.
    
*   Cleans HTML, strips scripts/ads, and returns raw text content.
    
*   Useful for crawling blogs, FAQs, and documentation sites.
