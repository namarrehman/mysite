
from django.conf.urls import url
from . import views
app_name = 'blog'
## above line is updated as per "https://stackoverflow.com/questions/48178196/include-got-an-unexpected-keyword-argument-app-name"
urlpatterns = [
    #    post views

    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
           r'(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
]
