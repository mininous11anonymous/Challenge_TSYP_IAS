import pypdf

def extract_text_from_pdf(path):
    """Extract all text from a PDF file."""
    reader = pypdf.PdfReader(path)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text
