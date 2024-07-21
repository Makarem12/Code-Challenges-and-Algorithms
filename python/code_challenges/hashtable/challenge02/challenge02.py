# Write here the code challenge solution
def first_repeated_word(s):
    import re
    words = re.findall(r'\b\w+\b', s)
    seen = set()
    for word in words:
        if word in seen:
            return word
        seen.add(word)
    return "No Repetition"

