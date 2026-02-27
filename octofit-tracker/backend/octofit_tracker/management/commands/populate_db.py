from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Cleared existing data.')

        # Create users - superheroes
        users = [
            User(username='ironman', email='tony@starkindustries.com', name='Tony Stark'),
            User(username='spiderman', email='peter@dailybugle.com', name='Peter Parker'),
            User(username='blackwidow', email='natasha@shield.gov', name='Natasha Romanoff'),
            User(username='superman', email='clark@dailyplanet.com', name='Clark Kent'),
            User(username='batman', email='bruce@wayneenterprises.com', name='Bruce Wayne'),
            User(username='wonderwoman', email='diana@themyscira.com', name='Diana Prince'),
        ]
        for user in users:
            user.save()
        self.stdout.write('Users created.')

        # Create teams - Marvel and DC
        team_marvel = Team(
            name='Team Marvel',
            members=['ironman', 'spiderman', 'blackwidow'],
        )
        team_marvel.save()

        team_dc = Team(
            name='Team DC',
            members=['superman', 'batman', 'wonderwoman'],
        )
        team_dc.save()
        self.stdout.write('Teams created.')

        # Create activities
        activities = [
            Activity(user='ironman', activity_type='Flight Training', duration='60 minutes', date=date(2024, 1, 10)),
            Activity(user='spiderman', activity_type='Web Swinging', duration='45 minutes', date=date(2024, 1, 11)),
            Activity(user='blackwidow', activity_type='Combat Training', duration='90 minutes', date=date(2024, 1, 12)),
            Activity(user='superman', activity_type='Flying', duration='30 minutes', date=date(2024, 1, 10)),
            Activity(user='batman', activity_type='Martial Arts', duration='120 minutes', date=date(2024, 1, 11)),
            Activity(user='wonderwoman', activity_type='Sparring', duration='75 minutes', date=date(2024, 1, 12)),
        ]
        for activity in activities:
            activity.save()
        self.stdout.write('Activities created.')

        # Create leaderboard
        leaderboard_entries = [
            Leaderboard(user='ironman', score=9500),
            Leaderboard(user='spiderman', score=8700),
            Leaderboard(user='blackwidow', score=8200),
            Leaderboard(user='superman', score=9800),
            Leaderboard(user='batman', score=9100),
            Leaderboard(user='wonderwoman', score=9300),
        ]
        for entry in leaderboard_entries:
            entry.save()
        self.stdout.write('Leaderboard created.')

        # Create workouts
        workouts = [
            Workout(
                name='Avengers Endurance',
                description='A high-intensity endurance workout inspired by the Avengers.',
                exercises=['Running 5km', 'Push-ups 3x20', 'Pull-ups 3x10', 'Plank 3x60s'],
            ),
            Workout(
                name='Gotham Knight Strength',
                description='Strength training program used by Gotham\'s Dark Knight.',
                exercises=['Bench Press 4x8', 'Deadlift 4x6', 'Squat 4x8', 'Overhead Press 4x8'],
            ),
            Workout(
                name='Web Warrior Agility',
                description='Agility and flexibility training for the friendly neighborhood hero.',
                exercises=['Box Jumps 3x12', 'Lateral Shuffles 3x20m', 'Yoga Flow 20min', 'Balance Board 3x2min'],
            ),
        ]
        for workout in workouts:
            workout.save()
        self.stdout.write('Workouts created.')

        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db with test data!'))
