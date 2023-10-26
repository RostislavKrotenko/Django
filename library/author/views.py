from django.shortcuts import render, HttpResponse
from .models import Author


def create_author(request):
    if request.method == 'GET':
        return render(request, 'new_author.html')

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        patronymic = request.POST.get('patronymic')

        if Author.objects.filter(surname=surname, name=name, patronymic=patronymic).exists():
            return HttpResponse('Author has already added')

        else:
            Author.create(name=name, surname=surname, patronymic=patronymic)
            return HttpResponse('Author has been added', status=200)


def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'author_list.html', context)


def delete_author(request, author_id=None):
    if request.method == 'GET':
        return render(request, 'delete_author.html')
    
    if request.method == 'POST':
        author_id = request.POST.get('author_id')
        if author_id and Author.objects.filter(id=author_id):
            Author.delete_by_id(author_id)
            return HttpResponse('Deleting has been completed')
        else:
            return HttpResponse("This author doesn't exist")
        

        