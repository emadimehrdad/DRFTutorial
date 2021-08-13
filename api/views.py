from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Article
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly,IsSuperUserOrStaffOrReadOnly
from .serializers import ArticleSerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


# Create your views here.
class ArticleListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # authentication_classes = (BasicAuthentication,)
    permission_classes = (IsStaffOrReadOnly,)


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = "pk"
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class UserListView(ListCreateAPIView):
    # queryset = User.objects.all()
    def get_queryset(self):
        # print("-----------------------")
        # print(self.request.user)
        # print(self.request.auth)
        # print("-----------------------")
        return User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffOrReadOnly,)


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffOrReadOnly,)


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def delete(self, request):
#         request.auth.delete()
#         #return Response({"msg": "Token Revoked"})
#         return Response(status=204)
