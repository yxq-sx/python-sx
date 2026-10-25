# for循环：遍历range、遍历字符串、简单求和
print("==== 1. range基础遍历 ====")
for i in range(1, 6):  # 1,2,3,4,5
    print(f"循环次数：{i}")

print("\n==== 2. 求1~10累加和 ====")
sum_num = 0
for i in range(1, 11):
    sum_num = sum_num + i
print(f"1到10的总和是：{sum_num}")

print("\n==== 3. 遍历字符串 ====")
s = "python"
for char in s:
    print(char)

print("\n==== 4. break跳出循环 ====")
for i in range(1, 10):
    if i == 5:
        break
    print(i)
