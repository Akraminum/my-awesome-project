from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from my_awesome_project.core.api.views.goal_view import GoalViewSet
from my_awesome_project.core.api.views.Journey_view import JourneyViewSet
from my_awesome_project.core.api.views.session_view import SessionViewSet
from my_awesome_project.core.api.views.target_view import TargetViewSet
from my_awesome_project.core.api.views.task_view import TaskViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("journeys", JourneyViewSet, basename="journeys")
router.register("goals", GoalViewSet, basename="goals")
router.register("targets", TargetViewSet, basename="targets")
router.register("tasks", TaskViewSet, basename="tasks")
router.register("sessions", SessionViewSet, basename="sessions")

from my_awesome_project.web.views import JourneyViewSet as WebJourneyViewSet
from django.urls import path

urlpatterns = [
    path("web/", WebJourneyViewSet.as_view(), name="web"),
]
app_name = "api"
urlpatterns += router.urls
