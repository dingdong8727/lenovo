'''
判断一个数是否是质数prime number
除了1和它本身以外不再有其他的因数的数就是质数。
也就是说，除了1和它本身能被整除的数就是质数。

'''


num = int(input("请输入要查询的数字： "))
i = 2
while i < num:
    s =num % i 
    if s == 0:
        break
    else:
        i = i + 1
if num == i:
    print(f"您输入的数字{num}是质数。")
else:
    print(f"您输入的数字{num}不是质数。")



