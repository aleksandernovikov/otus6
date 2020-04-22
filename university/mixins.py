from django.utils.functional import cached_property


class UserRepresentationModelMixin:
    def __str__(self):
        return self.user.display_name if self.user.display_name else self.user.username

    @cached_property
    def fio(self):
        return f'{self.user.first_name} {self.user.middle_name} {self.user.last_name}'


class TitleViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self, 'page_title'):
            context.update({
                'title': self.page_title
            })
        return context
