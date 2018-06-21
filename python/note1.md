
##知识点积累

### 读取配置文件
ini结尾的配置文件如下
  ```
[info]
email = xxxx@163.com
password = xxxx

[cookies]
q_c1 =
cap_id =
_za =
__utmt =
__utma =
__utmb =
__utmc =
__utmz =
__utmv =
z_c0 =
unlock_ticket = 
 ```
 

   ```
    import ConfigParser
    cf = ConfigParser.ConfigParser()
    cf.read('config.ini')
    cookies = cf.items('cookies')
    cookies = dict(cookies)
    from pprint import pprint
    pprint(cookies)
    email = cf.get('info', 'email')
    password = cf.get('info', 'password')
 ```

 ### 查找python默认路径


Mac在启动，会先加载系统配置文件(包括~/.bash_profile )，所有默认的命令的路径，将会配配置文件（比如：~/.bash_profile）中的路径覆盖，并且，是后面覆盖前面的路径：例如，在终端输入“python”，系统会在配置文件中的路径查找，一直到找到位置（在配置文件中从后向前找）。
$PATH是查找路径，你在bash输入 echo $PATH
