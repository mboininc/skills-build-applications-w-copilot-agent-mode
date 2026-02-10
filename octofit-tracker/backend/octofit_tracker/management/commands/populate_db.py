from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel')
        captain = User.objects.create(email='captain@marvel.com', name='Captain America', team='Marvel')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC')
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC')

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date='2026-02-09')
        Activity.objects.create(user=batman, type='Cycling', duration=45, date='2026-02-09')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        # Create workouts
        Workout.objects.create(name='Pushups', description='Upper body exercise', suggested_for='Marvel')
        Workout.objects.create(name='Squats', description='Lower body exercise', suggested_for='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
