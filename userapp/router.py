from user.viewsets import UserViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('user', UserViewset, basename='users')
