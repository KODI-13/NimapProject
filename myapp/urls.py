from django.urls import include, path

from myapp import views

urlpatterns = [
    path('', views.home),
    path('projects/<int:id>/', views.projects, name='projects'),
    path('registration/<int:id>/',views.registration,name='registration'),
    path('display/',views.display),
    path('update/<id>/',views.update),
    path('cupdate/<id>/',views.cupdate),
    path('delete/<id>/',views.delete),
    path('clogin/',views.clogin),
    path('new/',views.new),

    
]