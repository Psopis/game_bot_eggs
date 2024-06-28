from tortoise import Model, fields


class User(Model):
    id = fields.IntField(primary_key=True)
    tg_user_id = fields.TextField()
    tg_name = fields.TextField()
    rating = fields.IntField()
    game_user_id = fields.TextField()
    game_name = fields.TextField()

    def __str__(self):
        return self.tg_name, self.tg_user_id
