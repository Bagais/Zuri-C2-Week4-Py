from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'All Artistes', views.ArtisteViewSet)
router.register(r'All Songs', views.SongViewSet)
router.register(r'All Lyrics', views.LyricViewSet)


urlpatterns = [
	# path('', views.index, name='index'),
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]