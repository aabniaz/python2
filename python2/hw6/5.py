import re

def valid(number):
    pattern = r'^(\+7\s\d{3}\s\d{3}\s\d{2}\s\d{2}|\b87\d{9}|\+7\d{9}\b)$'
    return re.match(pattern, number) is not None

if __name__ == "__main__":
    num_strings = int(input().strip())
    for _ in range(num_strings):
        input_lines = map(str, input().strip().split('\n'))
        for line in input_lines:
            if valid(line):
                print('YES')
            else:
                print('NO')
