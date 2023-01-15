from datetime import datetime
from uuid import uuid4
 
 
class Task:
   def __init__(self, name=None):
       self.name = name
       self.create_time = str(datetime.now().strftime("%x %X"))
       self.updated_time = "NA"
       self.completed_time = "NA"
       self.task_done = False
       self.id = uuid4()
 
   @staticmethod
   def update_task(task, name=None):
       task.name = name
       task.updated_time = str(datetime.now().strftime("%x %X"))
 
   @staticmethod
   def complete_task(task=None):
       task.task_done = True
       task.completed_time = str(datetime.now().strftime("%x %X"))
 
 
class TaskManager:
   task = dict()
   main_menu = "1. Add New Task \n2. Show All Task \n3. Show Incomplete Tasks \n4. Show completed Task \n5. Update Task\n6. Mark A Task Completed"
 
   def __intit__(self):
       pass
 
   def new_task(self):
       _task_name = input("Enter New Task:")
       _task = Task(_task_name)
       self.task[_task.id] = _task
       print("\nTask Created Successfully")
 
   def all(self):
       _is_empty = True
       for id, _task in self.task.items():
           _is_empty = False
           print()
           print(
               f"ID - {id}\nTask - {_task.name}\nCreated time - {_task.create_time}\nUpdated time - {_task.updated_time}\nCompleted - {_task.task_done}\nCompleted time - {_task.completed_time}")
       if (_is_empty):
           print("Task Emtpy")
 
   def all_incomplete(self):
       _all_completed = True
       for _id, _task in self.task.items():
           if (_task.task_done == False):
               _all_completed = False
               print()
               print(
                   f"ID - {_id}\nTask - {_task.name}\nCreated time - {_task.create_time}\nUpdated time - {_task.updated_time}\nCompleted - {_task.task_done}\nCompleted time - {_task.completed_time}")
       if (_all_completed):
           print("All task Completed")
 
   def all_completed(self):
       _no_task_completed = True
       for id, _task in self.task.items():
           if (_task.task_done):
               _no_task_completed = False
               print()
               print(
                   f"ID - {id}\nTask - {_task.name}\nCreated time - {_task.create_time}\nUpdated time - {_task.updated_time}\nCompleted - {_task.task_done}\nCompleted time - {_task.completed_time}")
 
       if (_no_task_completed):
           print("No Completed Task")
 
   def update(self):
       _task_n = dict()
       _t_n = 1
       _all_completed = True
       for _id, _task in self.task.items():
           if (_task.task_done == False):
               _all_completed = False
               _task_n[str(_t_n)] = _id
               _t_n = _t_n + 1
       if (_all_completed):
           print(
               "No Task to update, you can only update incomplete Task")
       else:
           print("Select Which Task To Update")
           for _t_n, id in _task_n.items():
               print()
               print(
                   f"Task No - {_t_n}\nID - {id}\nTask - {self.task[id].name}\nCreated time - {self.task[id].create_time}\nUpdated time - {self.task[id].updated_time}\nCompleted - {self.task[id].task_done}\nCompleted time - {self.task[id].completed_time}")
 
           print()
           try:
               _t_n = input("Enter Task Number:")
               id = _task_n[_t_n]
               name = input("Enter your Task: ")
               Task.update_task(self.task[id], name)
               print("Task Updated Successfully")
           except KeyError:
               print("invalid Task number")
 
   def mark_completed(self):
       _task_n = dict()
       _t_n = 1
       _all_completed = True
       for id, _task in self.task.items():
           if (_task.task_done == False):
               _all_completed = False
               _task_n[str(_t_n)] = id
               _t_n = _t_n + 1
       if (_all_completed):
           print(
               "No Incomplete Task")
       else:
           print("Select Which Task To Complete")
           for t_n, id in _task_n.items():
               print()
               print(
                   f"Task No - {t_n}\nID - {id}\nTask - {self.task[id].name}\nCreated time - {self.task[id].create_time}\nUpdated time - {self.task[id].updated_time}\nCompleted - {self.task[id].task_done}\nCompleted time - {self.task[id].completed_time}")
           try:
               t_n = input("Enter Task Number:")
               id = _task_n[t_n]
               Task.complete_task(self.task[id])
               print("Task Completed Successfully")
           except KeyError:
               print("invalid Task number")
 
 
def driver():
   tm = TaskManager()
   while (True):
       print(f"{tm.main_menu}")
       print()
       option = input("Enter option:")
       print()
       if (option == "1"):  # create new Task
           tm.new_task()
       elif (option == "2"):  # show All Task
           tm.all()
 
       elif (option == "3"):  # show All incompleted Task
           tm.all_incomplete()
 
       elif (option == "4"):  # show All completed Task
           tm.all_completed()
 
       elif (option == "5"):  # Update Task
           tm.update()
 
       elif (option == "6"):  # Task Completed
           tm.mark_completed()
 
       else:
           print("Invalid Option")
       print()
 
 
driver()
