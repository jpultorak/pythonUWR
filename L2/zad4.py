from random import seed, sample
# program
seed()
special_ch = ['.', ',', '!', '?', ';', '\\', ':', '|', '\"', '/']

def pick_n(a, n):
    index = [i for i in range(0, len(a))]
    index = sample(index, n)

    return [a[id] for id in sorted(index)]

# count world length excluding some special characters

def word_length (w):
    return sum(1 for letter in w if letter not in special_ch)

def simplyfy_text(text, maxL, maxW):

    a = list(filter(lambda x: len(x) <= maxL, text.split()))
    n = len(a)
    print(a)
    if n <= maxW:
        return(a)
    else:
        return ' '.join(pick_n(a, maxW))
    
if __name__ == "__main__":
    text = '"Podział peryklinalny inicjałów wrzecionowatych \
    kambium charakteryzuje się ścianą podziałową inicjowaną \
    w płaszczyźnie maksymalnej."'

    text2 = 'a.'
    
    print(word_length('a'))
    print(word_length('a.?'))
    print(word_length('a/.?'))
    print(word_length('!kotpłot!'))

    print(simplyfy_text(text, 10, 5))
    print(simplyfy_text(text2, 2, 1))