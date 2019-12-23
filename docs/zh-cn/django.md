# 新建一个Django项目

打开项目文件夹
```
django-admin startproject jjnz  //新建一个项目（绞尽脑汁）
cd jjnz
python manage.py runserver  //打开本地服务器 127.0.0.1：8000
// Ctrl + c 停止服务器

python manage.py startapp blog  //新建一个应用 自动创造一个文件夹

python manage.py makemigrations //告知改变

python manage.py migrate //做出改变，创建数据表

python manage.py createsuperuser //新增用户
```

文件夹的作用
```
C:.
│  db.sqlite3  //数据库
│  manage.py  // runserver/
│  README.md
├─blog   //blog
│  │  admin.py
│  │  apps.py
│  │  models.py  //定义blog这个app中的元素类型
│  │  tests.py
│  │  urls.py  //定位blog中url
│  │  views.py
│  │  __init__.py
│  │···
|
├─jjnz         //init jjnz
│  │  asgi.py
│  │  settings.py
│  │  urls.py     //  url先定位到此
│  │  wsgi.py
│  │  __init__.py

└─templates
    │  base.html
    │
    └─blog
            detail.html
            index.html
```