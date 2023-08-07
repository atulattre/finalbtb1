from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
    path('',views.loginpage,name='loginpage'),
    path('homepage',views.homepage,name='homepage'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('cp',views.cp,name='cp'),
    path('all_flat',views.all_flat,name='all_flat'),#cp=complete profile
    path('contact/<int:id>/',views.contact,name='contact'),
    path('newhomepage',views.newhomepage,name='newhomepage'),
    path('newhomepage1',views.newhomepage1,name='newhomepage1'),
    
    path('userlogout',views.userlogout,name='userlogout'),
    path('post',views.post,name='post'),
    path('post1',views.post1,name='post1'),
    path('useredit1/<int:id>/',views.useredit1,name='useredit1'),
    path('delpost1/<int:id>/',views.delpost1,name='delpost1'),
    path('view11/<int:id>/',views.view11,name='view11'),
    path('notify1',views.notify1,name='notify1'),
    path('loginpage1',views.loginpage1,name='loginpage1'),


    



   
   
  
   



    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)