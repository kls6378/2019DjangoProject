from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from board.models import Board

# Create your views here.

def index(request):
    board_list=Board.objects.all().order_by('-date')
    return render(request, 'board/index.html', {'board_list':board_list})

def detail(request, board_id):
    board=get_object_or_404(Board, pk=board_id)
    return render(request, 'board/detail.html', {'board':board})

def create(request):
    if request.method == 'POST':
        new_board = Board.objects.create(
            name=request.POST['name'],
            password=request.POST['password'],
            title=request.POST['title'],
            contents=request.POST['contents']
        )
        return redirect(f'/board/{ new_board.id }')

    return render(request, 'board/create.html')

def update(request, board_id):
    board = Board.objects.get(id=board_id)

    if request.method == 'POST':
        if request.POST['password'] == board.password:
            board.name = request.POST['name']
            board.title = request.POST['title']
            board.contents = request.POST['contents']
            board.save()
            return redirect(f'/board/{ board.id }')

    return render(request, 'board/update.html',{'board':board})

def delete(request, board_id):
    board = Board.objects.get(id=board_id)

    if request.method == 'POST':
        if request.POST['password'] == board.password:
            board.delete()
            return redirect('/board/')

    return render(request, 'board/delete.html',{'board':board})
