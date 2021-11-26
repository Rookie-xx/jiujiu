### [获取某一个月有多少天](https://www.cnblogs.com/fixdq/p/9885796.html)

```python
import calendar
monthRange = calendar.monthrange(2018, 10)
print monthRange 

#(0, 31)
#输出的是一个元组；
#第一个元素，数字0是这个月第一天的星期码（0星期一，6星期天）；
#第二个元素，数字31是这个月的天数；
```

[Python-标准库calendar的使用](https://blog.csdn.net/y472360651/article/details/82291753?ops_request_misc=&request_id=&biz_id=102&utm_term=pycalendar&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-0-82291753.first_rank_v2_pc_rank_v29&spm=1018.2226.3001.4187)

