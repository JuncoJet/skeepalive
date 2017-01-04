# skeepalive
一个简单网页服务器/代理服务器存活检测程序，当服务失去响应后能够自动重启相关服务

如何使用
-
* Windows 下装 Python 环境后直接双击运行，程序开发使用标准库，无需安装其他第三方程序。用户可根据需求改写 skeepalive.py、killserver.bat、startserver.bat 的代码。
* Linux、BSD、OS X 下安装 Python 环境，可以输入以下命令运行`python skeepalive.py`，或者`chmod +x skeepalive.py`、`./skeepalive.py`执行。用户可根据需求改写 skeepalive.py、killserver.bat、startserver.bat 的代码。（你需要把bat改写成sh代码:-P）
