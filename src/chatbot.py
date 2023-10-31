import json
import pathlib


def load_data():
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

def respond(area=None, question=None, start=False):
    responses = load_data()
    
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

if __name__ == "__main__":
    start = True
    area = None
    question = None
    while True:
        response = respond(area, question, start=start)
        print(f"AzubiGPT: {response}\n")
        if response[0:5] == "Sorry":
            area = None
            question = None
            continue
        if not area:
            query = input("User: ")
            print("")
            area = query
        elif not question:
            query = input("User: ")
            question = query
            print("")
        else:
            area = None
            question = None

        start = False
