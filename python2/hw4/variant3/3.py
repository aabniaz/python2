with open("3_1.txt","r") as first_f:
    f1 = first_f.read()
with open("3_2.txt","r") as second_f:
    f2 = second_f.read()
with open("3_3.txt","w") as third_f:
    for x , y in zip(f1,f2):
        f3 = third_f.write(x+y)
    print(x + y)