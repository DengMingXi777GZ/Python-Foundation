print(6^2)#输出4是因为6的二进制是110，2的二进制是010，异或后是100，即4，此处并不是6的平方
print(84/2)#整数相除，结果是浮点数
print(85//2)#双斜杠地板除，结果是整数

#赋值运算符
a = 21
b = 10
c = 0
 
c /= a 
print("c=c/a的值为：", c)
c = 2
c %= a
print("c=c%a的值为：", c) 
c //= a
print("c=c//a的值为：", c)#0//21=0

q=1
w=2
e=3
print(q+w==e)

#逻辑运算符
a=10
b=-20
if a and b:
    print("变量a和b都为true")
else:
    print("变量a和b有一个不为true")

if a or b:
    print("变量a和b至少有一个为true")
else:
    print("变量a和b都不为true")

if not(a and b):
    print("变量a和b都为false")
else:
    print("变量a和b至少有一个为true")
print('-------------------')
#身份运算符
a=20
b=20
if a is b:
    print("a和b有相同的标识")
else:
    print("a和b没有相同的标识")

a=[1,2,3]
b=a
print('a,b是一个身份吗',a is b)
b=a[:]
print(b)
print('改变后a,b是一个身份吗',a is b)
b=[1,2,3]
print('改变后a,b是一个身份吗',a is b)
#为什么列表就不是一个身份了呢
#因为列表是可变对象，a=b是将b指向a的内存地址，a[:]是将b指向a的值，b=[1,2,3]是将b指向一个新的内存地址

print('-------------------')
 
a = 20
b = 10
c = 15
d = 5
e = 0
 
e = (a + b) * c / d       #( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：",  e)
 
e = ((a + b) * c) / d     # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：",  e)
 
e = (a + b) * (c / d);    # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：",  e)
 
e = a + (b * c) / d;      #  20 + (150/5)
print("a + (b * c) / d 运算结果为：",  e)

result = a < b and b < c
print('a<b and b<c的结果是',result)

result = 10 + 2 * 3 ** 2 > 20 and not 5 % 2 == 0
print('10 + 2 * 3 ** 2 > 20 and not 5 % 2 == 0的结果是',result)

a*=b+2
print('a*=b+2的结果是',a)#a=a*(b+2)

def check(x):
    print("Checking:", x)
    return x > 0

result = check(5) and check(-1) and check(3)
print(result)  #and是短路运算，只要有一个为false，后面的就不再执行
print('-------------------')
x=y=1
print(x,y)
c=-3.5
#向上取整
print('向上取整',-(-c//1))
#向下取整
print('向下取整',c//1)

l1='was'
l2='it'
print(l1+l2)

def p(input):
    l=len(input)
    l=70-l
    print(' '*l+input)

p('hello34rrrrrrrr')
print('-------------------')