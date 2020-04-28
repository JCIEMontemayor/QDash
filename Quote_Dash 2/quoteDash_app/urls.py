from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('Logout', views.logout),
    path('back', views.back),
    path('Quote', views.quote),
    path('like/<int:id>', views.likeQ),
    path('delete/<int:id>', views.deleteQ),
    path('my_quotes/<int:id>', views.profile),
    path('editPRO', views.editPRO),
    path('edit/<int:id>', views.edit),
    path('edit', views.editForm)
]