class UserReprMixin:
    def __str__(self):
        full_name = self.user.get_full_name()
        return full_name if full_name else self.user.username
