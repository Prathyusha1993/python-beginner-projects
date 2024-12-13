# to do list app
#  user should allow to add task, view current list of tasks and remove the task when they are completed
from termios import VLNEXT


def print_menu():
    print('\nTodo List Menu: ')
    print('1. View Tasks')
    print('2. Add Task')
    print('3. Remove a Task')
    print('4. Exit')


def get_choice():
    while True:
        choice = input('Enter your choice: ')
        valid_choice = ('1', '2','3', '4')
        if choice not in valid_choice:
            print('Invalid choice')
            continue
        else:
            return choice


def display_tasks(tasks):
    if not tasks:
        print('No task in list.')
        return

    for index, task in enumerate(tasks, start=1):
        print(f'{index}. {task}')


def add_task(tasks):
    while True:
        task = input('Enter a new task: ').strip()
        if len(task) != 0:
            tasks.append(task)
            break
        else:
            print('Invalid Task')


def remove_task(tasks):
    display_tasks(tasks)

    while True:
        try:
            task_number = int(input('Enter the task number: '))
            if  1 <= task_number <= len(tasks):
                tasks.pop(task_number - 1)
                break
            else:
                raise ValueError
        except ValueError:
            print('Invalid task number')


def main():
    tasks = []

    while True:
        print_menu()

        choice = get_choice()

        if choice == '11':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        else:
            break


main()

