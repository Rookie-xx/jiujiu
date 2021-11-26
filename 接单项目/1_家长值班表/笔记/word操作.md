### 一、相关概念

> 1，Document对象，表示一个word文档。
> 2，Paragraph对象，表示word文档中的一个段落
> 3，Paragraph对象的text属性，表示段落中的文本内容。

### 

```python
# 创建文档对象
document = docx.Document()

# 设置文档标题，中文要用unicode字符串
title = document.add_heading(0)  #add_heading(self, text="", level=1)  如果*level*为0，则样式设置为' Title '，如果*level*不在0-9范围内，则引发|ValueError|

title.alignment = WD_PARAGRAPH_ALIGNMENT  #居中
title_run = title.add_run(u'' + data["title"])  #添加标题内容
title_run.font.name = u"微软雅黑"
title_run._element.rPr.rFonts.set(qn('w:eastAsia'), u'微软雅黑')  #设置标题字体
title_run.font.size = Pt(24)  #设置标题字体大小
title_run.font.color.rgb = RGBColor(0, 0, 0)  #字体颜色
# 往文档中添加段落
p = document.add_paragraph(data["context"])
```

