from django.contrib import admin
from apps.models import Post, Product, Category, ProductCommentary, PostCommentary


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'category', 'image')
    fields = ('name', 'price', 'description', 'category', 'image')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    fields = ('title', 'description', 'image')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ('name', )


@admin.register(ProductCommentary)
class ProductCommentaryAdmin(admin.ModelAdmin):
    list_display = ('description', 'product')
    fields = ('description', 'product')


@admin.register(PostCommentary)
class PostCommentaryAdmin(admin.ModelAdmin):
    list_display = ('description', 'post')
    fields = ('description', 'post')
