
print("<-- SUPER TO-DO LIST -->")

tasks = []

while True:
    cmd = input('CMD -> ')
    if cmd == 'add':
        task = input('TASK -> ')
        tasks.append(task)
        print("Done")
    elif cmd == '' and cmd != '':
        print('?')
    elif cmd == "show":
        print(tasks)
        for i in tasks:
            print(f'--- {i}')
    elif cmd == 'comand':
        print(f"clear - очистить список\n show - показать список\n add - добавить в список\n rem - очистить списко\n exit - вийти из приложения\n")     
    elif cmd == 'about':
        print(f"Приложение создан\nАртемом Пучковим \nПриложение записует ваши плани на день)")
    elif cmd == 'rem':
        taskr = int(input ("NAMBER -> "))
        tasks.pop(taskr -1 )
        print("Done")
    elif cmd == "clear":
        tasks.clear(tasks)
        print("done")
    elif cmd == 'Lesson':
        print('~ is over 🤣 ~')
    elif cmd == "exit":
        break
    elif cmd == "ok":
        print("ok")
        
