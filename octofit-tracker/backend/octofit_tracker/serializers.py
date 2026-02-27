from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout


class UserSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['_id', 'id', 'username', 'email', 'name']

    def get__id(self, obj):
        return str(obj.pk)


class TeamSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ['_id', 'id', 'name', 'members']

    def get__id(self, obj):
        return str(obj.pk)


class ActivitySerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = ['_id', 'id', 'user', 'activity_type', 'duration', 'date']

    def get__id(self, obj):
        return str(obj.pk)


class LeaderboardSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['_id', 'id', 'user', 'score']

    def get__id(self, obj):
        return str(obj.pk)


class WorkoutSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['_id', 'id', 'name', 'description', 'exercises']

    def get__id(self, obj):
        return str(obj.pk)
