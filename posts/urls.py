#from django.db import router
from django.urls import path
from rest_framework.routers import SimpleRouter

#from .views import UserList, UserDetail, PostList, PostDetail
from .views import UserViewSet, PostViewset

# New simplified routing method
router = SimpleRouter()
router.register('users', UserViewSet)
router.register('', PostViewset)

urlpatterns = router.urls



## Old redundant way
#urlpatterns = [
#         path('users/', UserList.as_view()),
#         path('users/<int:pk>/', UserDetail.as_view()),
#         path('<int:pk>/', PostDetail.as_view()),
#         path('', PostList.as_view()),
#]
