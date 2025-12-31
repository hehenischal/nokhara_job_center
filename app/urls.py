from django.urls import path
from .views import home,register,detail,faq


urlpatterns = [
    path('', home, name='home'),
  path("register/", register, name="register"),
  path("detail/",detail,name="detail"),
  path("faq/",faq,name="faq")
  
]