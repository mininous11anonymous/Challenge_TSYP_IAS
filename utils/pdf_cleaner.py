import re

def clean_pdf_text(text):
    text = text.replace("\t", " ")
    text = re.sub(r"\s{2,}", " ", text)
    text = text.replace("•", "- ")
    return text.strip()
