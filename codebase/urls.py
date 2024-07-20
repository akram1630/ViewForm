from django.urls import path
from .views import Home, Create, Detail, Update, Delete

urlpatterns = [
    #pk means primary key
    path('', Home.as_view(), name='home'),
    path('create/', Create.as_view(), name='create'),
    path('detail/<int:pk>', Detail.as_view(), name='detail'),
    path('update/<int:pk>', Update.as_view(), name='update'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
]
