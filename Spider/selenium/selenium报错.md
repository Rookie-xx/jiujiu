### 1.[关于sys.meta_path is None, Python is likely shutting down报错](https://blog.csdn.net/weixin_42346330/article/details/85336093)

> 1.网上查阅的方法是是说加quit就行了，其实这种方法治标不治本，每次 运行不加quit就会报错
>
> 原因分析：selenium版本和CHrome.chromedriver不匹配导致，每次Chromederiver调用chrome时后台都会打开一个Chromediver.
>
> 解决方法：升级selenium版本
>
> 查看selenium版本：pip show selenium
>
> 安装对应版本selenium：pip install selenium==3.141.0

