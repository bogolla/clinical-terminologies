"""demo_terms URL Configuration."""
from django.conf.urls import include, url


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),

    url(r'^rxnorm/', include('RxNorm.urls',
        namespace='rxnorm')),
]
