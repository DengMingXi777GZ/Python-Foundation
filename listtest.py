#列表是一个有序的集合，可以随时添加和删除其中的元素
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
classmates[0] = 'Adam'
print(classmates)
classmates.append('Jack') #他们都是修改列表，不会产生新的列表
classmates.extend(['Tom','Jerry'])#extend()可以添加多个元素
print(classmates)
#print(classmates[-1])
print('删除末尾元素',classmates.pop(1),classmates)#pop()删除指定位置的元素
classmates.remove('Tom')#remove()删除指定元素
print(classmates)
del classmates[1:3]#del删除指定位置的元素,不包含第二个下标
print('del删除指定位置的元素',classmates)
#列表可以遍历
for name in classmates:
    print(name)
print('-----------------')

#可以搭配+和*操作
L1 = ['Apple', 123, True]
L2 = ['python', 'java']
print(L1 + L2)
print(L2 * 3)
print('-----------------')
#同样可以切片
print(L1[0:2])
print('-----------------')
lt=['s','q','a','b','c']
print(lt)
lt.sort()#无需赋值，直接改变原列表
print(lt)
lt.sort(reverse=True)
print(lt)
print('-----------------')

def only_upper(w):
    res=[]
    for s in w:
        if s.isupper():
            res.append(s)
    return res

s='SsEerwrHJWqdsfhewbbejbewj'
print(only_upper(s))
print('-----------------')
#spilt方法会把字符串按照指定的分隔符进行分割
s='hello world'
print(s.split(' '))#按空格分割
print(s.split('o'))#按o分割
s=s.split(' ')
add=' '
s=add.join(s)#join方法会把列表中的元素按照指定的分隔符进行拼接
print(s)
print('-----------------')
#列表是可变的，字符串是不可变的，注意对象和值的关系，a=[1,2,3],b=[1,2,3]但 (a is b)为False
a=[1,2,3]
b=[1,2,3]
print((a is b))#False
b=a#这样b和a指向同一个对象,深拷贝
#b=a.copy()
#b=a[:]
print(b)
b[0]=0
print(a)
#列表的赋值是引用，一旦有a=b，就是引用，不是赋值,这个非常值得注意
c=[3,42,123,1]
c=sorted(c)
print(c)
print('-----------------')