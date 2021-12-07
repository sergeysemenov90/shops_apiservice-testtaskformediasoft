from django.contrib import admin
from django.urls import path, include
from shops import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('city/', views.CityListView.as_view()),
    path('city/<int:pk>/', views.CityDetailView.as_view()),
    path('street/', views.StreetListView.as_view()),
    path('shop/', views.ShopCreateView.as_view()),
    path('shop/<int:pk>', views.ShopDetailView.as_view()),

]
