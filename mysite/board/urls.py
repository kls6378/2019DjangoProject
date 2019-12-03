from django.urls import path
from board import views

app_name='board'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.create, name='create'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('<int:board_id>/update/', views.update, name='update'),
    path('<int:board_id>/delete/', views.delete, name='delete'),
    path('<int:comment_id>/cupdate/', views.cupdate, name='update'),
    path('<int:comment_id>/cdelete/', views.cdelete, name='delete'),
]