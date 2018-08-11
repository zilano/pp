from django.conf.urls import url
from . import views
#urlpatterns = [
#    path('', views.index, name='index'),
#]
urlpatterns=[
    url(r'^submit/expense/$', views.submit_expense, name='submit_expense')
]
