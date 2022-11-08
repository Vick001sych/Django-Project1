from rest_framework import routers, serializers, viewsets
from .models import Book
from .serializer import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

router = routers.DefaultRouter()
router.register(r'book/list', BookViewSet)