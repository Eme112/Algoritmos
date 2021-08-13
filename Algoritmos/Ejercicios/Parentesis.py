# Recibes una string conteniendo solo () y []
# Crea un algoritmos para validar que la sintaxis de los corchetes es correcta:
# Ejemplos validos:
# '()'
# '()()()()()()()()()'
# '([])[]()'
# Ejemplos no validos:
# ')'
# '()['
# '(([))]'
# '(((((((((((((((((((((((((((((((((('

def validParentheses(parentheses):
    stack = []
    stack.append(parentheses[0])

    for i in range(1, len(parentheses)):
        if parentheses[i] == '(' or parentheses[i] == '[':
            stack.append(parentheses[i])
        elif parentheses[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif parentheses[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return len(stack) == 0

parentheses = list(input("caso prueba: "))
print(validParentheses(parentheses))