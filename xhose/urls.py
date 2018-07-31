from django.conf.urls import url
from xhose import views

app_name = 'xhose'

urlpatterns = [
    url(r'^xhose/', views.xhose, name='xhose'),
    # url(r'^contacts/$', views.contacts, name='contacts'),
]