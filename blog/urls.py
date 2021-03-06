from django.urls import path, re_path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostLV.as_view(), name='index'),
    path('post/', views.PostLV.as_view(), name='post_list'),
    path('post/<int:pk>', views.PostDV.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/create', views.comment_write_view, name="comment_new"),
    path('post/<int:pk>/comment/delete', views.comment_delete_view, name = "comment_delete"),
    path('post/<int:pk>/comment/modify', views.comment_modify_view, name="comment_modify"),
   

    path('archive/', views.PostAV.as_view(), name='post_archive'),
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'),
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'),
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'),
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'),

    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),

    path('like/', views.post_like, name='post_like'),

    path('search/', views.SearchFormView.as_view(), name="search"),

    path('add/', views.PostCreateView.as_view(), name="add"),
    
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name="delete"),
]