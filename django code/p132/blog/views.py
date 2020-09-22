from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView
from django.http import Http404

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 1

    # def get_context_data(self, **kwargs):
    #     try:
    #         context = super(PostListView, self).get_context_data(**kwargs)
    #         return context
    #     except Http404:
    #         self.kwargs['page'] = 1
    #         context = super(PostListView, self).get_context_data(**kwargs)
    #         return context

    def paginate_queryset(self, queryset, page_size):
        try:
            context = super(PostListView,
                            self).paginate_queryset(queryset, page_size)
            return context
        except Http404:
            self.kwargs['page'] = 1
            context = super(PostListView,
                            self).paginate_queryset(queryset, page_size)
            return context


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post.html"
