def is_pangram(sentence):
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    sentence = sentence.replace(" ", "").lower()
    for letter in alphabets:
        if letter not in sentence:
            return False
    return True
