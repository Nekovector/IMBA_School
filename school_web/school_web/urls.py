from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('courses/', include('courses.urls')),
    path('account/', include('myAccount.urls'))
]
