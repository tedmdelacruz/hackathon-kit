from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        help = """This is a sample custom Django command"""

        # parser.add_argument('positional_arg_here')

        # parser.add_argument(
        #     '--test-arg',
        #     default='',
        #     dest='test_arg',
        #     help="This is a test argument"
        # )

    def handle(self, *args, **options):
        pass
