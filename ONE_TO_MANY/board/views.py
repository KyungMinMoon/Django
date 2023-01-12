from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import (require_http_methods,
                                          require_POST,
                                          require_safe, )
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@require_http_methods(['GET', 'POST'])
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)        
        if form.is_valid():
            article = form.save()
            return redirect('board:article_detail', article.pk)
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'board/form.html', context)


@require_safe  # GET, (HEAD) 요청만 허용하겠다.
def article_index(request):
    articles = Article.objects.all()
    context = {'articles': articles, }
    return render(request, 'board/index.html', context)


@require_safe  # GET, (HEAD) 요청만 허용하겠다.
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm()
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'board/detail.html', context)


@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    
    if form.is_valid():
        # 완전 저장하려고 하면 NOT NULL 에러 뜨니까, 직전에 멈춰 주세요.
        comment = form.save(commit=False)
        # 나머지는 직접 할게요
        comment.article = article
        comment.save()

    return redirect('board:article_detail', article.pk)


@require_POST
def delete_comment(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    article = get_object_or_404(Article, pk=article_pk)
    comment.delete()
    return redirect('board:article_detail', article.pk)