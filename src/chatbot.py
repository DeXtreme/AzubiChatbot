def load_data():
    # Define and return the dictionary with responses
    responses = {
        "Career Opportunities": {
            "what career opportunities does it offer?": "It offers a wide range of career opportunities, including cloud architect, cloud engineer, cloud developer, cloud administrator, and cloud security specialist",
            "What skills are essential for a career in cloud engineering?": "Essential skills include proficiency in cloud platforms (e.g., AWS, Azure, Google Cloud), knowledge of containerization (e.g., Docker, Kubernetes), scripting and automation",
            "What career path can one follow in cloud engineering?": "A typical career path may start as a junior cloud engineer or cloud administrator and progress to roles like cloud engineer, senior cloud engineer, and cloud architect"
        },
        "Eligibility Criteria": {
            "What are the eligibility criteria for this program?": "The eligibility criteria typically include specific requirements such as educational qualifications and other prerequisites",
            "Are there any age restrictions for this program?": "Age restrictions may vary depending on the program. This program is open to all age groups if only you can read and write",
            "Is work experience required to be eligible for this program?": "This program does not require any work experience"
        },
        "Curriculum": {
            "What topics are covered in the program's curriculum?": "The curriculum covers a wide range of topics, including but not limited to Linux, Python, and AWS Service",
            "What is the structure of the curriculum?": "The program is typically structured into two parts, that is teaching and project work",
            "How is the course delivered?": "The course is primarily delivered online"
        },
        "Payment Options": {
            "What payment options are accepted by the company?": "We accept a variety of payment options, including credit and debit cards (Visa, MasterCard, American Express)",
            "Is there a preferred or recommended payment method?": "While we accept multiple payment methods, we often recommend credit or debit card payments for their convenience and immediate processing",
            "Are there any additional fees associated with specific payment methods?": "Some payment methods may have associated fees, such as transaction fees for credit card payments or currency conversion fees for international transactions"
        },
        "Program Duration": {
            "How long is the course?": "The program duration is nine(9) months",
            "How long is the learning phase?": "The learning phase lasts for six(6) months",
            "How long is the project phase?": "The project phase lasts for three(3) months"
        }
    }
    return responses
def respond(area=None, question=None, start=False):
    responses = load_data()
    
    # Check if start is True
    if start:
        message = "Hello and welcome to Azubi. I am AzubiGPT, here to answer all your questions.\nWhich area would you like to hear about?\n"
        areas = list(responses.keys())
        area_list = "\n".join([f"{i}. {area}" for i, area in enumerate(areas, 1)])
        return message + area_list

    # Check if no arguments are passed
    if area is None and question is None:
        message = "Which area would you like to hear about?\n"
        areas = list(responses.keys())
        area_list = "\n".join([f"{i}. {area}" for i, area in enumerate(areas, 1)])
        return message + area_list
 # Check if only the area argument is passed
    if area is not None and question is None:
        area = area.lower()
        if area in responses:
            questions = list(responses[area].keys())
            question_list = "\n".join([f"{i}. {q}" for i, q in enumerate(questions, 1)])
            return f"Here are a few FAQs in this area:\n{question_list}"

    # Check if both area and question arguments are passed
    if area is not None and question is not None:
        area = area.lower()
        question = question.lower()
        if area in responses and question in responses[area]:
            return responses[area][question]

    # Handle other cases or invalid input
    return "Sorry, I don't quite understand."

if __name__ == "__main__":
    start = True
    area = None
    question = None
    while True:
        response = respond(area, question, start=start)
        print(f"AzubiGPT: {response}")
        if response[0:5] == "Sorry":
            area = None
            question = None
            continue
if not area:
            query = input("User: ")
            area = query
        elif not question:
            query = input("User: ")
            question = query
        else:
            area = None
            question = None

        start = False