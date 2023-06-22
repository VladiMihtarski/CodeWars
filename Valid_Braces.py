def valid_braces(string):
    stack = []

    for char in string:
        if char in '([{':
            stack.append(char)  # Добавяме отварящата скоба в стека
        elif char in ')]}':
            if not stack:  # Ако нямаме отваряща скоба в стека
                return False  # Низът е невалиден
            opening_bracket = stack.pop()
            if not is_matching(opening_bracket, char):  # Проверка за съответствие на скобите
                return False  # Низът е невалиден

    if stack:  # Ако имаме непарени скоби в стека
        return False  # Низът е невалиден

    return True  # Низът е валиден


def is_matching(opening, closing):
    # Проверка за съответствие на скобите
    if opening == '(' and closing == ')':
        return True
    elif opening == '[' and closing == ']':
        return True
    elif opening == '{' and closing == '}':
        return True
    else:
        return False


# Примери за използване на функцията и резултати

print(valid_braces("(){}[]"))  # True
print(valid_braces("([{}])"))  # True
print(valid_braces("(}"))  # False
print(valid_braces("[(])"))  # False
print(valid_braces("[({})](]"))  # False
