import imp
from pipes import Template
from re import template
from django.urls import path
from .views import (
    CourseView,
    CourseListView,
    # MyListView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
)


app_name = 'courses'
urlpatterns = [
    # path('', CourseView.as_view(template_name='contact.html'), name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name = 'courses-detail'),
    path('', CourseListView.as_view(), name='courses-list'),
    # path('', MyListView.as_view(), name='courses-list'),# just to show inheretance
    path('create/', CourseCreateView.as_view(), name='courses-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name = 'courses-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name = 'courses-delete'),

#     path('create/', product_create_view, name='product-list'),
#     path('<int:id>/', product_detail_view, name = 'product-detail'),

#     path('<int:id>/delete/', product_delete_view, name = 'product-delete'),
]

