from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register('todos', views.TodoViewSet, basename='todos')

urlpatterns = router.urls
