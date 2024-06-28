from tortoise import Model, fields


class User(Model):
    id = fields.IntField(primary_key=True)
    tg_user_id = fields.TextField()
    tg_name = fields.TextField()
    game_user_id = fields.TextField()
    nickname = fields.TextField(null=True)

    def __str__(self):
        return self.tg_name, self.tg_user_id


class Game(Model):
    id = fields.IntField(primary_key=True)
    datetime = fields.DatetimeField()
    rating = fields.IntField()
    user = fields.ForeignKeyField('models.User')

    def __str__(self):
        return self.id, self.rating
