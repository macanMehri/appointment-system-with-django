from django.urls import path
from .views import landing_page, login_page, sign_up_page


urlpatterns = [
    path('', landing_page),
    path('login/', login_page),
    path('signup/', sign_up_page),
]