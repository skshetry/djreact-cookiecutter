from django.conf.urls import url

from .views import MessageView

urlpatterns = [
     url(r'^echo', MessageView.as_view(), name="echo_message"),
]