## 一）git使用

1. 流程图

   ```mermaid
   graph LR
   a[工作区]-.add.->b((暂存区))-.commit.->c[仓库区 ]
   ```

   

2. 基本概念

   + 工作区：项目所在操作目录，实际操作项目的区域
   + 暂存区：用于记录工作区的工作(修改)内容
   + 仓库区：用于备份工作区的内容 

   > 注意：在本地仓库中，git总是希望工作区的内容与仓库区保持一致，而且只有仓库区的内容才能和其他远程仓库交互。

3. 初始设置

   > 配置命令：git config

   + 配置所有用户：git config --system [选项]

     > 配置文件位置：/etc/gitconfig

   + 配置当前用户：git config --global [选项]

     > 配置文件位置：~/.gitconfig

   + 配置当前项目：git config [选项]

     > 配置文件位置：project/.git/config

   > 配置用户名
   >
   > ```git
   > e.g. 将用户名设置为tiny
   > git config --system user.name tiny
   > ```
   >
   > 配置用户邮箱
   >
   > ```git
   > e.g. 将邮箱设置为lvze@126.com
   > git config --system user.email lvze@126.com
   > ```
   >
   > 配置编译器
   >
   > ```
   > e.g. 将编译器设置为pycahrm
   > git config core.editor pycharm
   > ```
   >
   > 

4. 基本命令

   + 初始化仓库

     > git init
     >
     > 意义：将某个项目目录变为git操作目录，生成git本地仓库。即该项目目录可以使用git管理

   + 查看本地仓库状态

     > git status
     >
     > 说明：初始化仓库后默认工作在master分支，当工作区与仓库区不一致时会有提示。

   + 将工作内容记录到暂存区

     > git add [files..]
     >
     > ```git
     > e.g.  将 a b 记录到暂存区
     > git add a b
     > 
     > e.g. 将所有文件（不包含隐藏文件）记录到暂存区
     > git add *
     > ```

   + 取消文件暂存记录

     > git rm --cached [file]

   + 将文件同步到本地仓库

     > git commit [file] -m [message]
     >
     > 说明：-m表示添加一些同步信息，表达同步内容
     >
     > ```git
     > e.g. 将暂存区所有记录同步到仓库区
     > git commit -m 'add files'
     > ```

   + 查看commit日志记录

     > git log
     >
     > git log --pretty=oneline

   + 比较工作区文件和仓库文件差异

     > git diff [file]

   + 将暂存区或者某个commit点文件恢复到工作区

     > git checkout [commit]  --  [file]
     >
     > + --是为了防止误操作，checkout还有切换分支的作用

   + 

