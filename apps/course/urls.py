from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start),
    url(r'^add_course', views.add),
    url(r'^delete/(?P<course_id>[0-9]+$)', views.delete),
    url(r'^actions', views.actions)
]
