from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BlogsView, RegisterView
router = DefaultRouter()
router.register(r'blog', BlogsView, basename='blogs')

# urlpatterns = router.urls
urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', obtain_auth_token, name='obtain token')
]
