from django.db import models

# Create your models here.
class NewsSource(models.Model):
    source_name = models.CharField(max_length = 255)
    source_perc = models.IntegerField()
    source_link = models.URLField()

    def __str__(self):
        return self.source_name

    def get_absolute_url(self):
        return reverse('source_edit', kwargs={'pk': self.pk})


class NewsFeed(models.Model):
    title        = models.CharField(max_length=255)
    content      = models.TextField()
    content_link = models.URLField()
    source       = models.ForeignKey(NewsSource, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def delete_all_news(self):
        NewsFeed.objects.all().delete()

