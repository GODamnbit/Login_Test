运行环境：python 3.7

依赖环境安装：
命令窗口切换到项目目录，执行pip install -r requirements.txt

项目执行：
命令窗下执行python app.py

接口测试：
项目运行后使用postman测试：
1. 登录测试：POST  127.0.0.1：5000/login
	header：json，键值对phone、password
	（ex：phone：123，password：123）

2. 注册测试：POST  127.0.0.1:5000/add
	header：json，键值对phone、user_name、(email)、password、(sex)
	（ex：phone：126，user_name：lala，password：w123，sex：男）
	ps：括号内参数可为空，sex：男/女

3. 发布测试：POST  127.0.0.1：5000/station
	header：json，键值对station_id
	（ex：station_id：101）
	ps：该文件含图片展示
