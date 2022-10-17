def is_palindrome(text):
    
    unwanted_chars = '.,:?! '
    text = list(filter(lambda x: x not in unwanted_chars, text.lower()))

    n = len(text)
    lhs, rhs = None, None
    offset = 1 if n %2 == 0 else 0

    mid = n // 2
    lhs = text[0:mid]
    rhs = text[-1:(mid-offset):-1]
    
    return lhs == rhs

if __name__ == "__main__":

    # expected result: True
    test = ["AB_/BA","ka!???!ak", "KaJAk", "Eine güldne, gute Tugend: Lüge nie!", "Míč omočím.", "Kobyła ma mały bok.", "saippuakivikauppias"]
    for t in test:
        print(t, is_palindrome(t))
