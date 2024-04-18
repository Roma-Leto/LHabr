from django.contrib import admin
from django.urls import path, include
from LHabrApp.views import good_morning, index_blog, index, create_post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('good_morning/', good_morning, name='g_morming'),
    path('blog/', index_blog, name='blog_pg'),
    path('create/', create_post, name='create_post'),

    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


