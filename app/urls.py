from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$',views.dashboard),
    url(r'^send_msg/$',views.send_msg,name='chat_send_msg'),
    url(r'^get_msg/$',views.get_msg,name='get_new_msg'),
]
