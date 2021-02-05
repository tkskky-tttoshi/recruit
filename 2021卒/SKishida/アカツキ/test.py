# アカツキ・コーディングテストs
import sys

if __name__ == '__main__':
    lines = list(input().split())

    stack = []
    for value in lines:
        if value != '+' and value != '-' and value != '*' and value != '++' and value != '@':
            stack.append(value)
        elif value == '+' and len(stack) >= 2:
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x + y)
        elif value == '-' and len(stack) >= 2:
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x - y)
        elif value == '*' and len(stack) >= 2:
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x * y)
        elif value == '++' and len(stack) >= 1:
            x = int(stack.pop())
            stack.append(x + 1)
        elif value == '@' and len(stack) >= 3:
            z = int(stack.pop())
            y = int(stack.pop())
            x = int(stack.pop())
            stack.append(x*y + y*z + z*x)
        else:
            print('invalid')
            sys.exit()

    try:
        if len(stack) == 1:
            print(int(stack[0]))
        else:
            print('invalid')
    except ValueError:
        print('invalid')