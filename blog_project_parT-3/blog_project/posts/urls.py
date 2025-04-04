from django.urls import path
from . import views
urlpatterns = [
    # path('add/',views.add_post,name='add_post'),
    path('add/',views.AddPostCreateView.as_view(),name='add_post'),
    # path('edit/<int:id>',views.edit_post,name='edit_post'),
    path('edit/<int:id>/',views.EditPostUpdateView.as_view(),name='edit_post'),
    # path('delete/<int:id>',views.delete_post,name='delete_post'),
    path('delete/<int:id>/',views.DeletePostDeleteView.as_view(),name='delete_post'),
    path('detail/<int:id>/',views.PostDetailView.as_view(),name='detail_post'),
    path('read/<int:id>',views.read_post,name='read_post'),
]
