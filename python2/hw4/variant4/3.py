def candies(isles):
    isle_candies = [0, isles[0], max(isles[0], isles[1])] + [0] * (len(isles) - 2) 
    for i in range(2, len(isles)):
        isle_candies[i] = max(isle_candies[i - 1], isle_candies[i - 2] + isles[i])
    return isle_candies[-1]

num = int(input().strip())

for _ in range(num):
    isles = list(map(int, input().split()))
    max_candies = candies(isles)
    print(max_candies)
