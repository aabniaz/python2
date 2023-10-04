roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

filtered_roll_number = [num for num in roll_number if num in sample_dict.values()]
print("After removing unwanted elements from list", filtered_roll_number)
