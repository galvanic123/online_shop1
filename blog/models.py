from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=300, verbose_name="Название статьи")
    description = models.TextField(
        verbose_name="Описание статьи", null=True, blank=True
    )
    image = models.ImageField(upload_to="images/", verbose_name="Превью", blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="дата создания", blank=True
    )
    publication = models.BooleanField(verbose_name="Признак публикации", default=True)
    count_of_views = models.IntegerField(
        verbose_name="Количество просмотров", default=0
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title"]


# Create your models here.
