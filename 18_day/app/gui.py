from modules import functions
import PySimpleGUI as sg
import time

sg.theme("DarkPurple4")

time_now = time.strftime("%b %d, %Y %H:%M:%S")
clock = sg.Text(time_now, key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
delete_button = sg.Button("Delete")
exit_button = sg.Button('Exit')
window = sg.Window('My To-Do App',
                   layout=[
                           [clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, delete_button],
                           [exit_button]
                           ],
                   font=('Helvetica', 15))

while True:
    event, values = window.read()
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].strip('\n')
                print(f'new_todo: {new_todo}')
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo

                print(5, f'todos:{todos}')
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica",20))

        case "Delete":
            try:
                todo_to_delete = values["todos"][0]
                todos = functions.get_todos()
                print(f"Delete: {todo_to_delete}")
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", font=("Helvetica", 20))

        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()
