from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('form', views.form, name='form'),
	path('detail/<id>', views.detail, name='detail'),
	path('delete/<id>', views.delete, name='delete'),
	path('update/<id>', views.update, name='update'),
	# Login
	path('lhome/', views.home, name='home'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('signup/', views.signup, name='signup'),
]