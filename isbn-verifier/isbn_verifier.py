def is_valid(isbn):
    i = 10
    aggregate = 0
    isbn = isbn.translate(isbn.maketrans({'-': ''}))
    if len(isbn) != 10 : return False
    for digit in isbn[:9]:
        try:
            aggregate += int(digit) * i
            i -= 1
        except ValueError:
            return False
    last_digit = '10' if isbn[9] == 'X' else isbn[9] 
    try:
        aggregate += int(last_digit)
    except ValueError:
        return False
    if aggregate % 11 == 0: return True
    return False
        
