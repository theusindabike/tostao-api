from django.urls import path, include
from rest_framework import routers

from api.users.views import Users

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users', Users)

urlpatterns = [
    path('', include(router.urls))
]
