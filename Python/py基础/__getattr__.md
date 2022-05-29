### 定义：

+ 如果属性查找（attribute lookup）在实例以及对应的类中（通过`__dict__`)失败， 那么会调用到类的`__getattr__`函数；
+ 如果没有定义这个函数，那么抛出AttributeError异常



```python
class A(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print('init')

    def mydefault(self, *args):
        print('default:' + str(args[0]))

    def __getattr__(self, name):
        print("other fn:", name)
        return self.mydefault


a1 = A(10, 20)
a1.fn1(33)
a1.fn2('hello')

#init
#other fn: fn1
#default:33
#other fn: fn2
#default:hello

第16行调用fn1属性时，查找不到次属性，程序调用__getattr__方法
```

```python
class ObjectDict(dict):
    def __init__(self, *args, **kwargs):
        super(ObjectDict, self).__init__(*args, **kwargs)

    def __getattr__(self, name):
        value = self[name]
        if isinstance(value, dict):
            value = ObjectDict(value)
        return value


if __name__ == '__main__':
    od = ObjectDict(asf = {'a': 1}, d = True)
    print(od.asf, od.asf.a)  # {'a': 1} 1
    print(od.d)  # True

```

