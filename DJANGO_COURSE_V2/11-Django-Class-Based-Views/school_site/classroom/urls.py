from django.urls import path


from .views import (HomeView,ThankYouView, 
                    ContactFormView, TeacherCreateView,
                    TeacherListView,TeacherUpdateView,
                    TeacherDeleteView,TeacherDetailView)

app_name = 'classroom'

urlpatterns = [ 
    path('',HomeView.as_view(),name='home'), 
    path('contact/',ContactFormView.as_view(),name='contact'),
    path('thank_you/',ThankYouView.as_view(),name='thank_you'),
    path('create_teacher',TeacherCreateView.as_view(),name='create_teacher'),
    path('list_teacher/',TeacherListView.as_view(),name='list_teacher'),
    path('delete_teacher/<int:pk>/',TeacherDeleteView.as_view(),name="delete_teacher"),
    path('update_teacher/<int:pk>/',TeacherUpdateView.as_view(),name='update_teacher'),
    path("teacher/<int:pk>/",TeacherDetailView.as_view(),name='detail_teacher')
]