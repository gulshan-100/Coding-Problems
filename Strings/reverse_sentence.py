def reverse_sentence(sentence):
    words = sentence.split()
    reverse = words[::-1]
    rev_sentence = " ".join(reverse)
    return rev_sentence

sentence = "Rohit loves Dogs"
print(reverse_sentence(sentence))