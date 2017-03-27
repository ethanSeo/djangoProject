from django.views.generic import View, TemplateView
from django.http import HttpResponse

class PostListView1(View):
    def get(self, requeset):
        name = 'Ethan'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
        <h1>Ask Django</h1>
        <p>{name}</p>
        <p>여러분의 파이썬&장고 페이스메이커</p>
        '''

post_list1 = PostListView1.as_view()


class PostListView2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = 'Ethan'
        return context

post_list2 = PostListView2.as_view()

# class PostListView3(object):
#
#
# class ExcelDownloadView(object):
