import datetime

import tortoise

from infrastructure.database.models import User


class UserWorking:
    @staticmethod
    async def add_user(user_id, name):
        try:
            return await User.get(tg_user_id=user_id)
        except tortoise.exceptions.DoesNotExist:
            print(f"Created user {name}")
            await User.create(tg_user_id=user_id, tg_name=name, rating=0, game_user_id='', game_name=''
                              )

    @staticmethod
    async def set_rating(user_id, rating):
        user = await User.get(tg_user_id=user_id)
        user.rating += rating
        await user.save()

    @staticmethod
    async def check_game_name(name):
        return await User.get_or_none(game_name=name)

    @staticmethod
    async def check_game_id(id):
        return await User.get_or_none(game_user_id=id)

    @staticmethod
    async def set_game_name(user_id, name):

        user = await User.get(tg_user_id=user_id)
        user.game_name = name
        await user.save()

    @staticmethod
    async def set_game_id(user_id, id):

        user = await User.get(tg_user_id=user_id)
        user.game_user_id = id
        await user.save()

    @staticmethod
    async def check_user(user_id):
        return await User.get_or_none(tg_user_id=user_id)

    @staticmethod
    async def get_id_from_name(name):

        user = await User.get(tg_name=name)
        return user.user_id

    @staticmethod
    async def get_name_from_id(user_id):

        return await User.get_or_none(tg_user_id=user_id)

    @staticmethod
    async def get_user(user_id):
        user = await User.get(tg_user_id=user_id)
        return user


class AdminWorking:
    pass
