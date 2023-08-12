from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView
from .serializers import BlogSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Blog
from .permissions import IsAuthorOrSuperUser
from rest_framework.authentication import TokenAuthentication


# Create your views here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)
        user = self.perform_create(serializer)
        token = Token.objects.create(user=user)
        return Response({'user': serializer.data, 'token': token.key}, status=status.HTTP_201_CREATED,)

    def perform_create(self, serializer):
        user = serializer.save()  # Save the user instance
        return user


class BlogsView(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    ordering_fields = ['title', 'author', 'created_at']
    search_fields = ['title', 'author', 'content']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Blog post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsAuthorOrSuperUser()]
        return super().get_permissions()
