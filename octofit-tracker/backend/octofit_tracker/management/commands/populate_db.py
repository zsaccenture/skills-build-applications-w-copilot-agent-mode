from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        from octofit_tracker.models import User
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(email='ironman@marvel.com', name='Iron Man', team='Marvel')
        captain = User.objects.create(email='cap@marvel.com', name='Captain America', team='Marvel')
        batman = User.objects.create(email='batman@dc.com', name='Batman', team='DC')
        superman = User.objects.create(email='superman@dc.com', name='Superman', team='DC')

        # Create activities
        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2025-11-01')
        Activity.objects.create(user='Captain America', type='cycle', duration=45, date='2025-11-02')
        Activity.objects.create(user='Batman', type='swim', duration=60, date='2025-11-03')
        Activity.objects.create(user='Superman', type='run', duration=50, date='2025-11-04')

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', difficulty='Hard')
        Workout.objects.create(name='Power Lift', description='Strength for super heroes', difficulty='Medium')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))

           self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
