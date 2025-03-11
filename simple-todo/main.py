import click # to create a command line interface
import json # to save and   load task from a file
import os

TODO_FILE = 'todo.json'

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE,'r') as f:
        data = json.load(f)
        if isinstance(data, dict):
            return [data]  # Wrap single dict in a list
        elif isinstance(data, list):
            return data
        else:
            return []  # Return an empty list for other data types
        
def save_tasks(tasks):
    with open(TODO_FILE,'w') as f:
        return json.dump(tasks,f,indent=4)
    
@click.group()
def cli():
    '''Simple Todo List Manager'''
    pass

@click.command()
@click.argument('task')
def add(task):
    '''Add a new task to the list'''
    tasks = load_tasks()
    tasks.append({'task': task,'done': False})
    save_tasks(tasks)
    click.echo(f'Task Added successfully : {task}')


@click.command()
def show():
    ''''List all the tasks'''
    tasks = load_tasks()
    if not tasks:
        click.echo('No tasks found')
        return
    for i, task in enumerate(tasks,1):
        click.echo(f'{i} {task["task"]}')
        click.echo(f'Done: {task["done"]}')

@click.command()
@click.argument('task_number',type=int) # type casting
def complete(task_number):
    '''Mark a task as complete'''
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        save_tasks(tasks)
        click.echo(f'Task {task_number} marked as completed.')
    else:
        click.echo(f'Invalid Task number : {task_number}')

@click.command()
@click.argument('task_number',type=int)
def delete(task_number):
    ''' Delete a Task '''
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        remove_task = tasks.pop(task_number - 1)
        save_tasks(remove_task)
        click.echo(f'Task {remove_task} number deleted.')
    else:
        click.echo(f'Invalid Task number ')

@click.command()
# @click.option('--index', type=int, default=None, help='Index of the task to mark as done')
@click.argument('index',type=int) # type casting
def done(index):
    tasks = load_tasks()
    if not tasks:
        click.echo('No tasks found')
        return
    if index is None:
        click.echo('Please provide an index (e.g., "done 1" or "done1")')
        return
    try:
        done = tasks[index - 1]
        done["done"] = True
        save_tasks(tasks)
        click.echo(f'Task marked as done : {done["task"]}')
    except IndexError:
        click.echo('Invalid Index')

cli.add_command(add)
cli.add_command(show)
cli.add_command(complete)
cli.add_command(delete)
cli.add_command(done)

if __name__ == '__main__':
    cli()