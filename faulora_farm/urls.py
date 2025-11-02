from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from products.views import home  # ✅ import the home view
from products.views import about 
from django.views.static import serve

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('accounts/', include('accounts.urls')),  # register view
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    path('about/', about, name='about'),  # Add this line
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
