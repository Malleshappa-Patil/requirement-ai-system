import re

def clean_text(text: str) -> str:
    """
    Basic text cleaning:
    - lowercase
    - remove extra spaces
    """

    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


