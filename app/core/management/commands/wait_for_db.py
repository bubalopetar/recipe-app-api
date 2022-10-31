"""Django command to wait to db to be available
"""

from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Pyscopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """
    Django command to wait do db
    """

    def handle(self, *args, **options):
        self.stdout.write("waiting for database...")
        db_up = False
        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Pyscopg2Error, OperationalError):
                self.stdout.write("Database unavailable, wait 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available"))
