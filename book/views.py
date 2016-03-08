from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken import TokenAuthentication
from .models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    permissions_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Book.objects.all()
