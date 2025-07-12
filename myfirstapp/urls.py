from django.urls import path, include  # Importing path and include to define URL patterns
from . import views  # Importing views from the current application

urlpatterns = [
    path('', views.myfunctioncall,name="index"),  # URL pattern for the home view
    path('about',views.myfunctionabout,name='about'),
    path('add/<int:a>/<int:b>',views.add,name='about'),
    path('intro/<str:name>/<int:age>',views.intro, name="intro"),
    path('myfirstpage', views.myfirstpage, name='myfirstpage'),
    path('mysecondpage', views.mysecondpage, name='mysecondpage'),
    path('mythirdpage', views.mythirdpage, name='mythirddpage'),
    path('myimagepage', views.myimagepage, name='myimagepage'),
    path('myimagepage2', views.myimagepage2, name='myimagepage2'),
    path('myimagepage3', views.myimagepage3, name='myimagepage3'),
    path('myimagepage4', views.myimagepage4, name='myimagepage4'),
    path('myimagepage5/<str:imagename>', views.myimagepage5, name='myimagepage5'),
    path('myform', views.myform, name='myform'),
    path('submitmyform', views.submitmyform, name='submitmyform'),
    path('myform2', views.myform2, name='myform2'),
    





]
