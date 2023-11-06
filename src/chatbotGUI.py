import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from chatbot import respond  # Import your chatbot functions

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AzubiGPT Chatbot")

        # Create a scrolled text widget to display the conversation
        self.conversation_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        self.conversation_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Create a label and a combobox for selecting chatbot areas
        self.area_label = tk.Label(root, text="Select Area:")
        self.area_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.areas = list(respond())
        self.selected_area = tk.StringVar()
        self.area_combobox = ttk.Combobox(root, textvariable=self.selected_area, values=self.areas)
        self.area_combobox.grid(row=1, column=1, padx=10, pady=5)
        self.area_combobox.bind("<<ComboboxSelected>>", self.display_questions)

        # Create a label and a combobox for selecting questions
        self.question_label = tk.Label(root, text="Select Question:")
        self.question_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        self.questions = []
        self.selected_question = tk.StringVar()
        self.question_combobox = ttk.Combobox(root, textvariable=self.selected_question, values=self.questions)
        self.question_combobox.grid(row=2, column=1, padx=10, pady=5)

        # Create an entry widget for user input
        self.user_input = tk.Entry(root, width=40)
        self.user_input.grid(row=3, column=0, padx=10, pady=5, columnspan=2)
        self.user_input.bind("<Return>", self.send_user_input)

        # Create a button to send user input
        self.send_button = tk.Button(root, text="Send", command=self.send_user_input)
        self.send_button.grid(row=3, column=2, padx=10, pady=5)

    def display_questions(self, event):
        selected_area = self.selected_area.get()
        self.questions = list(respond(selected_area).keys())
        self.question_combobox["values"] = self.questions
        self.selected_question.set("")

    def send_user_input(self, event=None):
        user_input = self.user_input.get()
        area = self.selected_area.get()
        question = self.selected_question.get()

        if not area and not question:
            area = user_input
        elif not question:
            question = user_input

        response = respond(area, question)

        self.conversation_text.insert(tk.END, f"User: {user_input}\n")
        self.conversation_text.insert(tk.END, f"AzubiGPT: {response}\n")
        self.conversation_text.see(tk.END)

        self.user_input.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()