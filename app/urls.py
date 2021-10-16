from django.conf.urls import url 
from app import views 
 
urlpatterns = [ 
    url(r'^api/app$', views.student_list),
    url(r'^api/app/(?P<pk>[0-9]+)$', views.student_detail),
]