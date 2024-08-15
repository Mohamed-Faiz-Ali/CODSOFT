import tkinter as tk

def add_task():
    task=task_entry.get()
    if task:
        task_listbox.insert(tk.END,task)
        task_entry.delete(0,tk.END)

def remove_task():
    selected_task_index=task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
root = tk.Tk()
root.title("To-Do-List")
root.geometry("700x600+450+100")

task_listbox = tk.Listbox(root,width=100,height=20)
task_listbox.pack(pady=10)

task_entry = tk.Entry(root,width=100)
task_entry.pack(pady=10)

add_button = tk.Button(root,text="ADD TASK",fg="black",command=add_task,bg="silver",padx=20)
remove_button = tk.Button(root,text="REMOVE TASK",fg="black",command=remove_task,bg="silver",padx=9)
add_button.pack()
remove_button.pack()
root.mainloop()
                          


