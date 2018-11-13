from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django.contrib.contenttypes.models import ContentType

from .models import SavedQuery
from .forms import SavedQueryForm


class SavedQueryView(View):
    model = None

    def get(self, *args, **kwargs):
        saved_queries = SavedQuery.get_saved_query_for_user_and_model(user=self.request.user, model=self.content_type)
        return JsonResponse({'saved_queries': list(saved_queries)})

    def post(self, *args, **kwargs):
        form = SavedQueryForm(data=self.request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.author = self.request.user
            query.model = self.content_type
            query.save()
            return JsonResponse({'id':query.id,
                                 'model_id':query.model.id,
                                 'description':query.description,
                                 'query':query.query,
                                 'is_public':query.is_public,
                                 'author_id':query.author.id
                                 }, status=201)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    @property
    def content_type(self):
        return ContentType.objects.get_for_model(self.model)


class SavedQueryPostView(View):
    model = None

    def post(self, *args, **kwargs):
        obj = get_object_or_404(SavedQuery, pk=kwargs.get('pk'))
        form = SavedQueryForm(instance=obj, data=self.request.POST)
        if form.is_valid():
            query = form.save(commit=False)
            query.author = self.request.user
            query.model = self.content_type
            query.save()
            return JsonResponse({'id': query.id,
                                 'model_id': query.model.id,
                                 'description': query.description,
                                 'query': query.query,
                                 'is_public': query.is_public,
                                 'author_id': query.author.id
                                 }, status=200)

    def delete(self, *args, **kwargs):
        status = False
        result, _ = SavedQuery.objects.get(pk=kwargs['pk']).delete()
        if result:
            status = True
        return JsonResponse({'id': self.kwargs['pk'], 'deleted': status}, status=200)

    @property
    def content_type(self):
        return ContentType.objects.get_for_model(self.model)
