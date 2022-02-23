## 检查某个文件夹中是否存在指定的文件类型

> endswith 与 普通数据聚合相结合

```
if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):
```

