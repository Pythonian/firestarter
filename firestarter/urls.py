import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from crowdfunding import paypal, views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('questions/', views.questions, name='questions'),
    path('updates/', views.updates, name='updates'),
    path('c/choose', views.choose, name='choose'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

for x in os.listdir(os.path.join(settings.BASE_DIR, 'templates', 'pages')):
    urlpatterns += [
        path('p/'+x[:-5]+'/', views.page, {'pagename': x[:-5]})
    ]

# for x in settings.PAY_TYPES:
#     if 'CC' in x[0]:
#         urlpatterns += patterns('firestarter.cc_stripe',
#             url(r'^c/CC$', 'approve_payment', name='approve_payment'),
#             url(r'^c/CC/complete$', 'complete_payment', name='complete_payment'),
#         )
#     elif 'BC' in x[0]:
#         urlpatterns += patterns('firestarter.bitcoin',
#             url(r'^c/BC$', 'approve_payment', name='approve_payment'),
#             url(r'^c/BC/complete$', 'complete_payment', name='complete_payment'),
#         )
#     elif 'PP' in x[0]:
#         urlpatterns += patterns('firestarter.paypal',
#             url(r'^c/PP$', 'approve_payment', name='approve_payment'),
#             url(r'^c/PP/confirm$', 'handle_response', name='handle_response'),
#             url(r'^c/PP/complete$', 'complete_payment', name='complete_payment'),
#             url(r'^c/PP/cancel$', 'cancel', name='cancel')
#         )
