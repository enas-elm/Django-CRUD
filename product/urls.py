from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'product'
urlpatterns = [
    # product/
    path('', views.index, name='index'),
    # product/create/
    path('create/', views.create, name='create'),

    path('show/<int:id>/', views.show, name='show'),

    path('update/<int:id>/', views.update, name='update'),

    path('delete/<int:id>/', views.delete, name='delete')
]

urlpatterns += staticfiles_urlpatterns()
