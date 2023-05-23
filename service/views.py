from django.shortcuts import render

# 设置主页
def index(request):
    # 2.返回request, 返回登入界面
    return render(request, 'index.html')

# 接收request参数
def login(request):
    # 2.返回request, 返回登入界面
    return render(request, 'login.html')

