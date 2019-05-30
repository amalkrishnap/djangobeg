from django.contrib import admin, auth
from django.urls import path
#import blog.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('blog/',blog.urls),
    #path('accounts/', auth_urls),
]
