from project.task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"

        searched_task_class = [t_class for t_class in self.tasks if t_class.name == task_name][0]
        searched_task_class.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        completed_tasks = [t_class for t_class in self.tasks if t_class.completed]
        cleared_tasks_amount = len(completed_tasks)
        if cleared_tasks_amount:
            self.tasks = [t_class for t_class in self.tasks if not t_class.completed]
        return f"Cleared {cleared_tasks_amount} tasks."

    def view_section(self):
        output = f"Section {self.name}:\n"

        for task_class in self.tasks:
            output += f"{task_class.details()}\n"

        return output


task = Task("Odi da pikash", "27/05/2020")
print(task.change_name("Odi da seresh"))
print(task.change_due_date("28.05.2020"))
# task.add_comment("Don't forget laptop")
# print(task.edit_comment(0, "Don't forget laptop and notebook"))
# print(task.details())
# section = Section("Daily tasks")
# print(section.add_task(task))
# second_task = Task("Make bed", "27/05/2020")
# section.add_task(second_task)
# print(section.clean_section())
# print(section.view_section())
