import os

#如果该文件已经存在，那么用写入模式打开它将会清空原来的数据并从新开始，所以要小心！如果文件不存在，那么将创建一个新的文件。
#f=open('PythonFoundation/test.txt', 'w')
#如果我只是想增加一些内容到文件中，而不是覆盖原来的内容，那么可以使用追加模式打开文件。
f=open('PythonFoundation/test.txt', 'a')
l1='Hello World\n'
f.write(l1)#write只能写字符串
f.close()
f=open('PythonFoundation/test.txt')#一定要选读取才能读取文件内容
for line in f:
    word=line.strip()
    print(word)
f.close()
print('-----------------')
#格式化
ca=42
ca='%d' % ca #将整数转换为字符串,%d表示第二个运算数应该被格式化为一个十进制整数,%表明格式化运算符
print(ca,type(ca))
ca=42
print('You are %d years old' % ca)#这里的%是格式化运算符，而不是字符串连接符
print('In %d, I have %g gram %s' % (2019, 0.59, 'gold'))#%g表示浮点数，%s表示字符串 格式化对应的数据类型一定要匹配
print('-----------------')

cwd=os.getcwd()#获取当前工作目录
print(cwd)
print(os.path.abspath('PythonFoundation/test.txt'))#返回文件的绝对路径
print(os.path.exists('PythonFoundation/test.txt'))#检查文件是否存在
print(os.path.isdir('PythonFoundation'))#检查是否是目录
print(os.path.isfile('PythonFoundation/test.txt'))#检查是否是文件
print(os.listdir(cwd))#列出目录下所有文件
print('-----------------')
#建立一个把工作空间的文件全部列出来的函数
def walk(workplacename):
    for name in os.listdir(workplacename):
        print(name)
        path=os.path.join(workplacename,name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
#walk(cwd)
print('-----------------')
#可以多点尝试try和except
try:
    f=open('PythonFoundation/test34.txt')
except:
    print('File cannot be opened:',f)
    exit()
#有一种数据库模块dbm，它可以用来创建一个持久的字典，这个字典可以保存在磁盘上，而不是保存在内存中
'''dbm的一个限制在于键和值必须是字符串或者字节。如果你尝试去用其它数据类型，你
会得到一个错误。
pickle 模块可以解决这个问题。它能将几乎所有类型的对象转化为适合在数据库中存储
的字符串，以及将那些字符串还原为原来的对象。shelve 模块提供了一个更高级别的接口，'''
#还有管道shell，可以用来在Python程序中运行外部程序