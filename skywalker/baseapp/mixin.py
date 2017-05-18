

class TitleContentPageMixin(object):

    title_content = None

    def get_context_data(self, **kwargs):
        context = super(TitleContentPageMixin, self).get_context_data(**kwargs)
        title_content = self.title_content
        if title_content:
            context['title_content'] = title_content
        else:
            context['title_content'] = title_content
        return context