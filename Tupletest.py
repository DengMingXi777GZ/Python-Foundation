#元组是不可变序列，可以使用整数索引，和列表类似

#创建元组
t = (1,2,3,4,5)
print(t[0],type(t))
#如果只有单个元素，需要加逗号
t = 1,#(1,)也可以
print(t[0],type(t))
t=tuple('apple')
print(t)#如果实参是一个序列(字符串、列表或者元组)，结果将是包含序列内元素的一个元组
print('-----------------')
#元组是不可变的，但是元组内部的元素可以是可变的
t1=(1,[1,2,3],4)
print(t1)
t1[1][0]=2
print(t1)
#因为元组是不可变的，您无法改变其中的元素。但是可以使用其他元组替换现有元组：
print(t)
t=('A',)+t[1:]
print(t)
#元组之间可以比较，从第一个元素开始比较，如果相等，继续比较下一个元素
print((1,2,9)<(2,2,4))#True
#两个变量交换值，在元组中非常方便
a=tuple('Apple')
b=tuple('Banana')
a,b=b,a
print(a,b)
#元组解包
a,b,c=t1 #t1=(1, [2, 2, 3], 4)
print(a,b,c)
print('-----------------')
t=(7,3)
res=divmod(*t)#divmod()函数返回一个包含商和余数的元组,*t表示将元组t解包
print(res)
print('-----------------')
#zip()函数将两个序列压缩在一起，返回一个元组的列表,每个元组包含了各个序列中相对位置的一个元素。长度由最短的序列决定
s1='abcde'
s2='123'
print(zip(s1,s2))#zip()函数返回一个zip对象，可以使用list()函数将其转化为列表
print(list(zip(s1,s2)))
for pair in zip(s1,s2):
    print(pair)

for letter,number in zip(s1,s2):
    print(letter,number)
print('-----------------')
#字典与元组
#字典对象有一个内建方法叫做itmes，它返回由多个元组组成的序列，其中每个元组是一个键值对。
d={'a':1,'b':2,'c':3}
print(d.items())
for key,value in d.items():
    print(key,value)
#由zip和dict函数可以将两个序列压缩在一起，创建一个字典
d=dict(zip('abc',range(3)))
print(d)
d.update(zip('def',range(3,6)))#update()方法可以用来合并字典
print(d)
#可以由元组做为字典的键
d=dict()
d['Deng','Ming','Xi']=21
d['Deng','Ming','A']=22
d['Deng','Ming','B']=23
d['Deng','Ming','C']=24
d['Deng','Ming','D']=25
for m1,m2,m3 in d:
    print(m1,m2,m3,d[m1,m2,m3])
print(d)
print('-----------------')
#序列嵌套
#序列可以嵌套，例如列表中可以包含元组，元组中可以包含列表，等等
'''
如果你想使用一个序列作为字典的键，那么你必须使用元组或字符串这样的不可
变类型。
如果你向函数传入一个序列作为参数，那么使用元组以降低由于别名而产生的意
外行为的可能性。
正由于元组的不可变性，它们没有类似sort和reverser这样修改现有列表的方法。然
而Python 提供了内建函数sorted，用于对任意序列排序并输出相同元素的列表，以及
reversed，用于对序列逆向排序并生成一个可以遍历的迭代器。
'''