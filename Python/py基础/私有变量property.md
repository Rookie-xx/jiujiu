+ 通常两个公开的的属性，保护一个私有变量
+ @property负责读取，@属性名.setter 负责写入
+ 只写：属性名=property(None,写入方法名)



### **事物演变的过程**

demo_1

```python
# 使用方法，封装变量
class Wife:
    def __init__(self,name,age,weight):
        self.name = name
        # 本质：障眼法 (实际将变量名改为：_类名__age)
        # self.__age = age
        self.set_age(age)
        self.weight = weight

    #提供公开的读写方法
    def get_age(self):
        return self.__age

    def set_age(self,value):
        if 21 < value < 31:
            self.__age = value
        else:
            raise ValueError('FUCK!!')
"""
w01 = Wife('蕾姆',87,87)
#重新创建了新实例变量(没有改变类中定义的__age)
# w01.__age = 107
w01._Wife__age = 107 #(修改了类中定义的私有变量)

print(w01.__dict__) #存储对象的实例变量
"""
w01 = Wife('蕾姆',87,87)
w01.set_age(25)
print(w01.get_age())
```

demo_2

```python
"""
使用property(读取方法，写入方法)，封装变量
"""

class Wife:
    def __init__(self,name,age,weight):
        self.name = name
        # self.set_age(age)
        self.age = age
        self.weight = weight


    #提供公开的读写方法
    def get_age(self):
        return self.__age

    def set_age(self,value):
        if 21 < value < 31:
            self.__age = value
        else:
            raise ValueError('FUCK!!')

    #属性  property对象拦截对age类变量的读写操作
    age = property(get_age,set_age)

    def get_weight(self):
        return self.__weight

    def set_weight(self,value):
        if 51 < value < 71:
            self.__weight = value
        else:
            raise ValueError('FUCK!!')

    weight = property(get_weight,set_weight)

w01 = Wife('蕾姆',22,52)
# w01.set_age(25)
w01.age = 25     #在写入时执行写入方法
print(w01.age)
print(w01.__dict__)
print(w01.get_age())
w01.weight = 60
print(w01.weight)

```

demo_3

```python
"""
使用property(读取方法，写入方法)，封装变量
"""

class Wife:
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight


    @property  #创建property对象，只负责拦截读取操作
    def age(self):
        return self.__age

    @age.setter  #只负责拦截写入操作
    def age(self,value):
        if 21 < value < 31:
            self.__age = value
        else:
            raise ValueError('FUCK!!')

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self,value):
        if 51 < value < 71:
            self.__weight = value
        else:
            raise ValueError('FUCK!!')

w01 = Wife('蕾姆',22,52)
# w01.set_age(25)
w01.age = 25     #在写入时执行写入方法
print(w01.age)
print(w01.__dict__)

w01.weight = 60
print(w01.weight)
```

