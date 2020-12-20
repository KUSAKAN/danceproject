from django.urls import path
from . import views

app_name = 'danceapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name = 'main'),
    path('search/', views.PostSearchList.as_view(), name='search'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('category/<int:pk>/', views.PostCategoryList.as_view(), name='category'),
    path('archive/<int:year>/', views.PostYearList.as_view(), name='year'),
    path('archive/<int:year>/<int:month>/', views.PostMonthList.as_view(), name='month'),
    #path('<int:post_id>/', views.post_detail, name="post_detail"),
]