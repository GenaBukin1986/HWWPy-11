class Stack:
    def __init__(self):
        self.__task_list = []

    def add_task(self, task):
        self.__task_list.append(task)
        return f'Задача {task} успешно добавлена в список задач'

    def add_more_tasks(self, tasks):
        self.__task_list.extend(tasks)

    def remove_task(self):
        if self.is_empty():
            return 'Стэк пуст'
        task = self.__task_list.pop()
        return f'Задача {task} успешно удалена из списка задач'

    def is_empty(self):
        if not len(self.__task_list):
            return True
        return False

class TaskManager:
    def __init__(self):
        self.__task_dict = dict()

    def new_task(self,do, number):
        if number not in self.__task_dict:
            # self.__task_dict[number] = [].append(do)
            self.__task_dict[number] = []
            self.__task_dict[number].append(do)
        else:
            self.__task_dict[number].append(do)
        return f'Задача {do} с приоритетом {number} успешно добавлена в ваш список задач'

    def remove_task(self):
        key_tasks = sorted(self.__task_dict.keys())
        if not self.is_epmty(key_tasks):
            for i in key_tasks:
                if not self.is_epmty(self.__task_dict[i]):
                    task = self.__task_dict[i].pop()
                    if self.is_epmty(self.__task_dict[i]):
                        del self.__task_dict[i]
                    return f'Задача {task} успешно удалена из списка задач'

            else:
                return "Список задач пуст"

    def is_epmty(self, my_list):
        if len(my_list) == 0:
            return True
        else:
            return None

    def __str__(self):
        return '\n'.join([f'{i[0]} - {"; ".join(i[1])}' for i in sorted(self.__task_dict.items())])



    def get_type(self):
        return type(self.__task_dict.items())






if __name__ == "__main__":
    # a = [1,2,3]
    # b = (1,2,3)
    # stack = Stack()
    # stack.add_more_tasks(a)
    # stack.add_more_tasks(b)
    # for i in range(10):
    #     print(stack.remove_task())

    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать ДЗ", 2)
    for i in range(10):
        manager.remove_task()
        print(manager)
        print()