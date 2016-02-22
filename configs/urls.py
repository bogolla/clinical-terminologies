"""demo_terms URL Configuration."""
from django.conf.urls import include, url
# from django.conf import settings


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),

    url(r'^rxnorm/', include('RxNorm.urls',
        namespace='rxnorm')),

    # url(r'^static/(?P.*)$', 'django.views.static.serve',
    #     {'document_root': settings.STATIC_ROOT})
]
