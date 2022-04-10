""" Sets up the database info used for this webapp"""
from peewee import Model, CharField, DateTimeField, ForeignKeyField
import os

from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class User(Model):
    """ Creates a User object, which consists of name and password"""
    name = CharField(max_length=255, unique=True)
    password = CharField(max_length=255)

    class Meta:
        database = db


class Task(Model):
    """ Creates a Task object, which consists of name (the name of the task), 
    performed (which will display the date and time it was completed, null if not),
    and performed_by (name of the person who did the task (must be a name found in User table).
    null if not done yet)
    """
    name = CharField(max_length=255)
    performed = DateTimeField(null=True)
    performed_by = ForeignKeyField(model=User, null=True)

    class Meta:
        database = db