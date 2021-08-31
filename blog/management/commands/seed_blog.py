import random
from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from django_seed import Seed
from blog.models import Blog
from users.models import User


class Command(BaseCommand):
    help = "adds blog title only"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("length", type=int)

    def handle(self, *args: Any, **options: Any):
        length = options.get("length")

        if length is None or length <= 0:
            raise CommandError("length should be greater than 0")

        user = User.objects.all()

        seeder = Seed.seeder()

        for _ in range(length):
            blog = Blog(
                title=seeder.faker.sentence(),
                user=random.choice(user),
                # It is difficult to create content data using seeder
                content=r"""{"time": 1629628939542, "blocks"
                : [{"id": "iUoOJT-3aw", "type": "paragraph", "data": {"text": "asg"}}], "version": "2.22.2"}""",
                is_private=random.choice([0, 1]),
            )
            blog.save()
