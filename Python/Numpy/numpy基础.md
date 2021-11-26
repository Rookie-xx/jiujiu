[toc]

## ndarry数组

#### 用np.ndarray类的对象表示n维数组

```python
import numpy as np
ary = np.array([1,2,3,4,5,6])
print(type(ary))
```

## 内存中ndarray对

dim ---> 维数

shape ---> 维度

dtype ---> 每个元素的数据类型

![](C:\Users\my\Desktop\mybook\图片\ndarray内存.png)

#### 元数据(metadata)

> 存储对目标数组的描述信息，如:dimcount、dimensions、dtype、data等。

#### 实际数据

> 完整的数组数据
>
> 将实际数据与元数据分开存放，一方面提高了内存空间的使用效率，另一方面减少对实际数据的访问频率，提高性能。

#### ndarry数组对象的特点

1. Numpy数组是同质数组，即所有元素的数据类型必须相同
2. Numpy数组的小标从0开始，最后一个元素的下标为数组长度减1

#### ndarry数组对象的创建

##### np.array(任何可被解释为Numpy数组的逻辑结构)

```python
imprt numpy as np
a = np.array([1,2,3,4,5,6])
print(a)
```

##### np.arange(起始值(0),终止值,步长(1))

```python
import numpy as np
a = np.arange(0,5,1)
print(a)  
b= np.arange(0,10,2)
print(b)
```

##### np.zeros(数组元素个数,dtype='类型')

```python
import numpy as np
c = np.zeros(10,dtype='int32')
print(c,c.dtype)
```

##### np.ones(数组元素个数,dtype='类型')

```python
import numpy as np
d = np.ones((2,3),dtype='float32')
print(d,d.shape,d.dtype)
```

##### #扩展

```python
d = np.ones((2,3),dtype='float32')
print(d,d.shape,d.dtype)
e = np.zeros_like(d)
print(e)
```

#### ndarray对象属性的基本操作

##### **数组的维度**：np.ndarray.shape

```python
import numpy as np
ary = np.array([1,2,3,4,5,6])
print(type(ary),ary,ary.shape)

#二维数组
ary = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print(type(ary),ary,ary.shape)
```

##### 元素的类型：np.ndarray.dtype

```python
import numpy as np
ary = np.array([1,2,3,4,5,6])
print(type(ary),ary,ary.dtype)

#转换ary元素的类型
b = ary.astype(float)
print(type(b),b,b.dtype)

#转换ary元素的类型
c = ary.astype(str)
print(type(c),c,c.dtype)
```

##### 数组元素个数：np.ndarray.size

```python
import numpy as np
ary = np.array([
	[1,2,3,4],
	[5,6,7,8]
])
#观察维度,size,len的区别
print(ary.shape,ary.size,len(ary))
```

##### 数组元素索引(下标)

> 数组对象[...,页号,行号,列号]
>
> 下标从0开始,到数组len-1结束
>
> ```python
> import numpy as np
> 
> c = np.arange(1,19)
> c.shape = (3,2,3)
> print(c)
> 
> print(c[0])
> print(c[0][1])
> print(c[0][1][0])
> print(c[0,1,0])
> 
> for i in range(c.shape[0]):
>     for j in range(c.shape[1]):
>         for k in range(c.shape[2]):
>             print(c[i,j,k])
> ```

#### ndarray对象属性操作详解

##### Numpy的内部基本数据类型

| 类型名       | 类型标识符                         |
| ------------ | ---------------------------------- |
| 布尔型       | bool                               |
| 有符号整数型 | int8(-127~127)/int16/int32/int64   |
| 无符号整数型 | uint8(0~255)/uint16/uint32/uint64  |
| 浮点型       | float16/float32/float64            |
| 复数型       | complex64/complex128               |
| 字符串       | str_,每个字符用32位Unicode编码表示 |

##### 自定义复合类型

```python
#自定义复合类型
import numpy as np

data=[
	('zs',[90,80,85],15),
	('ls',[92,81,83],16),
	('ww',[95,85,95],15)
]
#第一种设置dtype的方式
a = np.array(data,dtype='U2,3int32,int32')
print(a)
print(a[0]['f0'],":",a[1]['f1'])
print("===================================")
#第二种设置dtype的方式
a = np.array(data,dtype=[('name','str',2),
						 ('scores','int32',3),
						 ('age','int32',1)])
print(a)
print(a[2]['age'])
print("===================================")
#第三种设置dtype的方式
a = np.array(data,dtype={'names':['name','score','age'],
						 'formats':['U2','3int32','int32']})
print(a)
print(a[1]['name'])
print("===================================")
#数组中存储日期数据类型
dates = ['2011-01-01','2011','2011-02',
		 '2012-01-01','2012-02-01 10:10:00']
dates = np.array(dates)
#类型转换
dates = dates.astype('M8[D]')
print(dates,dates.dtype)
print(dates[2]-dates[1])
```

##### 数型字符码

![](C:\Users\my\Desktop\mybook\图片\字符码.png)

#### ndarray数组对象的维度操作

视图变维（数据共享）：reshape()与ravel()

```python
import numpy as np

a = np.arange(1,10)
print(a,a.shape)

#视图变维
b = a.reshape(3,3)
print(a,'->a')
a[0] = 999
print(b,'->b')
print(b.ravel()) #抻平

#复制变维
c = b.flatten()
print(c,'->c')
b[0][0] = 88
print(c,'->c')

#就地变维
c.shape = (3,3)
print(c,'->c')
c.resize((9,))
print(c,'->c')
```

###### ndarray数组切片操作

```python
#数组对象切片的参数设置与列表切面参数类似
# 步长+:默认切从首到尾
# 步长-:默认切从尾到首
数组对象[起始位置:终止位置:步长,...]
#默认位置步长：1
```

```python
import numpy as np

#一维数组切片
a = np.arange(1,10)
print(a)           # 1 2 3 4 5 6 7 8 9
print(a[:3])       # 1 2 3 
print(a[3:6])      # 3 4 5 
print(a[6:])       # 6 7 8 9
print(a[::-1])     # 9 8 7 6 5 4 3 2 1 
print(a[:-4:-1])   # 9 8 7
print(a[-4:-7:-1]) # 6 5 4
print(a[-7::-1])   # 3 2 1
print(a[::])       # 1 2 3 4 5 6 7 8 9
print(a[:])		   # 1 2 3 4 5 6 7 8 9
print(a[::3])      # 1 4 7 
print(a[1::3])     # 2 5 8
print(a[2::3])     # 3 6 9

# 二维数组的切片
a.resize((3,3))
print(a)
print(a[:2,:2])
print(a[::2,::2])
```

#### ndarray数组的掩码操作

```python
import numpy as np
a = np.arange(1,10)
mask = [True,False,True,False,True,False,True,False,True]
print(a[mask])

#基于bool数组的掩码
a = np.arange(100)
#输出100以内3的倍数
print(a[a%3==0])
#输出100以内既是3的倍数又是7的倍数
mask = (a%3==0)&(a%7==0)
print(a[mask])

#基于索引的掩码
name = np.array(['Apple','Mate30 pro','Mi','Oppo','Vivo'])

rank = [1,0,3,4,2]
print(name[rank])
```

#### 多维数组的组合与拆分

##### 垂直方向操作：

```python
import numpy as np
a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)
#垂直方向完成组合操作，生成新数组
c = np.vstack((a,b))
#垂直方向完成拆分操作,生成两个数组
d,e = np.vsplit(c,2)
```

##### 水平方向操作

```python
import numpy as np
a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)
#水平方向完成组合操作，生成新数组
c = np.hstack((a,b))
#水平方向完成拆分操作,生成两个数组
d,e = np.hsplit(c,2)
```

##### 深度方向操作：(3维)

```python
import numpy as np
a = arange(1,7).reshape(2,3)
b = arange(7,13).reshape(2,3)
#深度方向完成组合操作，生成新数组
c  =np.dstack((a,b))
print(c,'--->dc')
a,b = np.dsplit(c,2)
print(a,'--->da')
print(b,'--->db')

```

##### 多维数组组合与拆分的相关函数

```python
#通过axis作为关键字参数指定组合的方向,取值如下:
#若待组合的数组都是二维数组:
#	0:垂直方向组合
#	1:水平方向组合
#若待组合的数组都是三:
#	0:垂直方向组合
#	1:水平方向组合
#   2：深度方向组合
np.concatentate((a,b),axis=0)
#通过给出的数组与要拆分的份数，按照某个方向进行拆分
np.split(c,2,axis=0)
```

##### 长度不等的数组组合

```python
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4])
#填充b数组使其长度与a相同，头部补0个元素，尾部补1个元素
b = np.pad(b,pad_width=(0,1),mode='constant',constant_values=-1)
print(b)
#垂直方向完成组合操作，生成新数组
c = np.vstack((a,b))
print(c)
```

##### 一维数组的组合方案

```python
#一维数组的组合方案
a = np.arange(1,9)
b = np.arange(9,17)
print(a)
print(b)
print(np.row_stack((a,b))) #形成两行
print(np.column_stack((a,b))) #形成两列
```

#### ndarray类的其他属性

+ shape - 维度
+ dtype - 元素类型
+ size - 元素数量
+ ndim - 维数，len(shape)
+ itemsize - 元素字节数
+ nbytes - 总字节数 = size x itemsize
+ real - 复数数组的实部数组
+ imag - 复数数组的虚部数组
+ T - 数组对象的转置视图
+ flat - 扁平迭代器

```python
import numpy as np

a = np.array([[1+1j,2+4j,3+7j],
              [4+2j,5+5j,6+8j],
              [7+3j,8+6j,9+9j]])


print(a.shape)
print(a.dtype)           ----complex128
print(a.itemsize)        ----16
print(a.size)            -----9
print(a.nbytes)          -----144
print(a.real)
print(a.imag)
print(a.T)
print([x for x in a.flat])  
```

