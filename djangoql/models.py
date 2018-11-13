from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q


class SavedQuery(models.Model):
    model = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, null=True)
    query = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Saved query'
        verbose_name_plural = 'Saved queries'
        ordering = ('is_public',)

    @staticmethod
    def get_saved_query_for_user_and_model(user, model):
        """
        Get all saved queries: public and for current user, if user is none, get only public queries for model
        """
        if user:
            qs = SavedQuery.objects.filter(Q(is_public=True, model=model) | Q(is_public=False, author=user, model=model)).values()
        else:
            qs = SavedQuery.objects.filter(is_public=True, model=model).values()
        return qs
