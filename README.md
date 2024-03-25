# PDF Code Extractor

## Overview
The PDF Code Extractor is a Python tool designed to efficiently scrape coding information from PDF documents. This utility focuses on extracting code blocks that are marked by specific patterns, such as starting with "In [" to denote code lines, from a specified range of pages within a PDF file. It leverages the PyMuPDF library to handle PDF files and applies criteria based on font names and text patterns to distinguish code blocks from regular text or comments.

## Features
- **Selective Extraction**: Capable of identifying and extracting code blocks from a PDF, ensuring that only relevant coding information is retrieved.
- **Comment Handling**: Differentiates between code and comments within the extracted data, formatting comments appropriately to maintain readability and context.
- **Customizable Page Range**: Allows specifying the range of pages to scan, enabling targeted extraction from large documents.

## How It Works
The tool processes each page within the specified range of a PDF document, searching for text blocks that match predefined criteria indicative of code or comments. Code lines are expected to begin with "In [", a convention that helps in their identification. The extraction process also accounts for font styles, with specific fonts being associated with either code or comments. Extracted code blocks and comments are then compiled into a list of strings, each representing a discrete block of code or commentary extracted from the document.

## Usage
To use the PDF Code Extractor, provide the path to your PDF file to the `extract_code_blocks` function. This function will process the document, extract coding information based on the defined criteria, and return a list of code blocks and comments. You can then utilize this list as needed, whether for review, further processing, or integration into other applications.

## Dependencies
- PyMuPDF: Utilized for its robust PDF handling capabilities, enabling the extraction of text from documents with precision.

This tool is an efficient solution for developers, researchers, and educators looking to extract and utilize code blocks from PDF documents without manually sifting through pages of irrelevant content.