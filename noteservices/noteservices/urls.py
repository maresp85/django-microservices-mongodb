from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(('notes.urls', 'v1'), namespace='v1')),
]
