from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
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
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team='Marvel')
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team='Marvel')
        batman = User.objects.create(name='Batman', email='batman@dc.com', team='DC')
        superman = User.objects.create(name='Superman', email='superman@dc.com', team='DC')

        # Create activities
        Activity.objects.create(user='Iron Man', type='Run', duration=30, date='2025-11-24')
        Activity.objects.create(user='Captain America', type='Swim', duration=45, date='2025-11-24')
        Activity.objects.create(user='Batman', type='Bike', duration=60, date='2025-11-24')
        Activity.objects.create(user='Superman', type='Run', duration=50, date='2025-11-24')

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        Workout.objects.create(name='Justice Strength', description='Strength for justice')

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=190)
        Leaderboard.objects.create(team='DC', points=205)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
