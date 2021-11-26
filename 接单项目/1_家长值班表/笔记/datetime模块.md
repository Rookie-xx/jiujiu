[[一文搞懂python datetime模块-日期时间处理 ]](https://www.cnblogs.com/zhuwjwh/p/12325710.html)

### 前言

`datetime`是python的内置模块，用来处理日期和时间。
该模块常用的类有：

| 类名      | 功能说明     |
| --------- | ------------ |
| date      | 日期对象     |
| time      | 时间对象     |
| datetime  | 日期时间对象 |
| timedelta | 时间间隔     |
| tzinfo    | 时区信息对象 |

### 二、构造`datetime`对象

实例：

```python
a = datetime(2019,12,6,13,30,50)
print(a,type(a))
# 输出 :2019-12-06 13:30:50  <class 'datetime.datetime'> 
```

### 三、类方法

1. `datetime.today()`

返回本地区当前日期时间`datetime`对象

```python
a = datetime.today()
print(a,type(a))
# 输出 : 2021-11-24 21:31:09.862992 <class 'datetime.datetime'>
```

1. `datetime.now(tz=None)`

返回本地区当前日期时间`datetime`对象，可以添加时区tz
默认无时区时，返回结果和`datetime.today()`一致

```python
datetime.now()
# 输出 : datetime.datetime(2019, 12, 9, 13, 27, 54, 693978)
```

1. `datetime.combine(date, time, tzinfo=self.tzinfo)`

拼接`date`和`time`对象，形成一个新的`datetime`对象
可以输入时区参数，否则默认为原`time`的时区

```python
date_ = datetime.today().date()
time_ = datetime.today().time()
datetime.combine(date_,time_)
# 输出 : datetime.datetime(2019, 12, 9, 16, 12, 56, 914484)
```

1. `datetime.strptime(date_string, format)`

将格式化日期时间字符串，转换为`datetime`对象，可以转换日期、时间、日期时间

```python
datetime.strptime('2019-11-05','%Y-%m-%d')
# 输出 : datetime.datetime(2019, 11, 5, 0, 0)
datetime.strptime('09:30:50','%H:%M:%S')
# 输出 : datetime.datetime(1900, 1, 1, 9, 30, 50)
datetime.strptime('2019-11-05 09:30:50','%Y-%m-%d %H:%M:%S')
# 输出 : datetime.datetime(2019, 11, 5, 9, 30, 50)
```

### 四、实例方法

1. `datetime.date()`

返回`date`对象

```python
d = datetime(2019,12,6,13,30,50)
d.date()
# 输出 : datetime.date(2019, 12, 6)
```

1. `datetime.time()`

返回`time`对象

```python
d = datetime(2019,12,6,13,30,50)
d.time()
# 输出 : datetime.time(13, 30, 50)
```

1. `datetime.timestamp()`

对于给定的 `datetime`对象返回时间戳

```python
d = datetime(2019,12,6,13,30,50)
d.timestamp()
# 输出 : 1575610250.0
```

1. `datetime.weekday()`

返回星期几，星期一为 0，星期天为 6

```python
d = datetime(2019,12,6,13,30,50)
d.weekday()
# 输出 : 4
```

1. `datetime.isoweekday()`

返回星期几，星期一为 1，星期天为 7

```python
d = datetime(2019,12,6,13,30,50)
d.isoweekday()
# 输出 : 5
```

1. `datetime.isocalendar()`

返回数组：（年、第多少周、星期几）

```python
d = datetime(2019,12,6,13,30,50)
d.isocalendar()
# 输出 : (2019, 49, 5)
```

1. `datetime.ctime()`

返回日期时间的字符串表示

```python
d = datetime(2019,12,6,13,30,50)
d.ctime()
# 输出 : 'Fri Dec  6 13:30:50 2019'
```

1. `datetime.strftime(date_string, format)`

将`datetime`对象转换为格式化字符串

```python
d = datetime.today()
datetime.strftime(d,'%Y-%m-%d %H:%M:%S')
# 输出 : '2019-12-09 16:32:18'
```

 1.`datetime.isoformat(sep='T', timespec='auto')`

```python
x = datetime.today()
print("Normal format:",x)
d = x.isoformat()
print("ISO 8601 format:", d)
print("ISO 8601 format without separator 'T':", x.isoformat(sep=' '))

#Normal format: 2020-05-01 22:52:37.596841
ISO 8601 format: 2020-05-01T22:52:37.596841
ISO 8601 format without separator 'T': 2020-05-01 22:52:37.596841

```

