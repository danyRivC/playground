from django.urls import path
from .views import HomeView, SamplePageView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
]