

def sort_on(items):
    return items["num"]

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

def sort_scribe(dictionary):
    list =[]
    for char, num in dictionary.items():
        if char.isalpha():
            scribe = {"char": char, "num": num}
            list.append(scribe)
    list.sort(reverse=True, key=sort_on)
    return list
