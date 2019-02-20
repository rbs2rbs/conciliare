from django.conf.urls import url
from paginas import views

urlpatterns = [
    url(r'^$',views.inicial),
    url("suces",views.email_suces)
]
