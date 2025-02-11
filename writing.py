import time


print('请输入一个数据：')
#t=input()
#print(t,'类型是:',type(t))#无论你输入什么都是str类型
print("------------------")

t=time.time()
m=t//60
h=t//3600
d=t//(60**2*24)
y=t//(60**2*24*365)
print('当前距离1970年1月1日过去了：',t,'秒')
print('当前距离1970年1月1日过去了：',m,'分钟')
print('当前距离1970年1月1日过去了：',h,'小时')
print('当前距离1970年1月1日过去了：',d,'天')
print('当前距离1970年1月1日过去了：',y,'年')
print("------------------")

def recurse(n, s):
 if n == 0:
    print(s)
 else:
    recurse(n-1, n+s)
print('递归调用')
recurse(3, 0)
#recurse(-1, 0)#会报错，因为无限递归
print("------------------")
#利用逻辑表示式来判断
def campare(x,y,z):
  return x<=y and y<=z

if campare(5,2,3):
  print('1<=2<=3')
else:
    print('1<=2<=3 is False')
print("------------------")
#迭代递归求阶乘
def factorial(n):
  if not isinstance(n,int):
    #isinstance() 函数来判断一个对象是否是一个已知的类型
    print('Factorial is only defined for integers.')
    return None
  elif n<0:
    print('Factorial is not defined for negative integers.')
    return None
  elif n==0:
    return 1
  else:
    return n*factorial(n-1)

print('2.5的阶乘是：',factorial(2.5))
print('-----------------------')

def mysqrt(x):
    if x==0:
        return 0
    a=1
    poch=0
    while True:
        a=(a+x/a)/2
        poch=poch+1
        print('第',poch,'次迭代的值是：',a)
        if abs(a*a-x)<1e-10:
            return a

print('2的平方根是：',mysqrt(2))