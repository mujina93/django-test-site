from django.urls import include, path
from django.contrib import admin

from . import views

app_name = 'polls' # all urls below are namespaced to the 'polls' app. You can refer to them in templates with {% url 'namespace:name' caught_variables %}
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
