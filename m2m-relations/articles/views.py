from django.http import HttpResponse
from django.shortcuts import render


from articles.models import Article, Tag


def articles_list(request):
    """Функция формирует сгруппированный по дате публикации список статей и возвращает рендер"""
    template = 'articles/news.html'
    articles = Article.objects.all()  #order_by(ordering)
    context = {'object_list': articles}

    return render(request, template, context)


def add_tags(request):
    """Функция добавляет список тэгов в БД и возвращает уведомление."""
    tag_list = [
        'Наука',
        'Здоровье',
        'Культура',
        'Город',
        'Космос',
        'Международные отношения'
    ]

    for tag in tag_list:
        Tag.objects.create(name=tag)

    tag_str = ', '.join(tag_list)

    return HttpResponse(f'Успешно добавлен в БД следующий список - {tag_str}.')
