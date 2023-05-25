# 產生一個隨機正式1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 印出 "比答案大/小"

import random

ans = random.randint(1, 100)
ans = int(ans)
count = 0
# count = count + 1 = count += 1

while True:
    count += 1
    guess = input("請猜1~100之間的任何一個數字: ")
    guess = int(guess)
    if guess == ans:
        print("終於猜對了!")
        break
    elif guess > ans:
        print("你的猜測比正確答案大")
    elif guess < ans:
        print("你的猜測比正確答案小")
    print("你已進行了",count,"次猜測")
