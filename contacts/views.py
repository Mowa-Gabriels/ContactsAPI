from .models import Contact
from .serializers import ContactSerializer
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated





@api_view(['GET'])
def APIOverview(request, format=None):
    
    return Response({

        'register': reverse('register', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'contact': reverse('contact-list', request=request, format=format),
        'swagger': reverse('schema-swagger-ui', request=request, format=format),
        'redoc': reverse('schema-redoc', request=request, format=format),
    })

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)
    


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = "pk"