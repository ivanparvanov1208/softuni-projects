from .task import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        t = next((t for t in self.tasks if t.name == task_name), None)
        if t:
            t.completed = True
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0
        for i in range(len(self.tasks)):
            if self.tasks[i].completed:
                self.tasks.remove(self.tasks[i])
                count += 1

        return f"Cleared {count} tasks."

    def view_section(self):
        task_details = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n{task_details}"

