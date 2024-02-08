from django.http import JsonResponse
from .models import Post, Like
from django.views.generic.base import TemplateView
from pathlib import Path
from django.core.files import File
from django.template.loader import render_to_string


class PostsPage(TemplateView):
    template_name = 'posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

    def post(self, request):
        data = request.POST
        files = request.FILES
        with open('static/images/image.png', 'wb') as file:
            file.write(files['file'].read())
        path = Path('static/images/image.png')
        with path.open('rb') as file:
            image = File(file, name=file.name)
            post = Post(user=self.request.user, text=data['text'], image=image)
            post.save()
        html = render_to_string('post_template.html', {'p': post})
        return JsonResponse(html, safe=False)


class PostPage(TemplateView):
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(id=self.kwargs['id'])
        like = Like.objects.filter(post=post)
        context['post'] = post
        context['likes_amount'] = len(like)
        context['is_liked'] = False
        for i in like:
            if i.user == self.request.user:
                context['is_liked'] = True
                break
        return context

    def post(self, request, **kwargs):
        post = Post.objects.get(id=self.kwargs['id'])
        like = Like.objects.filter(post=post)
        for i in like:
            if i.user == self.request.user:
                i.delete()
                return JsonResponse({'action': 0, 'amount': len(like) - 1}, safe=False)
        else:
            l = Like(user=self.request.user, post=post)
            l.save()
            return JsonResponse({'action': 1, 'amount': len(like) + 1}, safe=False)

