from functools import reduce
li2=[1,2,3,4]
def add(x,y):
    return x+2*y
res=reduce(add,li2)
print(res)
tua=(1,2,3,4)
print(tua)
print(tua[1])
a,b,c,d=tua
print("a=",a,"b=",b, "c=",c,"d=",d)

# 1. 变量作用域演示
# 全局作用域：函数外部定义的变量
g_num = 100

def test_scope():
    # 局部作用域：函数内部定义，仅函数内可用
    l_num = 20
    print("函数内部，访问全局变量 g_num =", g_num)
    print("函数内部，访问局部变量 l_num =", l_num)

    # global 关键字：声明要修改全局变量
    global g_other
    g_other = 999

test_scope()
# print(l_num)  # 报错！l_num是局部变量，外部无法访问
print("函数外，global新增的全局变量 g_other =", g_other)
print("-" * 50)


    # 2. 嵌套作用域
def outer():
    enclose_var = "外层嵌套变量"
    def inner():
        # nonlocal：修改外层嵌套函数的变量（不是全局）
        nonlocal enclose_var
        enclose_var = "被inner修改后的嵌套变量"
        print("inner读取：", enclose_var)
    inner()
    print("outer读取：", enclose_var)

outer()
print("-" * 50)


# 3. 匿名函数 lambda 基础
# 格式：lambda 参数列表: 返回表达式
# 普通函数写法
def add(a, b):
    return a + b

# 等价lambda匿名函数
add_lambda = lambda a, b: a + b
print("普通函数add(3,5):", add(3,5))
print("lambda add_lambda(3,5):", add_lambda(3,5))
print("-" * 50)


# 4. lambda 的各类参数演示
# 4.1 位置参数
lambda_pos = lambda x, y: x * y
print("位置参数 lambda_pos(4,6):", lambda_pos(4,6))

# 4.2 默认参数
lambda_default = lambda x, y=10: x + y
print("默认参数 lambda_default(5):", lambda_default(5))
print("默认参数 lambda_default(5,20):", lambda_default(5,20))

# 4.3 可变位置参数 *args
lambda_args = lambda *args: sum(args)
print("*args可变参数 lambda_args(1,2,3,4):", lambda_args(1,2,3,4))

# 4.4 可变关键字参数 **kwargs
lambda_kwargs = lambda **kwargs: kwargs
print("**kwargs关键字参数 lambda_kwargs(name='小明',age=18):", lambda_kwargs(name="小明",age=18))

# 4.5 混合参数
lambda_mix = lambda x, y=2, *args, **kwargs: (x + y, args, kwargs)
print("混合参数：", lambda_mix(10, 5, 100, 200, city="贵阳"))
print("-" * 50)


# 5. lambda 常用场景：配合高阶函数 sorted / map / filter
student_list = [("张三", 85), ("李四", 72), ("王五", 91)]
# sorted 的 key 传匿名函数，按分数排序
res_sort = sorted(student_list, key=lambda item: item[1])
print("按分数排序：", res_sort)

# map：对每个元素执行匿名函数
nums = [1,2,3,4]
res_map = list(map(lambda i: i**2, nums))
print("map平方：", res_map)

# filter：过滤，返回条件为True的元素
res_filter = list(filter(lambda i: i % 2 == 0, nums))
print("filter偶数：", res_filter)
print("-" * 50)


#  6. 坑点：lambda延迟绑定（
func_list = []
for i in range(3):
    # 错误写法：lambda捕获i变量，不是捕获当时的值
    func_list.append(lambda: print(i))

f1, f2, f3 = func_list
f1()
f2()
f3()
print("↑ 上面全部输出2，因为调用时i已经变成2")

# 修复方案：给lambda加默认参数，立刻绑定当前值
func_list2 = []
for i in range(3):
    func_list2.append(lambda val=i: print(val))
f_a, f_b, f_c = func_list2
f_a()
f_b()
f_c()
print("↑ 修复后正常输出 0,1,2")

