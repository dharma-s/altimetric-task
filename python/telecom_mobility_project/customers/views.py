from rest_framework import viewsets
from .models import Plan
from accounts.models import CustomUser
from .serializers import PlanSerializer, CustomerSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomerSerializer

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


# customers/views.py
@api_view(['POST'])
def select_plan(request):
    customer_id = request.data.get('customer_id')
    plan_id = request.data.get('plan_id')
    # Logic to assign the selected plan to the customer

@api_view(['POST'])
def upgrade_plan(request):
    customer_id = request.data.get('customer_id')
    new_plan_id = request.data.get('new_plan_id')
    # Logic to upgrade the customer's plan


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
