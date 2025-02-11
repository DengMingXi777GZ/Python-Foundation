import copy
import random
#类和对象
#程序员自定义类型被称作类Class
class Point:
    '1234'
    def print_point(p):
        print('(%g,%g)'%(p.x,p.y))

blank = Point()#创建一个新对象的过程叫做实例化(instantiation)，这个新对象叫做这个类的一个实例(instance)
blank.x = 3.0   
blank.y = 4.0 #给实例的属性赋值

x1=blank.x #通过实例访问属性,这里的x1是变量，x是属性
print(x1,type(x1),blank.x,type(blank.x))#x1和blank.x是一样的
blank.print_point()#通过实例调用方法

class rectangle:
    pass
box=rectangle()
box.width=100.0
box.height=200.0
box.corner=Point()
box.corner.x=0.0
box.corner.y=0.0#表达式box.corner.x 的意思是，‘‘前往box 所引用的对象，找到叫做corner的属性；然后
#前往corner 所引用的对象，找到叫做x的属性。
print('-----------------')
def find_center(rect):
    p=Point()
    p.x=rect.corner.x+rect.width/2
    p.y=rect.corner.y+rect.height/2
    return p
center=find_center(box)
center.print_point()
print('-----------------')
#改变矩形大小却不改变位置,对象是可变的
def grow_rectangle(rect,dwidth,dheight,dcornerx,dcornery):
    rect.width+=dwidth
    rect.height+=dheight
    rect.corner.x+=dcornerx
    rect.corner.y+=dcornery
    return rect
grow_rectangle(box,50,100,10,10)
center=find_center(box)
center.print_point()
print('-----------------')
#copy()方法可以复制一个对象,但无法复制嵌套的point对象
p1=Point()
p1.x=3
p1.y=4
p2=copy.copy(p1)
l1=[1,2,3]
l2=copy.copy(l1)
print(p1 is p2,p1==p2,p1,p2)#False False
print(l1 is l2,l1==l2,l1,l2)#False True

box2=copy.copy(box)
print(box2 is box,box2==box,box.corner is box2.corner,box.corner,box2.corner)#False False True 
box2=copy.deepcopy(box)
print(box2 is box,box2==box,box.corner is box2.corner,box.corner,box2.corner)#False False False 真是真正的数值复制而不影响地址
#查询是不是是实例
print(isinstance(box,rectangle))#True
#如果你不确定一个对象是否拥有某个属性，你可以使用内置函数hasattr检查
print(hasattr(box,'corner'))#True
#列出对象的属性
print(dir(box))
print('----------------------------------------------------------------------')
#类与函数
class Time:
    pass

time=Time()
time.hour=11
time.minute=59
time.second=30
def print_time(time):
    print('%.2d:%.2d:%.2d'%(time.hour,time.minute,time.second))
print_time(time)

#编写一个叫做is_after的布尔函数，接收两个Time对象，t1和t2，若t1的时间在t2之后，则返回True，否则返回False。挑战：不要使用if语句
def is_after(t1,t2):
    return(t1.hour>=t2.hour and t1.minute>=t2.minute and t1.second>=t2.second)
t1=Time()
t1.hour=12
t1.minute=59
t1.second=30
t2=Time()
t2.hour=11
t2.minute=59
t2.second=30
print(is_after(t1,t2))

print(dir(t1))#打印类的文档字符串
print('----------------------------------------------------------------------')

def mul_time(time,n):
    new_time=Time()
    time_sum=(time.hour*3600+time.minute*60+time.second)*n
    new_time.hour=time_sum//3600
    new_time.minute=(time_sum-new_time.hour*3600)//60
    new_time.second=time_sum-new_time.hour*3600-new_time.minute*60
    return new_time
new_time=mul_time(time,2)
print(new_time.hour,new_time.minute,new_time.second)
print('----------------------------------------------------------------------')
#类的方法
class Time:
    def print_time(self):
        print('%.2d: %.2d: %.2d' % (self.hour, self.minute, self.second))
    def timetoint(self):
        return self.hour*3600+self.minute*60+self.second
    def inttotime(self,time_sum):
        self.hour=time_sum//3600
        self.minute=(time_sum-self.hour*3600)//60
        self.second=time_sum-self.hour*3600-self.minute*60
    def increment(self, seconds):
        seconds += self.timetoint()
        return self.inttotime(seconds)


test=Time()
test.hour=12
test.minute=59
test.second=30
test.print_time()
Time.print_time(test)#等价于上面的调用方法 ,Time是类的名字，test是实例的名字

test.increment(100)#time_sum函数放在类里面，是一个值，也有些函数放一个类在里面，是一个方法
test.print_time()

print('----------------------------------------------------------------------')
#init方法，初始化一个对象
class Time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour=hour
        self.minute=minute
        self.second=second
    def __str__(self):
        return ('%.2d: %.2d: %.2d' % (self.hour, self.minute, self.second))
    
    def __add__(self,other):
        if isinstance(other,Time):
            #isinstance()函数可以检查一个对象是否是一个类的实例，（对象，类），是就返回True
            time_sum=self.timetoint()+other.timetoint()
            self.inttotime(time_sum)
            return self
        else:
            return self.increment(other)

    
    def timetoint(self):
        return self.hour*3600+self.minute*60+self.second
    def inttotime(self,time_sum):
        self.hour=time_sum//3600
        self.minute=(time_sum-self.hour*3600)//60
        self.second=time_sum-self.hour*3600-self.minute*60
    def increment(self, seconds):
        seconds += self.timetoint()
        return self.inttotime(seconds)

test=Time()#可以在括号里赋值，也可以在后面覆盖属性
test.second=30
print(test)#调用__str__方法
strat=Time(12,59,30)
duration=Time(1,30)
strat+duration
print(strat)#+号调用__add__方法,print调用__str__方法
duration1=90
print(type(duration1))
strat+duration1
print(strat)
print('----------------------------------------------------------------------')
#还有哪些特殊方法
# __init__ 初始化一个新创建的对象
# __str__ 返回一个对象的字符串表示
# __add__ 定义加法运算符
# __lt__ 定义小于运算符
# __eq__ 定义等于运算符
# __len__ 定义len()函数
# __getitem__ 定义索引运算符
#介绍一下getitem()方法,
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __getitem__(self,index):
        if index==0:
            return self.x
        elif index==1:
            return self.y
        else:
            return 'error'
p=Point(3,4)
print(p[0],p[1],p[2])
# __setitem__ 定义赋值运算符
# __contains__ 定义in运算符
# __call__ 定义()运算符
# __getattr__ 定义点运算符
# __setattr__ 定义赋值点运算符
# __delattr__ 定义删除点运算符
print('----------------------------------------------------------------------')
'''我们做个练习，为Points编写一个add方法，使其既适用Point对象，也适用元组：
• 如果第二个运算数是一个Point，该方法将返回一个新的Point，x坐标是两个运算
数的x的和，y以此类推。
• 如果第二个运算数是一个元组，该方法将把元组的第一个元素与x相加，第二个
元素与y相加，然后返回以相关结果为参数的新的Point。'''

class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    def __add__(self,other):
        if isinstance(other,Point):
            self.x=self.x+other.x
            return self
        elif isinstance(other,tuple):
            self.x=self.x+other[0]
            self.y=self.y+other[1]
            return self
        else:
            return 'error'

p1=Point(3,4)
p2=Point(5,6)
p3=(1,2)
p1+p2
print(p1.x,p1.y)
p1+p3
print(p1.x,p1.y)#p1的值被改变了
print('----------------------------------------------------------------------')

class kangaroo:
    def __init__(self):
        self.pounch_contents=[]

    def put_in_pounch(self,object):
        self.pounch_contents.append(object)

    def __str__(self):
        #返回Kangaroo 对象的字符串表示和pounch中的内容。
        t=[object.__str__() for object in self.pounch_contents]

        return ' '.join(t)
kanga=kangaroo()
roo=kangaroo()
roo.put_in_pounch('money')
kanga.put_in_pounch(roo)
print(kanga)
print(roo)
print('----------------------------------------------------------------------')
#继承
class poke:
    def __init__(self,suit=0,rank=2):
        self.suit=suit
        self.rank=rank
    suit_name=['Spades','Hearts','Diamonds','Clubs']
    rank_name=[None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']

    def __str__(self):
        return '%s of %s'%(poke.rank_name[self.rank],poke.suit_name[self.suit])#这就是类属性，实例化后再定义的属性是实例属性

    def __lt__(self,other):
        if self.suit<other.suit:
            return True
        if self.suit>other.suit:
            return False
        return self.rank<other.rank

p1=poke(2,11)
print(p1)
p2=poke(3,11)
t=p1<p2
print(t)

class Deck:
    def __init__(self):
        self.cards=[]
        for suit in range(4):
            for rank in range(1,14):
                card=poke(suit,rank)
                self.cards.append(card)#这里的self.cards是一个列表，列表里的元素是poke类的实例
    
    def __str__(self):
        res=[]
        print(type(self.cards),'122222222222Deck')
        print(self.cards,'Deck')#这里的self.cards是一个列表，列表里的元素是poke类的实例,存放的全是地址，需要str方法取出来
        for card in self.cards:
            res.append(str(card))
        print(res,'Deck')
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop() #pop()方法返回的是一个对象,是被删除的对象

    def add_card(self,card):
        self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards) #random.shuffle()方法是打乱列表的顺序


deck=Deck()
print(deck)

class Hand(Deck):
    #将Deck类作为父类，Hand类继承Deck类
    def __init__(self,label=''):
        self.cards=[]
        self.label=label
        #调用init时是为hand类创建一个新的实例，这个实例有一个属性cards，这个属性是一个列表，这个列表是空的
        #如果我们提供一个Hand的init方法，它会覆盖从Deck类继承来的同名方法。这就是方法重写


hand=Hand('new hand')#没有生成card属性，suit_name属性，rank_name属性,
print(hand.cards,hand.label)#直接继承poke的——__str__

deck=Deck()
deck.shuffle()
card=deck.pop_card()#牌堆发牌
print('----')
hand.add_card(card)#手牌接受牌
print(hand)#直接继承poke的——__str__
print('------------------')

class PingPongParent:
    pass
class Ping(PingPongParent):
    def __init__(self, pong):
        self.pong = pong
class Pong(PingPongParent):
    def __init__(self, pings=None):
        if pings is None:
            self.pings = []
        else:
            self.pings = pings
    def add_ping(self, ping):
        self.pings.append(ping)

pong = Pong()
ping = Ping(pong)
pong.add_ping(ping)
print(ping.pong)#<__main__.Pong object at 0x0000015CC5862C10>
print(pong.pings)#[<__main__.Ping object at 0x0000015CC5862C40>],列表里的元素是地址

g=[x**2 for x in range(1,4)]
print(g)
#any和all函数很好用
print(any([False,True,False]))#只要有一个为True就返回True
print(all([False,False,False]))#只要有一个为False就返回False
print(all([True,True,True]))
print('------------------')
#集合
#集合是一个无序的集合，没有重复元素，相当于没有值的字典
s=set()
s.add(1)
s.add(2)
print(s)
s.add(2)
print(s)
s.remove(2)
print(s)
#一次加入多个元素
s.update([2,3,4])
print(s)
def has_duplicates(t):

    return len(set(t))<len(t)
t=[1,2,3,4,5,6,7,8,9,0,1]
print(has_duplicates(t))
t=set(t)#去重
print(t)
print('------------------')
#计数器
from collections import Counter
count=Counter('parrot')
print(count)

