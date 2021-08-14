from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from blog.models import Article
from .permissions import IsSuperUser, IsStaffOrReadOnly, IsAuthorOrReadOnly,IsSuperUserOrStaffOrReadOnly
from .serializers import ArticleSerializer, UserSerializer, AuthorSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


# Create your views here.
# class ArticleListView(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     # authentication_classes = (BasicAuthentication,)
#     permission_classes = (IsStaffOrReadOnly,)
#
#
# class ArticleDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     lookup_field = "pk"
#     permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)

class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['status', 'author__username', 'author']
    ordering_fields = ['publish', ]
    search_fields = ['author__username', 'author__first_name', 'author__last_name', 'title']

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Article.objects.all()
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #     return queryset

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            # permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
            permission_classes = [IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


# class UserListView(ListCreateAPIView):
#     # queryset = User.objects.all()
#     def get_queryset(self):
#         # print("-----------------------")
#         # print(self.request.user)
#         # print(self.request.auth)
#         # print("-----------------------")
#         return User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUserOrStaffOrReadOnly,)
#
#
# class UserDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperUserOrStaffOrReadOnly,)

class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrStaffOrReadOnly,)


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)
#
#     def delete(self, request):
#         request.auth.delete()
#         #return Response({"msg": "Token Revoked"})
#         return Response(status=204)

class AuthorRetrieve(RetrieveAPIView):
    queryset = get_user_model().objects.filter(is_staff=True)
    serializer_class = AuthorSerializer
