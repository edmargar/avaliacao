from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'chamadosv'

router = routers.SimpleRouter(trailing_slash=False)
router.register('responsavel_tecnico', views.ResponsavelTecnicoView, basename='responsavel_tecnico')
router.register('chamados', views.ChamadoView, basename='chamados')
urlpatterns = format_suffix_patterns(router.urls)
