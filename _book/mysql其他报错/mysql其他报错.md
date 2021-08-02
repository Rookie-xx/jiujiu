# mysql其他报错

**[1].mysql服务器无法连接10055报错**

> <span style="color:red">原因:Win32 error code 10055: 由于系统缓冲区空间不足或列队已满，不能执行套接字上的操作</span>	
>
> 解决方法:修改windows 注册表：
>
> > 有两个相关值，一是修改MaxUserPort(最大连接数);另一个是修改**TcpTimedWaitDelay（**TCP/IP 可释放已关闭连接并重用其资源前，必须经过的时间**）**
> >
> > **据我的经验推断修改MaxUserPort为最佳。**
> >
> > 注册表位置如下，如果没有此项，需要手动添加
> >
> > HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters
> > <p>Value Name: MaxUserPort</p>
> > <p>Value Type: DWORD</p>
> > <p>Value data: 65534（十进制）</p>

**[2].this is incompatible with sql_mode=only_full_group_by**

> <span style="color:red">原因:ONLY_FULL_GROUP_BY  对于GROUP BY聚合操作，如果在SELECT中的列，没有在GROUP BY中出现，那么这个SQL是不合法的，因为列不在GROUP BY从句中。简而言之，就是SELECT后面接的列必须被GROUP BY后面接的列所包含</span>
>
> 解决：去掉sql_mode配置 ONLY_FULL_GROUP_BY
>
> ```mysql
> mysql> set session sql_mode='STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';
> 
> ```
>
> [文献连接](https://www.imooc.com/article/294753)
>