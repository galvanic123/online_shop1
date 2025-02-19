from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from blog.models import Blog


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/paper_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(publication=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/paper_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'description', 'image', 'publication', 'count_of_views')
    template_name = 'blog/paper_form.html'
    success_url = reverse_lazy('blog:paper_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'description', 'image', 'publication', 'count_of_views')
    template_name = 'blog/paper_form.html'
    success_url = reverse_lazy('blog:paper_list')

    def get_success_url(self):
        return reverse('blog:paper_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/paper_confirm_delete.html'
    success_url = reverse_lazy('blog:paper_list')

# Create your views here.
