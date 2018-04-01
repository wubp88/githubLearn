
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