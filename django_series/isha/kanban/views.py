from django.shortcuts import render, redirect, get_object_or_404
from .models import Column, Task


def board(request):
    columns = Column.objects.prefetch_related('tasks').all()
    return render(request, 'kanban/board.html', {'columns': columns})


def add_task(request, column_id):
    if request.method == 'POST':
        column = get_object_or_404(Column, id=column_id)
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()
        if title:
            Task.objects.create(title=title, description=description, column=column)
    return redirect('kanban:board')


def move_task(request, task_id, direction):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        columns = list(Column.objects.all())
        current_index = next((i for i, c in enumerate(columns) if c.id == task.column_id), None)
        if direction == 'right' and current_index is not None and current_index < len(columns) - 1:
            task.column = columns[current_index + 1]
            task.save()
        elif direction == 'left' and current_index is not None and current_index > 0:
            task.column = columns[current_index - 1]
            task.save()
    return redirect('kanban:board')


def delete_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.delete()
    return redirect('kanban:board')
