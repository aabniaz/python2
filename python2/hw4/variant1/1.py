"""l1 = 'message' #l1 = input()
l1_new =  []
l2_new = []
for i in range(0, len(l1)):
    if i % 2 == 0:
       l1_new.append(l1[i]) 
    if i % 2 != 0:
        l2_new.append(l1[i]) 
l3 = l1_new + l2_new
for x in l3:
    print(x, end='')"""

def encoder(word: str):
    encoded_word = word[0::2] + word[1::2]
    return encoded_word

def decoder(encoded_word: str):
    md = (len(encoded_word) + 1) // 2
    even_pos = encoded_word[:md]
    odd_pos = encoded_word[md:]
    decoded_word = ""
    for f, g, in zip(even_pos, odd_pos):
        decoded_word += f + g
    if len(even_pos) > len(odd_pos):
        decoded_word += even_pos[-1]
    elif len(even_pos) < len(odd_pos):
        decoded_word += odd_pos[-1]
    return decoded_word

word = input()

encoded = encoder(word)
decoded = decoder(encoded)    
print(encoded)
print(decoded)



