from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from my_awesome_project.users.api.views import UsersViewSet
from my_awesome_project.core.api.views.Journey_view import JourneyViewSet
from my_awesome_project.core.api.views.goal_view import GoalViewSet
from my_awesome_project.core.api.views.target_view import TargetViewSet
from my_awesome_project.core.api.views.task_view import TaskViewSet
from my_awesome_project.core.api.views.session_view import SessionViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

goals_patterns = r"journeys/(?P<journey_id>\d+)/goals"
targets_patterns = goals_patterns + r"/(?P<goal_id>\d+)/targets"
tasks_patterns = targets_patterns + r"/(?P<target_id>\d+)/tasks"
sessions_patterns = tasks_patterns + r"/(?P<task_id>\d+)/sessions"

router.register("journeys", JourneyViewSet, basename="journeys")

# /journeys/journey_id/goals
# router.register( goals_patterns , GoalViewSet, basename="journey-goals")
router.register("goals", GoalViewSet, basename="goals")

# router.register( targets_patterns , TargetViewSet, basename="goal-targets")
router.register("targets", TargetViewSet, basename="targets")

router.register( r"targets/(?P<target_id>\d+)/tasks" , TaskViewSet, basename="target-tasks")
# router.register("tasks", TaskViewSet, basename="tasks")

# /tasks/task_id/sessions
router.register(r"targets/(?P<target_id>\d+)/sessions", SessionViewSet, basename="task-sessions")
# router.register("sessions", SessionViewSet, basename="sessions")


urlpatterns = []
app_name = "api"
urlpatterns = router.urls
