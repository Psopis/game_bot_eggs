import datetime

import tortoise

from infrastructure.database.models import User, Game


class UserWorking:
    @staticmethod
    async def add_user(user_id, name):
        try:
            return await User.get(tg_user_id=user_id)
        except tortoise.exceptions.DoesNotExist:
            print(f"Created user {name}")
            await User.create(tg_user_id=user_id, tg_name=name, game_user_id='', niсkname=''
                              )

    @staticmethod
    async def create_game(user, rating):
        await Game.create(datetime=datetime.date.today(), rating=rating, user=user)

    @staticmethod
    async def get_users_history_game(user):
        print(f"Get history game {user.nickname}")
        return await Game.all().filter(user=user)

    @staticmethod
    async def set_rating(user_id, rating):
        user = await User.get(tg_user_id=user_id)
        user.rating += rating
        await user.save()

    @staticmethod
    async def get_today_rating():
        users = await User.all().order_by('-rating')
        arr = []
        ch = 0
        for user in users:
            arr.append(user)
            ch += 1
            if ch == 10:
                return arr

    @staticmethod
    async def get_week_rating():
        users = await User.all().order_by('-rating_week')
        print(users)
        arr = []
        ch = 0
        for user in users:
            print(user.rating)
            arr.append(user)
            ch += 1
            if ch == 10:
                return arr

    @staticmethod
    async def check_game_name(name):
        return await User.get_or_none(nickname=name)

    @staticmethod
    async def check_game_id(id):
        return await User.get_or_none(game_user_id=id)

    @staticmethod
    async def set_game_name(user_id, name):

        user = await User.get(tg_user_id=user_id)
        user.nickname = name
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
