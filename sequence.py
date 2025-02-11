#字符串str 有序不可变序列
fruit='banana'
print('fruit[0]:',fruit[0])
print('fruit[-1]:',fruit[-1])
print('fruit的长度是:',len(fruit))

#遍历字符串
print('for循环遍历')
for index in fruit:
    print(index)
print('while循环遍历')
index=0
while index<len(fruit):
    print(fruit[index])
    index+=1
print('------------------')
print('字符串遍历与拼接')
D1="ABCDEFG" 
D2='ack'
for i,letter in enumerate(D1):
    if i==3 or i==6:
        print(letter+'u'+D2)
    else:
        print(letter+D2)
print('------------------')
#字符串切片
s='Monty Python'
print('s[:5]:',s[:5])
print('s[6:12]:',s[6:12])
#字符串是不可变的，只能重新赋值
s1='Hello,HongKong'
print('s1:',s1)
s2='NiHao'
s=s2+s1[5:]
print('s:',s)
print('-------------')
def search(word,letter,start):
    index=0
    for idx,l in enumerate(word[start:]):
        if l==letter:
            print('idx',idx)

word='rqwertyuio'
letter='r'
search(word,letter,2)
print('------------')
#大写函数
t='hello,world,world'
t=t.upper()
print(t)
print('----------')
#搜索函数find
w='WORLD'
index=t.find(w,3,19)
print('index',index)
#大小写比较
str1 = "apple"
str2 = "banana"
if str1 < str2:
    print(f'"{str1}" 在 "{str2}" 之前')
else:
    print(f'"{str1}" 在 "{str2}" 之后')
'''字符串比较的规则逐个字符比较：字符串比较是基于字符的 Unicode 编码值进行的。例如：
'a' 的 Unicode 值是 97。'b' 的 Unicode 值是 98。
因此，'a' < 'b' 是 True。
短字符串和长字符串的比较：如果两个字符串的前缀相同，较短的字符串被认为更小。
例如："apple" < "applepie" 是 True。
大小写敏感：
字符串比较是区分大小写的。例如："Hello" 和 "hello" 是不同的字符串。如果需要忽略大小写，可以先将字符串转换为统一的大小写形式（如使用 upper() 或 lower()）。'''

str1=''.join(reversed(str1))#join是把序列中的字母都组合起来的方法，''表示结合中间不加东西
print(str1)

i1=ord('a')#把字母转成ascii码表
print(i1)
s1=chr(97)#把ascii码表转成字母
print(s1)

t1='Hello world'
t1=t1.strip('H')#只能删除开头与结尾的字符，不输入参数默认删除空格
print(t1)
print('--------------------')
print('读取单词列表小案例')
t=open('PythonFoundation\words.txt')
poch=0
e='e'
for line in t:
    line=line.strip()
    idx=line.find(e)
    if(idx==-1) and len(line)>17:
        poch=poch+1
        print(line)
print('不含e的单词',poch)
print('--------------------')
'''另外一种检测方法
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True'''


