import re

def valid(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    num = int(input().strip())
    valid_pairs = []
    for _ in range(num):
        pair = input().strip().split(' ')
        name = pair[0]
        email = pair[1]
        if valid(email):
            valid_pairs.append(f"{name}, {email}")
    for pair in valid_pairs:
        print(pair)
