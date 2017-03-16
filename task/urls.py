from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as auth_views

from task import views

urlpatterns = [
    url(r'^tasks/(?P<pk>[0-9]+)', views.TaskView.as_view(), name="tasks"),
    url(r'^tasks/', views.TaskView.as_view(), name="post_tasks"),
    url(r'^users/$', views.UserView.as_view(), name="users"),
    url(r'^users/(?P<pk>[0-9]+)', views.UserDetailView.as_view(), name="users_detail"),
    url(r'^users_task/$', views.UserTaskView.as_view(), name="users_task"),
    url(r'^login/$', auth_views.obtain_auth_token, name="login"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
