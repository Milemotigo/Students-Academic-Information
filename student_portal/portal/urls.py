from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='portal', permanent=True)),
    path('test_portal/', views.test_portal, name='test_portal'),
    path('view_students_json/', views.all_students_json),
    # path('portal/', views.portal)
    path('base-html-view/', views.base_view),
    # path('home/', views.base_view, name='home'),
]