def sum_average():
    sum = 0
    count = 0
    while True:
        num = int(input('your numbers: (enter 0 to finish)'))
        if num == 0:
            break
        sum += num
        count += 1
    
    average = sum / count
    print(f"Sum of the numbers: {sum}")        
    print(f"Average of the numbers: {average}")
sum_average()
