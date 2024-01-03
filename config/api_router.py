from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from my_awesome_project.users.api.views import UsersViewSet
from my_awesome_project.core.api.views.Journey_view import JourneyViewSet
from my_awesome_project.core.api.views.goal_view import GoalViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()




router.register("journeys", JourneyViewSet, basename="journeys")
router.register("goals", GoalViewSet, basename="goals")


urlpatterns = []
app_name = "api"
urlpatterns = router.urls
