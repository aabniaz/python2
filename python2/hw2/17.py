datalist = [1452, 11.23, 1+2j, True,'student', (0, -1), [5,12], {"class":'V', "section":'A'}]
datalist_new = []
for x in datalist:
    type_of_element = type(x)
    print(x , "--->",type_of_element)