# I asked chat gpt to add a feature to save the file with ctrl + s and then asked it to Improve the code
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

class TextEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("My Text Editor")
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

        self.create_widgets()

    def create_widgets(self):
        self.frm_button = tk.Frame(self.master, relief="raised")
        self.frm_button.rowconfigure([0, 1], weight=1)
        self.frm_button.grid(column=0, row=0, sticky="nw", padx=5, pady=5)

        self.txt_edit = tk.Text(self.master)
        self.txt_edit.grid(column=1, row=0, sticky="nesw")

        self.btn_open = tk.Button(self.frm_button, text="Open File", command=self.open_file)
        self.btn_save = tk.Button(self.frm_button, text="Save As", command=self.save_file)

        self.btn_open.grid(column=0, row=0, sticky="new")
        self.btn_save.grid(column=0, row=1, sticky="ew")

        # Bind the Ctrl + S shortcut to the save_file function
        self.master.bind("<Control-s>", self.save_file)

    def open_file(self, event=None):
        filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filepath:
            with open(filepath, mode="r", encoding="utf-8") as input_file:
                text = input_file.read()
                self.txt_edit.delete("1.0", tk.END)
                self.txt_edit.insert(tk.END, text)
                self.master.title(f"My Text Editor - {filepath}")

    def save_file(self, event=None):
        file_path = asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )

        if file_path:
            with open(file_path, 'w') as output_file:
                text = self.txt_edit.get("1.0", tk.END)
                output_file.write(text)
                self.master.title('File Saved - {}'.format(file_path))

def main():
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
