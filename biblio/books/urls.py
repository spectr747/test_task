from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('addrec/', views.addrec, name='addrec'),
    # path('update/', views.update, name='update'),
    # path('books/', views.books_list, name='book_list'),
    # path('profile/', views.profile_edit, name='profile_edit')
]
