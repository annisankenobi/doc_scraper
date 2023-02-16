import pandas as pd
import os
import html

# this converter reads PDFs with scientific paper layouts (columns)

def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def pdf_to_txt(src_dir, dest_dir):
    from io import StringIO
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfdocument import PDFDocument
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.pdfpage import PDFPage
    from pdfminer.pdfparser import PDFParser

    files = os.listdir(src_dir)
    files = [i for i in files if '.pdf' in i]
    for file in files:
        try:
            with open(src_dir+file, 'rb') as pdf:
                output_string = StringIO()
                parser = PDFParser(pdf)
                doc = PDFDocument(parser)
                rsrcmgr = PDFResourceManager()
                device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
                interpreter = PDFPageInterpreter(rsrcmgr, device)
                for page in PDFPage.create_pages(doc):
                    interpreter.process_page(page)
                save_file(dest_dir+file.replace('.pdf','.txt'), str(output_string.getvalue()))
        except Exception as oops:
            print(oops, file)    

if __name__ == '__main__':
    #convert_docx2txt('docx/', 'converted/')
    pdf_to_txt('PDFs/', 'converted/')

pdf_to_txt('PDFs/', 'converted/')
