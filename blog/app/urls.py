from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('post/<int:pk>',views.post,name='post'),
    path('post/update',views.update,name='update'),
    path('post/delete',views.delete,name='delete')
]
