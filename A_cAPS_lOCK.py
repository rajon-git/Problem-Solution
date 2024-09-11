def caps_lock_convert_titlecase(word):
    if len(word) == 1:
        if word.islower():
            return word.upper()
        else:
            return word.lower()
    elif word.isupper():
        return word.lower()
    elif word[1:].isupper() and word[0].islower():
        return word.capitalize()
    else:
        return word

word = input().strip()
print(caps_lock_convert_titlecase(word))