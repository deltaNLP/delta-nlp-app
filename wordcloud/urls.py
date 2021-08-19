from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about, name='wordcloud.views.about'),
    url(r'^gsoc$', views.gsoc, name='wordcloud.views.gsoc'),
    url(r'^api/analyze$', views.analyze, name='wordcloud.views.analyze'),
    url(r'^visualize$', views.visualize_view, name='wordcloud.views.visualize_view')