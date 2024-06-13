1、CMD打开，输入以下命令，进入MYSQL数据库
mysql -h localhost -u root -p 数据库名
mysql -h localhost -u root -p wxdb

2、建号Model后，终端运行以下两条命令，数据库创建该表
python manage.py makemigrations
python manage.py migrate

3、运行服务命令，终端执行
python manage.py runserver 0.0.0.0:8000



INSERT INTO wxs_mymsg (adminID, userID,date,title,content,state) VALUES (1, 8,'2024-5-15','报修成功通知','您的维修申请已提报，请按照维修人员联系地址，邮寄器材进行维修','未读');
SELECT * FROM wxs_mymsg;
SELECT * FROM wxs_userinfo;
