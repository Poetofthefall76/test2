from main.viewsets import UserProfileViewset, ProductViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('UserProfile', UserProfileViewset)
router.register('Product', ProductViewset)
