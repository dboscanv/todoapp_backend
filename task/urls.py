from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as auth_views

from task import views

urlpatterns = [
    url(r'^tasks/(?P<pk>[0-9]+)', views.TaskView.as_view()),
    url(r'^tasks/', views.TaskView.as_view()),
    url(r'^users/$', views.UserView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)', views.UserDetailView.as_view()),
    url(r'^users_task/$', views.UserTaskView.as_view()),
    url(r'^login/$', auth_views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
