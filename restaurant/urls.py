#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'menus', views.MenuViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', MenuItemsView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-item-detail'),
    path('api-token-auth/', obtain_auth_token),
]