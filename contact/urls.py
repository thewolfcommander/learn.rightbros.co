from django.urls import path
from contact.views import (
    home,
    enroll,
    social,
    thanks,
    failed,
)

app_name = 'contact'

urlpatterns = [
    path('', home, name='home'),
    path('enroll/step-1/', enroll, name='enroll'),
    path('enroll/step-2/', social, name='social'),
    path('enroll/success/waiting/', thanks, name='thanks'),
    path('enroll/failed/', failed, name='failed'),
]