from django.shortcuts import render

tasks = [
    [{
        'name': 'Task1',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': False
    }, {
        'name': 'Task2',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': True
    }, {
        'name': 'Task3',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': False
    }, {
        'name': 'Task4',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': True
    }],
    [{
        'name': 'Task5',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': False
    }, {
        'name': 'Task6',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': True
    }, {
        'name': 'Task7',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': False
    }, {
        'name': 'Task8',
        'created': '10/09/2018',
        'due_on': '12/09/2018',
        'owner': 'admin',
        'mark': True
    }]
]


def todos(request):
    context = {
        'tasks_lists': tasks
    }
    return render(request, 'todo_list.html', context=context)


def todosCompleted(request, id):
    if id is None:
        context = {
            'tasks': tasks
        }
    else:
        context = {
            'tasks': tasks[id]
        }
    return render(request, 'completed_todo_list.html', context=context)
