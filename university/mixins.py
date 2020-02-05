class UserRepresentationModelMixin:
    def __str__(self):
        return self.user.display_name if self.user.display_name else self.user.username


class TitleViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self, 'page_title'):
            context.update({
                'title': self.page_title
            })
        return context
