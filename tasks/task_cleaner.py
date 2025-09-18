import re

def clean_text(payload: dict) -> dict:
    """ Clean up input text:
        Removing :
            - HTML Tags
            - Special characters
        Converts to lowercase
        Strips whitespace
    """
    raw = payload.get('text', '')
    
    cleaned = raw
    cleaned = re.sub(r"<.*?>", "", cleaned)
    cleaned = re.sub(r"[^a-zA-Z0-9\s]", "", cleaned)
    cleaned = cleaned.lower()
    cleaned = cleaned.strip()
    
    return {
        "original": raw,
        "cleaned": cleaned
    }
