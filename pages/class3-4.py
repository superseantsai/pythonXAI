import random as r

b = r.randint(1, 100)
while True:
    a = int(input("請輸入一個數字："))
    if a > b:
        print("smaller")
    elif a < b:
        print("bigger")
    else:
        print("correct!")
        break
