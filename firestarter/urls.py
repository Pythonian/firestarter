import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from crowdfunding import views, cc_stripe


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pledge/', cc_stripe.approve_payment, name='approve_payment'),
    path('pledge/successful/', cc_stripe.complete_payment, name='complete_payment'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
