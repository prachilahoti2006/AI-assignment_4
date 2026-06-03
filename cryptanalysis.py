characters = ['S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y']

digits = list(range(10))

solution = {}

def unique_digits():
    return len(solution.values()) == len(set(solution.values()))

def check_first_digit():
    if solution.get('S') == 0:
        return False
    if solution.get('M') == 0:
        return False
    return True

def make_number(word):
    number = 0
    for ch in word:
        number = number * 10 + solution[ch]
    return number

def check_equation():
    if len(solution) < len(characters):
        return True

    send = make_number("SEND")
    more = make_number("MORE")
    money = make_number("MONEY")

    return send + more == money

def valid_assignment():
    return unique_digits() and check_first_digit() and check_equation()

def get_next_letter():
    for ch in characters:
        if ch not in solution:
            return ch
    return None

def solve():
    if len(solution) == len(characters):
        return check_equation()

    letter = get_next_letter()

    for digit in digits:
        if digit not in solution.values():
            solution[letter] = digit

            if valid_assignment():
                if solve():
                    return True

            solution.pop(letter)

    return False

if solve():
    print("Solution Found:\n")

    for ch in sorted(solution):
        print(ch, "=", solution[ch])

    send = make_number("SEND")
    more = make_number("MORE")
    money = make_number("MONEY")

    print("\nVerification:")
    print(send, "+", more, "=", money)

else:
    print("No solution exists")
