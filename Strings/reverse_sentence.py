def reverse_sentence(sentence):
    words = sentence.split()
    reverse = words[::-1]
    rev_sentence = " ".join(reverse)
    return rev_sentence

def reverse_sentence_2(sentence):
    words = sentence.split()
    start = 0
    end = len(words) - 1
    while (start < end):
        words[start], words[end] = words[end], words[start]
        start += 1
        end -= 1
    rev_sentence = " ".join(words)
    return rev_sentence

sentence = "Rohit loves Dogs"
print(reverse_sentence(sentence))