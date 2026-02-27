from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'name']
    search_fields = ['username', 'email', 'name']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'members']
    search_fields = ['name']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'activity_type', 'duration', 'date']
    search_fields = ['user', 'activity_type']
    list_filter = ['activity_type', 'date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'score']
    search_fields = ['user']
    ordering = ['-score']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']
