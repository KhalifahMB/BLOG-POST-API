from django.core.management.base import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from blogs.models import Blog, Tag
import random


class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        users = User.objects.all()

        for _ in range(50):
            title = fake.sentence(nb_words=6)
            content = fake.paragraph(
                nb_sentences=3, variable_nb_sentences=True)
            author = random.choice(users)

            post = Blog.objects.create(
                title=title, content=content, author=author)

            num_tags = random.randint(1, 3)
            for _ in range(num_tags):
                tag_name = fake.word()
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)

            self.stdout.write(self.style.SUCCESS(
                f'Successfully created post "{title}"'))
