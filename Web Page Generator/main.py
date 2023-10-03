import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        self.master.geometry("700x350")

        self.lbl_instruction = Label(self.master, text="Enter custom HTML content:")
        self.lbl_instruction.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky=W)

        self.txt_custom_content = Text(self.master, height=4, width=50)
        self.txt_custom_content.grid(row=1, column=0, columnspan=2, padx=20, pady=(0, 20))

        self.btn_default = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn_default.grid(row=2, column=0, padx=20, pady=10, sticky=W)

        self.btn_custom = Button(self.master, text="Generate Custom HTML Page", width=30, height=2, command=self.customHTML)
        self.btn_custom.grid(row=2, column=1, padx=(0, 20), pady=10, sticky=E)

    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer sale!"
        self.txt_custom_content.delete("1.0", END)
        self.txt_custom_content.insert("1.0", htmlText)

    def customHTML(self):
        customText = self.txt_custom_content.get("1.0", END).strip()
        if customText:
            self.generateHTML(customText)
        else:
            tk.messagebox.showerror("Error", "Please enter custom HTML content.")

    def generateHTML(self, content):
        htmlFile = open("index.html", "w")
        htmlFileContent = f"<html>\n<body>\n<h1>{content}</h1>\n</body>\n</html>"
        htmlFile.write(htmlFileContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
