import random

from django.core.checks import database
from django_seed import Seed
from faker import Faker
from faker.providers import DynamicProvider
from random import randrange

from tree.models import Employee

# Create custom new provider to faker instance
structure_provider = DynamicProvider(
    provider_name="structure",
    elements=['Department', 'Division', 'Branch', 'Unit']
)
position_provider = DynamicProvider(
    provider_name="position",
    elements=['Head', 'Executive manager', 'Director', 'Supervisor', 'Manager']
)


def first_rec():
    """
    Generated first record of employees (highl level)
    :return:
    """
    e1 = Employee(
        structure='Block',
        full_name='Мария Ивановна Сидорова',
        position='Head',
        emp_date='2010-02-16',
        salary='4000',
    )
    e2 = Employee(
        structure='Block',
        full_name='Иван Иванович Иванов',
        position='Head',
        emp_date='2010-02-16',
        salary='4000',
    )
    e1.save()
    e2.save()


def file_db(count, structure, year, parent_min, parent_max):
    """
    This generates fake data for the database
    """
    seeder = Seed.seeder()
    fake = Faker('ru_RU')

    # then add new provider to faker instance
    fake.add_provider(structure_provider)
    fake.add_provider(position_provider)

    with Employee.objects.disable_mptt_updates():
        val = Employee.objects.last()
        seeder.add_entity(Employee, count, {
            'structure': structure,
            'full_name': lambda x: fake.name(),
            'position': fake.position(),
            'emp_date': '{}-{}-{}'.format(year, random.randint(1, 12), random.randint(1, 28)),
            'salary': lambda x: random.randint(1000, 4000),
            'parent': lambda x: Employee.objects.get(id=randrange(parent_min, parent_max, 1)),
        })
        seeder.execute()


def del_objects():
    """
    This deletes all objects from the database
    """
    with Employee.objects:
        Employee.objects.all().delete()
        Employee.objects.rebuild()


def run():
    """
    This runs the file_db function
    """
    first_rec()
    file_db(10, 'Department', 2018, 1, 2)
    file_db(100, 'Division', 2019, 2, 11)
    file_db(1000, 'Branch', 2020, 12, 111)
    file_db(50000, 'Unit', 2021, 112, 1111)
    Employee.objects.rebuild()
    pass
