import string
import random
import tkinter as tk

class PasswordGeneratorGUI:
    def __init__(self, title="Password Generation"):
        self.labelString = 'Enter desired password length:'
        self.buttonString = 'Generate'
        self.copyString = 'Copy to Clipboard'
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry('500x350')
        self.root.configure(bg="light blue")
        self.root.resizable(1, 0)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        self.topFrame = tk.Frame(self.root, width=300, height=300, bg="light blue")
        self.topFrame.grid(row=0, column=0, padx=10, pady=10)
        
        self.userInput = tk.StringVar()
        self.display = tk.StringVar()
        
        self.createGUI()

    def createGUI(self):
        self.makeLabel()
        self.makeEntry()
        self.makeButton()
        self.makePasswordDisplay()
        self.makeExitButton()

    def makeEntry(self):
        self.textEntry = tk.Entry(self.topFrame, textvariable=self.userInput, fg="#614553", bg="white")
        self.textEntry.grid(row=1, column=0)

    def makeLabel(self):
        self.display.set(self.labelString)
        self.displayLabel = tk.Label(self.topFrame, textvariable=self.display, fg="#614553", bg="light blue")
        self.displayLabel.grid(row=0, column=0)

    def makeButton(self):
        self.gameButton = tk.Button(self.topFrame, text=self.buttonString, fg="#614553", highlightbackground="light blue", command=self.clicked)
        self.gameButton.grid(row=2, column=0)

    def disableButton(self):
        self.gameButton['state'] = tk.DISABLED

    def enableButton(self):
        self.gameButton['state'] = tk.NORMAL

    def makeExitButton(self):
        self.exitButton = tk.Button(self.topFrame, text="Exit", fg="#614553", highlightbackground="light blue", command=self.clickedExit)
        self.exitButton.grid(row=6, column=0)
    
    def makePasswordDisplay(self):
        self.passwordDisplay = tk.Label(self.topFrame, text="", fg="#614553", bg="light blue", wraplength=400)
        self.passwordDisplay.grid(row=4, column=0)

    def makeCopyButton(self):
        self.copyButton = tk.Button(self.topFrame, text=self.copyString, fg="#614553", highlightbackground="light blue", command=self.copyToClipboard)
        self.copyButton.grid(row=3, column=0)

    def copyToClipboard(self):
        generated_password = self.passwordDisplay.cget("text")
        if generated_password:
            self.root.clipboard_clear()
            self.root.clipboard_append(generated_password)
            self.root.update() #updates clipboard with password

    def clicked(self):
        password_length = self.userInput.get()
        if password_length.isnumeric():
            password_length = int(password_length)
            if password_length >= 4 and password_length <= 500:
                password = create_password(password_length)
                self.display.set('Password generated!\nEnter desired length for new password:')
                self.passwordDisplay.config(text=password)
                self.makeCopyButton()
            else: 
                self.display.set('Password must be 4-500 characters long.')
        else:
            self.display.set('Please enter a numeric value.')

    def clickedExit(self):
        self.root.destroy()

def create_password(password_length):
    possible_chars = list(string.punctuation + string.digits + string.ascii_letters)
    return "".join([random.choice(possible_chars) for x in range(int(password_length))])

if __name__ == "__main__":
    app = PasswordGeneratorGUI()
    app.root.mainloop()