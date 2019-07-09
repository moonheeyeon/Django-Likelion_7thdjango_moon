from django.contrib import admin
from django.urls import path, include
import viewcrud.urls
import viewcrud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewcrud.views.welcome, name="welcome"),
    path('viewcrud/', include(viewcrud.urls)),
    path('viewcrud/', include(viewcrud.urls)),
    path('signup/', viewcrud.views.signup, name='signup'),
    path('login/', viewcrud.views.login, name='login'),
    path('logout/', viewcrud.views.logout, name='logout'),
]
