from tortoise import Model, fields


class User(Model):
    id = fields.IntField(primary_key=True)
    user_id = fields.TextField()
    username = fields.TextField()
    role_ = fields.TextField()
    date = fields.DateField()
    your_promo = fields.TextField()
    activated_promo = fields.TextField()
    is_employee = fields.BooleanField(default=False)

    def __str__(self):
        return self.username, self.user_id
