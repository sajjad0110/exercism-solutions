def is_pangram(sentence):
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    sentence = sentence.replace(" ", "").lower()
    for letter in alphabets:
        if letter in sentence:
            continue
        else:
            return False
    return True
