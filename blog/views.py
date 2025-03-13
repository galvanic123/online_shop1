from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.views import View
from blog.models import Blog
from django.shortcuts import render


class BlogListView(ListView):
    model = Blog
    template_name = "blog/paper_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(publication=True)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/paper_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_of_views += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "description", "image", "publication", "count_of_views")
    template_name = "blog/paper_form.html"
    success_url = reverse_lazy("blog:paper_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "description", "image", "publication", "count_of_views")
    template_name = "blog/paper_form.html"
    success_url = reverse_lazy("blog:paper_list")

    def get_success_url(self):
        return reverse("blog:paper_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/paper_confirm_delete.html"
    success_url = reverse_lazy("blog:paper_list")


class CatalogContactsView(View):
    def get(self, request):
        return render(request, "blog/contacts.html")

    def post(self, request):
        # Получение данных из формы
        name = request.POST.get("name")
        message = request.POST.get("message")
        # Обработка данных (например, сохранение в БД, отправка email и т. д.)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


# Create your views here.
