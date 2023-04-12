from django.urls import path
from apps.views import ProductListPage, ProductPage, PostListPage, PostPage, AddPostPage
from core import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ProductListPage.as_view(), name='product_list'),
    path('product/<int:pk>', ProductPage.as_view(), name='product'),
    path('post_list', PostListPage.as_view(), name='post_list'),
    path('post/<int:pk>', PostPage.as_view(), name='post'),
    path('add_post', AddPostPage.as_view(), name='add_post')

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

