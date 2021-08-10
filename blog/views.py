from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from .models import Article


class ArticleList(ListView):
    context_object_name = "articles"

    def get_queryset(self):
        return Article.objects.filter(status=True)


class ArticleDetail(DetailView):
    context_object_name = "article"

    def get_object(self):
        return get_object_or_404(
            Article.objects.filter(status=True),
            pk=self.kwargs.get("pk"),
            )
