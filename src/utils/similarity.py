from difflib import SequenceMatcher

def similarity_score(text1: str, text2: str) -> float:
    return SequenceMatcher(None, text1, text2).ratio()
