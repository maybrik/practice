from django.core.management.base import BaseCommand

from faker import Faker

from random import randint, random, randrange

from blog.models import Post, Comment

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


fake = Faker()
UserM = get_user_model()

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, default=10, choices=range(1, 200),
                            help='Enter how many data you want to create')


    def handle(self, *args, **options):
        amount = options['amount']

        for _ in range(amount):
            User.object.create(username=fake.name(), password=make_password('password'))

            posts = []
            for _ in UserM.objects.all():
                for i in range(random(1, 10)):
                    posts.append(Post(label=fake.sentence(nb_words=1), short_description=fake.sentence(nb_words=3),
                                      full_description=fake.text(), user=_))

                    Post.objects.bulk_create(posts)
