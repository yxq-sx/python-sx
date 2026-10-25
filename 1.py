# 综合练习：猜数字小游戏（分支 + while循环）
import random

answer = random.randint(1, 20)
print("游戏开始！猜一个1~20之间的数字")

while True:
    guess = int(input("请输入你猜的数字："))
    if guess > answer:
        print("猜大了！")
    elif guess < answer:
        print("猜小了！")
    else:
        print("恭喜你猜对啦！")
        break
