图解<img src="H:\图片\dump,dumps,load,loads.png" style="zoom:150%;" />

### dumps() 和loads()

+ 是在字典与字符串之间的类型转换

```python
import json
 
dict1 = {'a':1,'b':2,'c':3}
str1 = json.dumps(dict1)
print(type(str1), str1)
 
mydict = json.loads(str1)
print(type(mydict), mydict)
```

### dump() 和load()

+ 是在字典与文件之间进行存盘和加载

```python
dict1 = {'a':1,'b':2,'c':3}
f1 = open("test.txt", 'w', encoding='utf-8')
str1 = json.dump(dict1, f1)
f1.close()
 
print("\n====文件内容===")
!type test.txt
print("====end===\n")
 
f2 = open("test.txt", 'r', encoding='utf-8')
mydict = json.load(f2)
print(type(mydict), mydict)
f2.close()
```

### **jsonpath使用**

| XPath | JSONPath | 描述                                                         |
| ----- | -------- | ------------------------------------------------------------ |
| /     | $        | 根节点                                                       |
| .     | @        | 现行节点                                                     |
| /     | .or[]    | 取子节点                                                     |
| ..    | n/a      | 取父节点，Jsonpath未支持                                     |
| //    | ..       | 就是不管位置，选择所有符合条件的条件                         |
| *     | *        | 匹配所有元素节点                                             |
| @     | n/a      | 根据属性访问，Json不支持，因为Json是个Key-value递归结构，不需要属性访问。 |
| []    | []       | 迭代器标示（可以在里边做简单的迭代操作，如数组下标，根据内容选值等） |
| \|    | [,]      | 支持迭代器中做多选。                                         |
| []    | ?()      | 支持过滤操作.                                                |
| n/a   | ()       | 支持表达式计算                                               |
| ()    | n/a      | 分组，JsonPath不支持                                         |

```json
book_dict = { 
  "store": {
    "book": [ 
      { "category": "reference",
        "author": "Nigel Rees",
        "title": "Sayings of the Century",
        "price": 8.95
      },
      { "category": "fiction",
        "author": "Evelyn Waugh",
        "title": "Sword of Honour",
        "price": 12.99
      },
      { "category": "fiction",
        "author": "Herman Melville",
        "title": "Moby Dick",
        "isbn": "0-553-21311-3",
        "price": 8.99
      },
      { "category": "fiction",
        "author": "J. R. R. Tolkien",
        "title": "The Lord of the Rings",
        "isbn": "0-395-19395-8",
        "price": 22.99
      }
    ],
    "bicycle": {
      "color": "red",
      "price": 19.95
    }
  }
}

from jsonpath import jsonpath
print(jsonpath(book_dict,'$..author')) #如果取不到返回false

```

| JsonPath               | Result                  |
| ---------------------- | ----------------------- |
| $.store.book[*].author | store中的所有的book作者 |
| $…author               | 所有的作者              |
| $.store.*              | store下的所有元素       |
| $.store…price          | store中的所有价钱       |
| $…book[2]              | 第三本书                |
| $…book[(@.length-1)]   | 最后一本书              |
| $…book[0,1]            | 取前两本书              |
| $…book[?(@.isbn)]      | 获取有jsbn的所有数      |
| $…book[?(@.price<10)]  | 获取价格大于10          |
| $…*                    | 匹配所有数据            |



### **问题**

+ json.dumps,json.dump输出中文

  > [链接](https://blog.csdn.net/seapeak007/article/details/71081904)
  >
  > python的json.dumps方法默认会输出成这种格式`"\u2535a\u35a2\u89bd",`。
  >
  > 要输出中文需要指定ensure_ascii参数为False，如下代码片段：

```python
json.dumps({'text':"你好"},ensure_ascii=False,indent=2)

json.dump(appjson_list,f,ensure_ascii=False,indent=2)

#indent=2表示缩进
```



