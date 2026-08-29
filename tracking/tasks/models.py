from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Назва")
    status = models.CharField(max_length=25, verbose_name='Статус')
    priority = models.CharField(max_length=25, verbose_name='Пріорітет')
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='tasks_images/', verbose_name='Зображення', blank=True, null=True)

    def __str__(self):
        return self.title