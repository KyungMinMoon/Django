from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('board.urls')),
    # /articles/1/
    # /articles/
    # /articles/create/
]
