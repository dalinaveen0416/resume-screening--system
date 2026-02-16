import re
from pypdf import PdfReader


def extract_text(file_path: str) -> str:

    try:
        reader = PdfReader(file_path)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return clean_text(text)

    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""


def clean_text(text: str) -> str:
    """
    Cleans extracted text:
    - Removes extra whitespace
    - Normalizes newlines
    - Removes weird characters
    """

    # Remove multiple spaces
    text = re.sub(r"\s+", " ", text)

    # Remove non-printable characters
    text = re.sub(r"[^\x20-\x7E]+", " ", text)

    return text.strip()


def validate_pdf(file_path: str) -> bool:
    """
    Checks if file is a valid PDF.
    """

    try:
        reader = PdfReader(file_path)
        return len(reader.pages) > 0
    except Exception:
        return False
