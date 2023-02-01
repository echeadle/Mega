todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            # file = open('files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            # file = open('files/todos.txt', 'w')
            # file.writelines(todos)
            # file.close()

            with open('files/todos.txt', 'w') as file:
                todos = file.readlines()

        case 'show' | 'display':
            # file = open('files/todos.txt', 'r')
            # file.readlines()
            # file.close()
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()


            # new_todos = []
            # for item in todos:
            # new_item = item.strip('\n')
            # new_todos.append(new_item)
7
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index +1 }--{item}"
                print(row)
        case 'edit':
            number = int(input('Number of todo to edit: '))
            number -= 1
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number -1)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")
print('Bye!')