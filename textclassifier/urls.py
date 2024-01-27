from django.urls import path
from .views import HomeView, CategoryListView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("category/<int:pk>/", CategoryListView.as_view(), name="category_detail"),
]
