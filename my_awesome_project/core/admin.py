from django.contrib import admin

from .models import Goal, Journey, Session, Target, Task

# Register your models here.
admin.site.register(Journey)
admin.site.register(Goal)
admin.site.register(Target)
admin.site.register(Task)
admin.site.register(Session)
