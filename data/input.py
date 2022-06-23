import PyPDF2

"""
IMPLEMENT ALL INPUT PROCESSORS, PRE AND POST-PROCESSORS HERE
"""


def cleanup_characters(text):
    return text\
        .replace('’', '')\
        .replace('…', '')\
        .replace('—', '')\
        .replace('- ', '')\
        .replace("”", "")


def cleanup_breaklines(text):
    return text.replace('\n', ' ')


def load_pdf(pdf_path, page_start, page_end):
    text = ''
    with open(pdf_path, 'rb') as pdffile:
        pdf_reader = PyPDF2.PdfFileReader(pdffile)
        print('Loaded PDF. Total pages: ' + str(pdf_reader.numPages))
        # Range in the PDF (Usually +2) - Recommended to point to Lore sections, not rules
        for i in range(page_start, page_end):
            page = pdf_reader.getPage(i)
            text += page.extractText() + '\n'
    return text


def load_txt(txt_path):
    with open(txt_path, 'r') as f:
        text = f.read()
    return text
