from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from blog.models import Article


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "last_name", "first_name"]


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    # --------- Using model to represent author name ---------- #
    # author = AuthorSerializer()

    # --------- Hyperlink method to represent author  ---------- #
    # author = serializers.HyperlinkedIdentityField(view_name='api:authors-detail')

    # --------- Using fields to represent author name ---------- #
    # author = serializers.CharField(source="author.username", read_only=True)

    # --------- Using SerializeMethodField to represent author name ---------- #
    def get_author(self, obj):
        return {
            "username": obj.author.username,
            "email": obj.author.email
        }
    author = serializers.SerializerMethodField("get_author")

    class Meta:
        model = Article
        # fields = ("title", "slug", "author", "content", "publish", "status")
        # exclude = ("created", "updated")
        fields = "__all__"

    def validate_title(self, value):
        filter_list = ["content", "test"]

        for i in filter_list:
            if i in value:
                raise serializers.ValidationError("Don't use this!: {}".format(i))
        return value


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model
        fields = "__all__"

