## Django项目介绍
pip install django
pip install Serializer 自定义响应
pip install Response
pip install djangorestframework
pip install loguru

### 工程目录
+ component
    + CustomResponse 自定义响应数据组件
+ djangoProject   与项目名同名目录，全局配置
    + setting.py   全局配置文件
    + urls.py      全局路由【*】--html页面
    + wsgi.py      wsgi服务器配置
+ requirement 模块名称
    + migrations  数据库变更相关记录 不要删、不要改
    + admin.py    后台管理
    + apps.py     app的相关配置
    + models.py   数据库相关【*】
    + tests.py     测试函数
    + view.py     视图函数【*】 
+ static 静态文件，需要在setting中配置
+ templates   模板文件，html 【*】
+ manage.py   启动项目，创建app、各种命令操作
+ venv 虚拟环境

### 创建app、注册app、创建请求【views】、配置路由
**创建app:**
```shell
python manage.py startapp app_name
```

**启动项目**
```shell
python manage.py runserver
```
    
### 错误处理

静态文件404错误,app.setting 添加配置
```python
import os
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    )
```


### 项目打包

打包exe
    PyInstaller是一个跨平台的Python应用打包工具  
        安装：pip install Pyinstaller   
        或者  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple Pyinstaller  
    准备：fac.ico 程序的图标   tree.py 是python文件  
        pyinstaller -F -i ./fac.ico tree.py    #  切换到项目目录再执行打包命令  
    dist目录就是我们打包好的地方  