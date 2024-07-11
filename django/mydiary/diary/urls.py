from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('calendar/', views.calendar, name='calendar'),
    path('new/', views.new_entry, name='new_entry'),
    path('search/', views.search, name='search'),
    path('diary/', views.diary_list, name='diary_list'),
    path('diary/<int:pk>/', views.diary_detail, name='diary_detail'),
    path('diary/<int:pk>/delete/', views.diary_delete, name='diary_delete'),
    path('edit/<int:pk>/', views.edit_entry, name='edit_entry'),
    path('save_memo/', views.save_memo, name='save_memo'),
]

