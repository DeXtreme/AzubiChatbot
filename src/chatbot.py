import tkinter as tk
from tkinter import scrolledtext

import json
import pathlib



class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("AzubiGPT Chatbot")

        # Create a scrolled text widget to display the conversation
        self.conversation_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        self.conversation_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Create an entry widget for user input
        self.user_input = tk.Entry(root, width=40)
        self.user_input.grid(row=3, column=0, padx=10, pady=5, columnspan=2)
        self.user_input.bind("<Return>", self.send_user_input)

        # Create a button to send user input
        self.send_button = tk.Button(root, text="Send", command=self.send_user_input)
        self.send_button.grid(row=3, column=2, padx=10, pady=5)

        self.area = None
        self.question = None

        response = self.respond(self.area, self.question, True)
        self.conversation_text.insert(tk.END, f"AzubiGPT: {response}\n\n")
    
    def load_data(self):
        # Define and return the dictionary with responses
        data_dir = pathlib.Path(__file__).parent.parent/"src/data"

        responses = {}

        area_json = {
            "Career Opportunities": "career.json",
            "Eligibility Criteria": "criteria.json",
            "Curriculum": "curriculum.json",
            "Payment Options": "payment.json",
            "Program Duration": "program_duration.json"
        }

        for area in area_json:
            with open(data_dir/area_json[area]) as f:
                responses[area] = json.loads(f.read())

        return responses

    def respond(self,area=None, question=None, start=False):
        responses = self.load_data()
        
        # Create a new dict with lower case keys
        responses_lower = {area.lower():{q.lower():responses[area][q] for q in responses[area]} for area in responses}

        # Check if start is True
        if start:
            message = "Hello and welcome to Azubi. I am AzubiGPT, here to answer all your questions.\nWhich area would you like to hear about?\n"
            areas = list(responses_lower.keys())
            area_list = "\n".join([f"{i}. {area.title()}" for i, area in enumerate(areas, 1)])
            return message + area_list

        # Check if no arguments are passed
        if area is None and question is None:
            message = "Which area would you like to hear about?\n"
            areas = list(responses_lower.keys())
            area_list = "\n".join([f"{i}. {area.title()}" for i, area in enumerate(areas, 1)])
            return message + area_list
        
        # Check if only the area argument is passed
        if area is not None and question is None:
            area = area.lower()
            if area in responses_lower:
                questions = list(responses_lower[area].keys())
                question_list = "\n".join([f"{i}. {q.capitalize()}" for i, q in enumerate(questions, 1)])
                return f"Here are a few FAQs in this area:\n{question_list}"

        # Check if both area and question arguments are passed
        if area is not None and question is not None:
            area = area.lower()
            question = question.lower()
            if area in responses_lower and question in responses_lower[area]:
                return responses_lower[area][question]

        # Handle other cases or invalid input
        return "Sorry, I don't quite understand."

    
    def send_user_input(self, event=None):
        
        user_input = self.user_input.get()

        if not user_input:
            return
        
        self.conversation_text.insert(tk.END, f"User: {user_input}\n\n")

        if not self.area:
            self.area = user_input
        elif not self.question:
            self.question = user_input
            response = self.respond(self.area, self.question)
            self.conversation_text.insert(tk.END, f"AzubiGPT: {response}\n\n")
            
            self.area = None
            self.question = None

        response = self.respond(self.area, self.question)
        self.conversation_text.insert(tk.END, f"AzubiGPT: {response}\n\n")
        
        if response[0:5] == "Sorry":
            self.area = None
            self.question = None
            
        self.conversation_text.see(tk.END)
        self.user_input.delete(0, tk.END)
        
    
if __name__ == "__main__":
    root = tk.Tk()
    app = Chatbot(root)
    root.mainloop()
