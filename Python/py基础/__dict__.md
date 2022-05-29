![图例](.\img\__dict__.png)



### 概念

+ \__dict__是用来存储对象属性的一个字典，其键为属性名，值为属性的值。

### 代码示例

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-
class A(object):
    class_var = 1
    def __init__(self):
        self.name = 'xy'
        self.age = 2

    @property
    def num(self):
        return self.age + 10

    def fun(self):pass
    def static_f():pass
    def class_f(cls):pass

if __name__ == '__main__':#主程序
    a = A()
    print a.__dict__   #{'age': 2, 'name': 'xy'}   实例中的__dict__属性
    print A.__dict__   
    '''
    类A的__dict__属性
    {
    '__dict__': <attribute '__dict__' of 'A' objects>, #这里如果想深究的话查看参考链接5
    '__module__': '__main__',               #所处模块
    'num': <property object>,               #特性对象 
    'class_f': <function class_f>,          #类方法
    'static_f': <function static_f>,        #静态方法
    'class_var': 1, 'fun': <function fun >, #类变量
    '__weakref__': <attribute '__weakref__' of 'A' objects>, 
    '__doc__': None,                        #class说明字符串
    '__init__': <function __init__ at 0x0000000003451AC8>}
    '''

    a.level1 = 3
    a.fun = lambda :x
    print a.__dict__  #{'level1': 3, 'age': 2, 'name': 'xy','fun': <function <lambda> at 0x>}
    print A.__dict__  #与上述结果相同

    A.level2 = 4
    print a.__dict__  #{'level1': 3, 'age': 2, 'name': 'xy'}
    print A.__dict__  #增加了level2属性

    print object.__dict__
    '''
    {'__setattr__': <slot wrapper '__setattr__' of 'object' objects>, 
    '__reduce_ex__': <method '__reduce_ex__' of 'object' objects>, 
    '__new__': <built-in method __new__ of type object at>, 
    等.....
    '''
```



### \__dict__属性总结

```

 1.类__dict__属性中包括类属性，类方法（非系统默认的，修改过的__init__()等，自己写的静态非静态方法），包括它实例化对象的方法
 
 2.对象的属性就是__init__方法中带有的属性，子类默认继承父类__init__时候，子类创建对象的属性与父类一致，取决于你是否重写__init__属性，你可以尝试在子类重写__init__方法，并修改属性
  
 3.可以通过操作对象__dict__属性来获取对象的属性。有时候会用到
```

```
自己总结： 对象的属性 实际是添加到 对象的 __dict__ 属性中 

```

### 用法延展

```python
person_info = {'name': 'xiaoming','age': 18,'gender': 'man'}
class Person1:
    def __init__(self, person_info):
        self.__dict__.update(person_info)

        
b = Person1(person_info)
print(b.name)

```

