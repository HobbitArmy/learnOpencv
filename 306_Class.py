# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:46:09 2017

@author: Green
"""

class Myclass:
    a = 123
    def f(self):
        return "hello"
x = Myclass
print(x.a)
print(x.f)

class Complex:
    def __init__(self, real, imag):
        self.r = real
        self.i = imag
x = Complex(5, -4)
print(x.r, x.i)

""" self代表类的实例，而非类;类的方法与普通的函数只有一个特别的区别——
它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
self 不是 python 关键字，我们把他换成其他也是可以正常执行的 """

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t = Test
t.prt('hob')
        
"""类的方法在类地内部,使用 def 关键字来定义一个方法，与一般函数定义不同，
类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。 """
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w
    def prt(self):
        print('%s says : I am %d years-old now'%(self.name, self.age))
p = People('Hobbit', 113, 45)
p.prt()
"""类的继承"""
class Student(People):
    grade = ''
    def __init__(self, n, a, w, g):
        # 调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g
    def plt(self):
        print('%s says : I am %d years-old , and i am in the\
 %d-Grade now.'%(self.name, self.age, self.grade))
s = Student('Hobbit', 113, 45, 16)
s.plt()

"""多重继承"""
class Speaker():
    topic = ''
    career = ''
    def __init__(self, t, c):
        self.topic = t
        self.career = c
    def plt(self):
        print("hello, im a %s, im going to talk about %s."%(self.career, self.topic))
        
class Multi(Speaker, Student):
    def __init__(self, n, a, w, g, t, c):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, t, c)
m = Multi('LUCK', 19, 60, 14, 'SEX', 'student')
m.plt() # 方法名同，默认调用的是在括号中排前地父类的方法
        
""" 类属性与方法:
*1 类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问.
在类内部的方法中使用时 self.__private_attrs.
*2 类的方法
在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，且为第一个参数，
self 代表的是类的实例.self 的名字并不是规定死的,也可以使用 this,但是最好还是按照约定是用 self.
*3 类的私有方法
__private_method:两个下划线开头,声明该方法为私有方法,只能在类的内部调用,
不能在类地外部调用.self.__private_methods. """

class Test1:
    __secretCount = 0
    publicCount = 0
    
    def count(self):
        self.__secretCount += 1 # 私有变量
        self.publicCount += 1 # 公有变量
        print(self.__secretCount)
counter = Test1()
counter.count()
counter.count()
print(counter.publicCount)
print(counter.__secretCount) #！！！ 会报错,实例不能访问私有变量

class Test2:
    def __init__(self, name, url):
        self.name = name # public
        self.__url = url # private
    def who(self):
        print(self.name)
        print(self.__url)
    def __foo(self): # 私有方法
        print('private')
    def foo(self): # 公共方法
        print('public')    
        self.__foo()
t = Test2('Hobbit', 'www.hobbit.com')
t.who()
t.foo()
t.__foo() #！！！ 报错，外部不能调用私有方法
    





        


        
        
        
        
        