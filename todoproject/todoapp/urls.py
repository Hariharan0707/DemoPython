from . import views
from django.urls import path

from todoapp import admin

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('tlvhome/',views.Tasklistview.as_view(),name='tlvhome'),
    path('tdvdetail/<int:pk>/',views.TaskDetailview.as_view(),name='tdvdetail'),
    path('tuvupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='tuvupdate'),
    path('tdvdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='tdvdelete')
]