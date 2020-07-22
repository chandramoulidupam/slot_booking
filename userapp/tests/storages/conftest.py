import pytest
from freezegun import freeze_time
from userapp.models.models import User


@pytest.fixture()
def users():
    list_of_users = [
        User(username="user1", password="user1passowrd", is_admin=True),
        User(username="user2", password="user2passowrd", is_admin=False),
        User(username="user3", password="user3passowrd", is_admin=False)
        ]
    User.objects.bulk_create(list_of_users)
    users = User.objects.all()
    return users
