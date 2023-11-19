import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename



def open_file():

    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"My Text Editor - {filepath}")



def save_file():
    file_path = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
    )

    if file_path:
        with open(file_path,'w') as output_file:
            text=txt_edit.get(1.0,tk.END)
            output_file.write(text)
            window.title('saved')

window = tk.Tk()
window.rowconfigure(0, minsize=600)
window.columnconfigure(1, minsize=600)

frm_button = tk.Frame(master=window, relief="raised")
frm_button.rowconfigure([0, 1], weight=1)
txt_edit = tk.Text(master=window)

frm_button.grid(column=0, row=0, sticky="nw", padx=5, pady=5)
txt_edit.grid(column=1, row=0, sticky="nesw")


btn_open = tk.Button(master=frm_button, text="open file", command=open_file)
btn_save = tk.Button(master=frm_button, text="save as", command=save_file)

btn_open.grid(column=0, row=0, sticky="new")
btn_save.grid(column=0, row=1, sticky="ew")

window.mainloop()
