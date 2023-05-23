
from django.contrib import admin
from django.urls import path,include

# 导入视图模块
from service import views as service
from component import views as api
from component import tests as api_test


urlpatterns = [
    path('admin/', admin.site.urls),
    # component模块路由
    path('test/apiResponse',api_test.testApiResponse),

    # service 模块路由
    path('', service.index),
    path('login/', service.login),



]
