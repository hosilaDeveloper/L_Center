from django.urls import path
from .views import teachers_detail_view, teachers_list_view, home_view, courselist_view, course_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('course_list/', courselist_view, name='course_list'),
    path('teachers/', teachers_list_view, name='teacher_list'),
    path('courselist/<int:pk>/', course_detail_view, name='course-detail'),
    path('teachers/<int:pk>', teachers_detail_view, name='teachers_detail'),
]
