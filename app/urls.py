from django.urls import path
from .views import UserCostsAPIView

urlpatterns = [
    path('costs/', UserCostsAPIView.as_view())
]