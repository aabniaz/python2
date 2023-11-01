str, input_str = map(str, input().split())
middle = len(str) // 2
result = str[:middle] + input_str + str[middle:]
print(result)