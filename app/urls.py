from django.urls import path,include
from .views import *


urlpatterns = [
  path('accounts/', include('allauth.urls')),
  path('', home, name='home'),
  path("register/", register, name="register"),
  path('detail/<int:job_id>/', detail, name='detail'),  
  path("faq/",faq,name="faq"),
  path("register/",register,name="register"),
  path("login_view/",login_view,name='login'),
  path("search/",search,name='search'),
  path("post_job",post_job,name='post_job'),
  path('category/<slug:category_slug>/', category_detail, name='category_detail'),
  path("logout_view",logout_view,name="logout_view")
  
]