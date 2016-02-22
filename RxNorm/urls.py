from rest_framework import routers
from .views import (
    RxnatomarchiveViewSet, RxnconsoViewSet, RxncuiViewSet,
    RxncuichangesViewSet, RxndocViewSet, RxnrelViewSet,
    RxnsabViewSet, RxnsatViewSet, RxnstyViewSet
)

router = routers.SimpleRouter()
router.register(r'rxn_atom_archive', RxnatomarchiveViewSet)
router.register(r'rxn_conso', RxnconsoViewSet)
router.register(r'rxn_cui', RxncuiViewSet)
router.register(r'rxn_cuichanges', RxncuichangesViewSet)
router.register(r'rxn_doc', RxndocViewSet)
router.register(r'rxn_rel', RxnrelViewSet)
router.register(r'rxn_sab', RxnsabViewSet)
router.register(r'rxn_sat', RxnsatViewSet)
router.register(r'rxn_sty', RxnstyViewSet)

urlpatterns = router.urls
