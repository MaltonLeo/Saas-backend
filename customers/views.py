from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        tenant_id = self.request.query_params.get('tenant')
        if tenant_id:
            return Customer.objects.filter(tenant_id=tenant_id)
        return Customer.objects.all()

