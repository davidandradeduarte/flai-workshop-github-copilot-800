from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            username='ironman',
            email='tony@starkindustries.com',
            name='Tony Stark',
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_list_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self):
        response = self.client.get(f'/api/users/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'ironman')

    def test_create_user(self):
        data = {'username': 'spiderman', 'email': 'peter@dailybugle.com', 'name': 'Peter Parker'}
        response = self.client.post('/api/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TeamAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(
            name='Team Marvel',
            members=['ironman', 'spiderman'],
        )

    def tearDown(self):
        Team.objects.all().delete()

    def test_list_teams(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_team_detail(self):
        response = self.client.get(f'/api/teams/{self.team.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Team Marvel')

    def test_create_team(self):
        data = {'name': 'Team DC', 'members': ['superman', 'batman']}
        response = self.client.post('/api/teams/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.activity = Activity.objects.create(
            user='ironman',
            activity_type='Flight Training',
            duration='60 minutes',
            date=date(2024, 1, 10),
        )

    def tearDown(self):
        Activity.objects.all().delete()

    def test_list_activities(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_activity_detail(self):
        response = self.client.get(f'/api/activities/{self.activity.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'ironman')

    def test_create_activity(self):
        data = {
            'user': 'spiderman',
            'activity_type': 'Web Swinging',
            'duration': '45 minutes',
            'date': '2024-01-11',
        }
        response = self.client.post('/api/activities/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LeaderboardAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.entry = Leaderboard.objects.create(user='ironman', score=9500)

    def tearDown(self):
        Leaderboard.objects.all().delete()

    def test_list_leaderboard(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_leaderboard_entry(self):
        response = self.client.get(f'/api/leaderboard/{self.entry.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'ironman')
        self.assertEqual(response.data['score'], 9500)

    def test_create_leaderboard_entry(self):
        data = {'user': 'superman', 'score': 9800}
        response = self.client.post('/api/leaderboard/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class WorkoutAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(
            name='Avengers Endurance',
            description='High-intensity endurance workout.',
            exercises=['Running 5km', 'Push-ups 3x20'],
        )

    def tearDown(self):
        Workout.objects.all().delete()

    def test_list_workouts(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_workout_detail(self):
        response = self.client.get(f'/api/workouts/{self.workout.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Avengers Endurance')

    def test_create_workout(self):
        data = {
            'name': 'Gotham Knight Strength',
            'description': 'Strength training for the Dark Knight.',
            'exercises': ['Bench Press 4x8', 'Deadlift 4x6'],
        }
        response = self.client.post('/api/workouts/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class APIRootTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_root_at_slash(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)

    def test_api_root_at_api(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
