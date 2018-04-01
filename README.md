# githubLearn

 ## 本地代码同步到远程git仓库
 
+ 1 设置git账号
 ```
 git config --global user.name "Your Name"
 git config --global user.email "email@example.com"
 ```
 
 + 2 提交到本地git仓库
 
  ```
 git init
 git add .
 git commit -m "注释语句"
 ```
 
 + 3 产生公钥和私钥，并且把公钥配置到远程的github仓库里面
 
 ```
 本地Git仓库和GitHub仓库之间的传输是通过SSH加密。
 ssh-keygen -t rsa -C "youremail@example.com"
 登陆GitHub，打开“Account settings”，“SSH Keys”页面，把id_rsa.pub内容粘贴进去：

 ```
 
+ 4 去github上创建自己的Repository，获取创建的仓库的https地址

+ 5 取消本地目录下原有关联的远程库
```
git remote remove origin
```
+ 6 本地目录下关联新的远程repository

```
git remote add origin https://github.com/hanhailong/CustomRatingBar
```

+ 7 上传代码到github远程仓库（上传github之前，要先pull一下）

```
git pull origin master
git push -u origin master
```


## git常见错误

+ 1  git pull 失败 ,提示：fatal: refusing to merge unrelated histories

```
git pull origin master --allow-unrelated-histories
```















