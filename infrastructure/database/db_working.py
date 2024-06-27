import datetime

import tortoise

from infrastructure.database.models import User


class UserWorking:
    @staticmethod
    async def add_user(user_id, username, time):
        try:
            return await User.get(user_id=user_id)
        except tortoise.exceptions.DoesNotExist:
            print(f"Created user {username}")
            await User.create(user_id=user_id, username=username, role_='member',
                              date=time + datetime.timedelta(days=30), your_promo='', activated_promo='')

    @staticmethod
    async def check_user(user_id):
        return await User.get_or_none(user_id=user_id)

    @staticmethod
    async def get_id_from_name(username):

        user = await User.get(username=username)
        return user.user_id

    @staticmethod
    async def get_name_from_id(user_id):

        return await User.get_or_none(user_id=user_id)

    @staticmethod
    async def get_user(user_id):
        user = await User.get(user_id=user_id)
        return user

    @staticmethod
    async def role_update(username, role):

        user = await User.get(username=username)
        user.role_ = role
        user.is_employee = False
        if role == 'admin':
            user.is_employee = True

        await user.save()

    @staticmethod
    async def set_your_promo(user_id, promo):
        user = await User.get(user_id=user_id)
        user.your_promo = promo
        await user.save()

    @staticmethod
    async def activate_promo(user_id, promo):
        user = await User.get(user_id=user_id)
        user.activated_promo = promo
        await user.save()


class AdminWorking:
    @staticmethod
    async def get_all_admins():
        return await User.filter(is_employee=True)

    @staticmethod
    async def add_admin(user_id, username, time):
        try:
            return await User.get(user_id=user_id)
        except tortoise.exceptions.DoesNotExist:

            await User.create(user_id=user_id, username=username, role_='admin', profit=0, is_employee=True, date=time)

    @staticmethod
    async def check_admin(user_id):
        user = await User.get(user_id=user_id)
        return user.role_
