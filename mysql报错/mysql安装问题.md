# mysql安装问题

[1].在windos 的cmd下安装mysql

在mysql的bin目录下面执行： mysqld --install

>  报错：Install/Remove of the Service Denied
>
> 解决办法：
>
> 打开cmd.exe程序的时候选择“用管理员身份打开”。

[2].报错：

mysql启动失败：mysql服务无法启动 服务没有报告任何错误 解决方法

> 解决方法：
> a 删除自己创建的data，进入mysql的bin目录；
>
> b 执行mysqld  --initialize-insecure ，第一次执行的话，时间会久一些，执行结束后没有输出信息，查看bin的同级目录下会多出一个data文件夹，里面一堆文件。
> （不要自己创建data文件夹，配置完my.ini后执行mysqld --initialize-insecure会自己生成data文件，然后执行net start mysql就可以了）
>
> 3.在bin下执行执行mysqld  --initialize-insecure  报错Can't create directory 'C:\Program Files\MySQL\Data\'
> 解决方法：
> 以管理员模式执行dos



