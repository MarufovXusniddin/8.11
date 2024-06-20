from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Cost
from .serializers import CostSerializer


class UserCostsAPIView(generics.ListAPIView):
    serializer_class = CostSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Cost.objects.filter(user_id=user_id)


