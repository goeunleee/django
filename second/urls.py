"""second URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myapp.views
import static_practice_app.views
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import return_main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/',myapp.views.main,name = 'main'),
    path('myapp/google_move',myapp.views.google_move,name='google_move'),
    path('myapp/detail/<int:blog_id>',myapp.views.detail,name='detail')
    ,path('myapp/new/',myapp.views.new,name='new'),
    path('myapp/return_main', myapp.views.return_main, name='return_main'),
    path('myapp/renew/<int:blog_id>', myapp.views.renew, name='renew'),
    path('myapp/remove/<int:blog_id>', myapp.views.remove, name='remove'),
    path("",static_practice_app.views.index, name="index"),
    path("upload/",static_practice_app.views.upload,name='upload'),
    path("upload_result/", static_practice_app.views.upload_result, name='upload_result'),
    path("community/", static_practice_app.views.community, name="community"),
]

urlpatterns += static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
#사람들이 업로드 한 다음 미디어라는 파일이 붙음 상대측에서 미디어를 올린다는 것을 의미 
#settiong.media_Root에서 해당 파일을 가져와라 
