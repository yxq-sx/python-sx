
#  一、常用基础内置函数演示
print("===== 1. 常用内置函数 =====")

# len() 获取长度
lst = [10, 20, 30]
print("len(lst) =", len(lst))

# max() min() 最大最小
print("max(lst) =", max(lst))
print("min(lst) =", min(lst))

# sum() 求和
print("sum(lst) =", sum(lst))

# type() 查看类型
print("type(lst) =", type(lst))

# int() str() float() 类型转换
a = "66"
print("int(a) =", int(a))
print("str(99) =", str(99))

# range() 生成序列
print("range(1,5) 转列表：", list(range(1, 5)))

# enumerate() 带下标遍历
print("\nenumerate遍历：")
for index, value in enumerate(["苹果", "香蕉"]):
    print(index, value)

# zip() 打包，把多个序列一一配对
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
z = zip(list1, list2)
print("zip结果转列表：", list(z))
print("-" * 40)


# 二、序列拆包（* 拆包：列表、元组）
print("===== 2. * 序列拆包（list / tuple） =====")

# 1. 简单变量拆包
t = (10, 20, 30)
x, y, z = t
print("x =", x, "y =", y, "z =", z)

# 2. * 接收多个剩余值（星号变量）
nums = [1, 2, 3, 4, 5]
first, *rest, last = nums
print("first =", first)
print("rest =", rest)
print("last =", last)

# 3. 函数传参时 * 拆包
def show(a, b, c):
    print(f"a={a}, b={b}, c={c}")

data = [100, 200, 300]
show(*data)   # 等价 show(100,200,300)
print("-" * 40)


#三、字典拆包（** 拆包字典）

def student(name, age):
    print(f"姓名：{name}，年龄：{age}")

info = {"name": "小明", "age": 18}
student(**info)  # 等价 student(name="小明", age=18)
print("-" * 40)


#  四、拆包 + zip 内置函数组合（重点）
print("===== 4. zip + 拆包 搭配使用 =====")
l1 = [1, 2]
l2 = ["张三", "李四"]

pack = zip(l1, l2)
# zip打包，* 拆包
unpack = zip(*pack)
print(list(unpack))
print("-" * 40)


# 五、*args 和 **kwargs 接收参数（和拆包对应）
print("===== 5. 函数接收可变参数 *args **kwargs =====")
def test(*args, **kwargs):
    print("args 接收位置参数元组：", args)
    print("kwargs 接收关键字参数字典：", kwargs)

test(1, 2, 3, name="小红", gender="女")

# 先用容器装好，再拆包传入
num_list = [10, 20]
dict_info = {"city": "贵阳", "score": 90}
test(*num_list, **dict_info)
print("-" * 40)


#  六、小易错点总结
print("===== 易错提醒 =====")
# * 只能拆 序列：列表、元组、字符串
# ** 只能拆 字典，只能在函数传参时使用
# 不能单独写 print(**{"a":1}) 会报错
