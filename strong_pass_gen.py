# strong_pass_gen.py
#
# Module that creates a strong password generator, with GUI.

import string
import random
import tkinter as tk

class PasswordGeneratorGUI:
    """A class that creates a randomly generated strong password of the user's desired length.
    Implements a GUI using tkinter for ease of use."""
    
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
        """Creates the GUI window."""
        self.makeLabel()
        self.makeEntry()
        self.makeButton()
        self.makePasswordDisplay()
        self.makeExitButton()

    def makeEntry(self):
        """Creates the text entry box."""
        self.textEntry = tk.Entry(self.topFrame, textvariable=self.userInput, fg="#614553", bg="white")
        self.textEntry.grid(row=1, column=0)

    def makeLabel(self):
        """Creates the label providing user instructions within the GUI."""
        self.display.set(self.labelString)
        self.displayLabel = tk.Label(self.topFrame, textvariable=self.display, fg="#614553", bg="light blue")
        self.displayLabel.grid(row=0, column=0)

    def makeButton(self):
        """Creates the password generation button."""
        self.generateButton = tk.Button(self.topFrame, text=self.buttonString, fg="#614553", highlightbackground="light blue", command=self.clickedGenerate)
        self.generateButton.grid(row=2, column=0)
        
    def makeExitButton(self):
        """Creates the GUI exit button."""
        self.exitButton = tk.Button(self.topFrame, text="Exit", fg="#614553", highlightbackground="light blue", command=self.clickedExit)
        self.exitButton.grid(row=6, column=0)
    
    def makePasswordDisplay(self):
        """Creates the label displaying the generated password."""
        self.passwordDisplay = tk.Label(self.topFrame, text="", fg="#614553", bg="light blue", wraplength=400)
        self.passwordDisplay.grid(row=4, column=0)

    def makeCopyButton(self):
        """Creates the button that allows a user to copy to clipboard."""
        self.copyButton = tk.Button(self.topFrame, text=self.copyString, fg="#614553", highlightbackground="light blue", command=self.copyToClipboard)
        self.copyButton.grid(row=3, column=0)

    def copyToClipboard(self):
        """Updates the user's clipboard with the generated password."""
        generated_password = self.passwordDisplay.cget("text")
        if generated_password:
            self.root.clipboard_clear()
            self.root.clipboard_append(generated_password)
            self.root.update() 

    def clickedGenerate(self):
        """Checks if generate button is clicked, and ensures user input is valid."""
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
        """Checks if exit button is clicked and destroys the window if so."""
        self.root.destroy()

def create_password(password_length):
    """Randomly generates a password of _password_length_, utilizing any punctuation, digits, and ascii letters."""
    possible_chars = list(string.punctuation + string.digits + string.ascii_letters)
    return "".join([random.choice(possible_chars) for x in range(int(password_length))])

if __name__ == "__main__":
    app = PasswordGeneratorGUI()
    app.root.mainloop()