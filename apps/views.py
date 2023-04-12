from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from apps.forms import ProductForm, PostForm
from apps.models import Product, Post


class ProductListPage(ListView):
    template_name = 'shop-list-left-sidebar.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('...')


class ProductPage(DeleteView):
    template_name = 'single-product.html'
    model = Product
    context_object_name = 'product'


class PostListPage(ListView):
    template_name = 'blog-list-left-sidebar.html'
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('...')


class PostPage(ListView):
    template_name = 'blog-details.html'
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('homepage')


class AddPostPage(CreateView):
    template_name = 'add_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_list')
