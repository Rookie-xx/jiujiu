## openpyxl常用方法

[Python_Openpyxl 浅谈](https://blog.csdn.net/weixin_43094965/article/details/82226263?ops_request_misc=&request_id=&biz_id=102&utm_term=openpyxl&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-82226263.first_rank_v2_pc_rank_v29&spm=1018.2226.3001.4187)

#### 读取Excel文档

```python
import openpyxl

# 文件必须是xlsx格式，如果是其他格式在执行前可利用win32辅助转化
wb = openpyxl.load_workbook(‘example.xlsx’)

#函数作用
#打开给定的文件名并返回工作簿

#参数的含义
#1.filename 文件名:打开的路径或一个类文件对象
#2. read_only:优化阅读，内容不能编辑
#3. keep_vba:保存vba内容
#4. data_only:控制带有公式的单元格是否具有公式(默认值)或上次Excel读取工作表时存储的值
#5. keep_links:是否应保留对外部工作簿的链接。默认为True
```

#### 获取工作表

> 每一个Excel表格中都会有很多张sheet工作表，在对表格操作前需要先选定一张工作表

```python
# 获取所有工作表名(返回一个列表)
sheets = wb.get_sheet_names()

# 获取某一特定的工作表
sheet = wb.get_sheet_by_name('Sheet2')

# 获取工作表的表名
sheet_name = sheet.title

# 一般来说，表格大多数用到的是打开时显示的工作表，这时可以用active来获取当前工作表
sheet = wb.active
```

#### 获取单元格

> 对Excel表格的操作最终都落于对单元格的操作，获取单元格有两种获取方法：**sheet[列行名]\**和\**sheet.cell(row,column)**

```python
# 通过sheet[列行名]获取
a = sheet['A2']

# 通过sheet.cell(row,column)获取
b = sheet.cell(1, 2)  # 即sheet['B1']

# 获取单元格内容
print(a.value)

# 获取单元格所在列和行
print(‘a is ’+str((a.column,a.row)))
```



### 打开文件

#### ① 创建

```python
from  openpyxl import  Workbook 
# 实例化
wb = Workbook()
# 激活 worksheet
ws = wb.active
```

#### ② 打开已有

```python
>>> from openpyxl  import load_workbook
>>> wb2 = load_workbook('文件名称.xlsx')
```

### 储存数据

```python
# 方式一：数据可以直接分配到单元格中(可以输入公式)
ws['A1'] = 42
# 方式二：可以附加行，从第一列开始附加(从最下方空白处，最左开始)(可以输入多行)
ws.append([1, 2, 3])
# 方式三：Python 类型会被自动转换
ws['A3'] = datetime.datetime.now().strftime("%Y-%m-%d")

```

