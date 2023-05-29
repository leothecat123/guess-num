# 產生一個隨機正式1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 印出 "比答案大/小"

import random

start = input('請決定隨機數字範圍開始值：')
end = input('請決定隨機數字範圍結束值：')
start = int(start)
end = int(end)
# count = count + 1 = count += 1

ans = random.randint(start, end)
count = 0

while True:
    count += 1
    guess = input("請猜範圍內任一數字: ")
    guess = int(guess)
    if guess == ans:
        print("終於猜對了!")
        break
    elif guess > ans:
        print("你的猜測比正確答案大")
    elif guess < ans:
        print("你的猜測比正確答案小")
    print("你已進行了",count,"次猜測")
