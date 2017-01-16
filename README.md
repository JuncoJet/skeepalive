# skeepalive
一个简单网页服务器/代理服务器存活检测程序，当服务失去响应后能够自动重启相关服务

##如何使用

skeepalive.py
-
* Windows 下装 Python 环境后直接双击运行，程序开发使用标准库，无需安装其他第三方程序。用户可根据需求改写 skeepalive.py、killserver.bat、startserver.bat 的代码。
* Linux、BSD、OS X ~~下安装 Python 环境~~默认已有Python 2.x，可以输入以下命令运行`python skeepalive.py`，或者`chmod +x skeepalive.py`、`./skeepalive.py`执行。用户可根据需求改写 skeepalive.py、killserver.bat、startserver.bat 的代码。（你需要把bat改写成sh代码:-P）。

skeepalivex.py
-
* `skeepalivex.py` 是在原有基础上新增开发了带负载均衡的存活检测程序，能够在服务器检测失败之后自动切换到其他镜像服务器，使用方法类似上面。
* 需要先安装bottle库，可以用`easy_install bottle`或者 `pip install bottle`来进行安装。
* 启动本程序后会创建一个简易的服务器，可以通过 [http://127.0.0.1:8080/pac](http://127.0.0.1:8080/pac) 来获取负载均衡的pac文件。

##更新日志
* 2017-1-16 17:08:57 加入负载均衡模块，当服务器挂掉时可以自动切换服务器地址（初步实现基本功能、尚不完善）
* 2017-1-5 09:47:42 增加 Linux 支持，调整配置参数，之前的检测过于激进
* 2017-1-5 08:57:25 更新 OS X 支持，修正一处BUG