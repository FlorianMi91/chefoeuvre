import pytest



# @pytest.mark.django_db
# def test_create_user():
#     User.objects.create_user("test","test@test.com","test")
#     count = User.objects.all().count()
#     print(count)
#     assert count == 1

#-----------------------------------------------------------------------------
# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user("test_user")

# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new_pass")
#     assert user_1.check_password("new_pass") is True
#-----------------------------------------------------------------------------



def test_set_check_username(user_1):
    print(user_1)
    assert user_1.username == "test_user"

def test_set_check_username2(user_1):
    print(user_1)
    assert user_1.username == "test_user"

def test_create_user(new_user):
    print(new_user.first_name)
    assert new_user.username == "test_user"