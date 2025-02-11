#介绍字典知识
#字典重点在于键值对，键值对是一种映射关系，键是唯一的，值可以重复
import matplotlib.pyplot as plt


d1=dict()
d1['name']='Tom' #name是键，Tom是值
print(d1)
#字典是无序的，不能用下标访问，只能用键访问
print('字典的长度就是键值对的个数:',len(d1))
print('age', 'age' in d1)#in操作符只能判断键是否在字典中
v1=d1.values()
print('Tom in Dictionary?', 'Tom' in v1)#values()方法可以判断值是否在字典中
print('键和值的查询是分开的')
print('-----------------')
#通过字典生成一个字母计数器
def check(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]=d[c]+1
    return d

s='hello,world'
#画图表示各个字母出现的次数
d=check(s)
print(d)
print('-----------------')
print(sorted(d.items(), key=lambda x: x[1], reverse=True))  
#各参数的意义：d.items()是将字典转化为元组，key=lambda x: x[1]是按照第二个元素排序，reverse=True是降序
#plt.bar(d.keys(),d.values())
#plt.show()
print('-----------------')
print(d.get('l',0))
print(d.get('z',5))#get()用来查询键对应的值，如果键不存在，返回默认值
print('-----------------')
#遍历字典
for key in d:
    print(key,d[key]) #先键后值
print(sorted(d))#sorted()方法可以对字典的键进行排序
#通过值去查键是不行的，因为值可以重复，一个值可以对应多个键
print('-----------------')
d1={'Name':['Tom'],'Address':'HongKong'}
d1['Name'].append('a')#字典的值可以是列表
print(d1)

a=1
t=[1,2,3]
def f(a):
    a=a+1
    t.append(4)
    b=4
    return b
b=f(a)
print(a)#答案是1，因为函数内部的a是局部变量，不会改变外部的a
print(t)#答案是[1,2,3,4]，因为列表是可变的，函数内部的t和外部的t指向同一个对象
print('-----------------')
#字典合并
d2 = {'Age': 25}
d1.update(d2)
print(d1)  # {'Name': ['Tom', 'Alice'], 'Age': 25}

s = 'hello,world'
d = {c: s.count(c) for c in s if c.isalpha()}
print(d)  # {'h': 1, 'e': 1, 'l': 3, 'o': 1, 'w': 1, 'r': 1, 'd': 1}
#字典推导式，字典推导式是一种快速生成字典的方法
#字典推导式的语法是{key: value for key, value in iterable},isalpha()方法检测字符串是否只由字母组成
print('-----------------')
#以下是相关练习
f=open('PythonFoundation\words.txt')
d=dict()
for line in f:
    word=line.strip()
    if word not in d:
        d[word]=1
    else:
        d[word]=d[word]+1
#print(d)
print('acnes' in d)
print('-----------------')
#setdefault()插入或查询键值，(key,value)如果键不存在，插入键值对，如果键存在，返回值
D1={'Name':'Tom','Age':25}
value=D1.setdefault('Name','Alice')#有Name这个键，返回值Tom
value1=D1.setdefault('Address','HongKong')
print(D1,value,value1)
#删除字典中的键值对
del D1['Name']
print(D1)