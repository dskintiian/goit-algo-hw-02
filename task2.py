from collections import deque

def check_palindrome_queue(queue: deque):
    if len(queue) < 2:
        return True

    if queue.pop().casefold() == queue.popleft().casefold():
        return check_palindrome_queue(queue)

    return False


def main():
    palindrome_string = input('Type your text: ').replace(" ", "")

    print('String is a palindrome' if check_palindrome_queue(deque(palindrome_string)) else 'String is not a palindrome')

if __name__ == '__main__':
    main()