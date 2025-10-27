

def count_words(text):
    count = len(text.split())
    return f"Found {count} total words."

def count_char(text):
    scribe = {}
    lower = text.lower()
    for char in lower:
        if char not in scribe:
            scribe[char] = 1
        else:
            scribe[char] += 1
    return scribe
