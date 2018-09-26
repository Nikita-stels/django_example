from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.category_list, name='category_list'),
    url('category', views.category_page, name='category_page'),
    url('delete', views.del_category, name='delele')
]