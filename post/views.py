from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostModelForm, AskForm

# Create your views here.

def index(request):
    context = {}
    posts = Post.objects.all()
    context['post'] = posts
    return render(request, 'index.html', context)

def help(request):
    return HttpResponse('This is the help page')

def detail(request, post_id):
    context = {}
    context['post'] = Post.objects.get(id=question_id)
    return render(request, 'detail.html', context)

def update(request, post_id):
    context = {}
    post = Post.objects.get(id=question_id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return HttpResponse('Post Updated')
        else:
            context['form'] = form
            render(request, 'update.html', context)
    else:
        context['form'] = PostModelForm(instance=post)
    return render(request, 'update.html', context)

def create(request):
    context = {}
    form = AskForm()

    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Post Created')

    return render(request, 'create.html', {'form': form})
