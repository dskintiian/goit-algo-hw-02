import re

def main():
    input_string = re.sub(r'[^(){}\[\]]', '', input('Type your text: '))
    stack = []
    reversed_map = {'(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{'}

    for element in input_string:
        if len(stack) > 0 and reversed_map[element] == stack[-1]:
            stack.pop()
        else:
            stack.append(element)

    print('String is asymmetrical' if len(stack) > 0 else 'String is symmetrical')

if __name__ == '__main__':
    main()