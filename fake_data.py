# OS config
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Django config
import django
django.setup()

# Faker config
from faker import Faker
fake_data = Faker()

# # importing app models
from parent_child.models import Parent, Child


# 1st, creating the priority object with fake data
def create_parent():
    parent = Parent.objects.get_or_create(
        first_name=fake_data.first_name(),
        last_name=fake_data.last_name(),
        street=fake_data.street_address(),
        city=fake_data.city(),
        state=fake_data.state(),
        zip=fake_data.zipcode(),
    )[0]
    # note: [0] = Usage of get_or_create() method, if priority object already exists then get from first index.
    # if not, then create the priority object.
    parent.save()
    return parent


# populating other classes
def populate(n):
    for entry in range(n):

        # 1st, calling priority method for creating priority object
        parent = create_parent()

        # creating objects
        Child.objects.create(
            first_name=fake_data.first_name(),
            last_name=fake_data.last_name(),
            parent=parent,
        )


# calling populate() method
if __name__ == '__main__':
    print("** Populating the Database, Please Wait...")
    populate(5)
    print('** Populating Complete **')


