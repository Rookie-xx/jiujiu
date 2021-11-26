### str

```python
S.find(sub[, start[, end]]) -> int
"""
返回S中找到子字符串sub的最低下标，
使sub包含在S[start:end]中。可选
参数start和end被解释为片表示法。
失败时返回-1。
"""
a = '邀请'
b = '邀请函标题'
print(b.find(a))  # 0
a = '邀标'
b = '邀请函标题'
print(b.find(a))  # -1
```



```python
import string

print(string.ascii_letters)
#'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
```

