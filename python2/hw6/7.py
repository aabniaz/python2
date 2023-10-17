def valid(card):
    card = card.replace('-', '')
    if not card.isdigit():
        return False
    if len(card) != 16:
        return False
    if card[0] not in ['4', '5', '6']:
        return False
    for i in range(len(card) - 3):
        if card[i] == card[i + 1] == card[i + 2] == card[i + 3]:
            return False
    return True

if __name__ == "__main__":
    num = int(input().strip())
    for _ in range(num):
        card = input().strip()
        if valid(card):
            print('Valid')
        else:
            print('Invalid')
