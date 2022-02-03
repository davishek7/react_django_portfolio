from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('',views.get_all_projects,name='get_all_projects'),
    path('contact-view/',views.contact_view,name='contact_view'),
]
