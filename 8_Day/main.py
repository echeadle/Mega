todos = []
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'show' | 'display':

            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index +1 }-{item}"
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