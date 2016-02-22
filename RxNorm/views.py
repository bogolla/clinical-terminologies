from rest_framework import viewsets
from .models import (
    Rxnatomarchive, Rxnconso, Rxncui, Rxncuichanges,
    Rxndoc, Rxnrel, Rxnsab, Rxnsat, Rxnsty
)
from .serializers import (
    RxnatomarchiveSerializer, RxnconsoSerializer, RxncuiSerializer,
    RxncuichangesSerializer, RxndocSerializer, RxnrelSerializer,
    RxnsabSerializer, RxnsatSerializer, RxnstySerializer
)


class RxnatomarchiveViewSet(viewsets.ModelViewSet):
    serializer_class = RxnatomarchiveSerializer
    queryset = Rxnatomarchive.objects.all()


class RxnconsoViewSet(viewsets.ModelViewSet):
    serializer_class = RxnconsoSerializer
    queryset = Rxnconso.objects.all()


class RxncuiViewSet(viewsets.ModelViewSet):
    serializer_class = RxncuiSerializer
    queryset = Rxncui.objects.all()


class RxncuichangesViewSet(viewsets.ModelViewSet):
    serializer_class = RxncuichangesSerializer
    queryset = Rxncuichanges.objects.all()


class RxndocViewSet(viewsets.ModelViewSet):
    serializer_class = RxndocSerializer
    queryset = Rxndoc.objects.all()


class RxnrelViewSet(viewsets.ModelViewSet):
    serializer_class = RxnrelSerializer
    queryset = Rxnrel.objects.all()


class RxnsabViewSet(viewsets.ModelViewSet):
    serializer_class = RxnsabSerializer
    queryset = Rxnsab.objects.all()


class RxnsatViewSet(viewsets.ModelViewSet):
    serializer_class = RxnsatSerializer
    queryset = Rxnsat.objects.all()


class RxnstyViewSet(viewsets.ModelViewSet):
    serializer_class = RxnstySerializer
    queryset = Rxnsty.objects.all()
