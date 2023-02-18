# Document Scraper
This repository contains a tool to extract text from PDFs. The perk of this tool is that enables layout-aware text extraction from full-text PDF of scientific articles.

## Contents

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#project-description"> ➤ Project Description </a></li>
    <li><a href="#folder-structure"> ➤ Folder Structure</a></li>
    <li><a href="#workflow"> ➤ Workflow</a></li>
    <li><a href="#quickstart"> ➤ Quickstart</a></li>
  </ol>
</details>

## Project Description
This tool adresses the absence of effective means to extract text from scientific PDF files in a layout-aware manner. Utilising pdfminer layout-Aware PDF Text Extractioncan be used for text mining applications.

## Folder Structure

    doc_scraper
    │
    ├── PDFs 
    │   ├── *store all your PDFs here*

    ├── Converted
    │   ├── *where the txt files will be saved*
    │
    ├── robust_converter.py
    │   
    ├── convert_pdfs.py 
    │ 
    ├── README.md 

## Workflow

As shown in the folder structure above, the project contains two key folders:
- **PDFs**: Collection of PDFs
- **Converted**: Where txt files will be stored

In general, you want to create the folders within the Projects area to store files associated with the project.

## QuickStart

1. Place your PDF/s into the PDF folder
2. Install dependencies (pdfminer for layout-aware text extraction, pdfplumber for standard text extraction)
3. Run the app
`python robust_converter.py`

Note: If your PDFs have a basic layout format (no columns of text), you can also use `python convert_pdfs.py`.
For this app you need to install pdfplumber