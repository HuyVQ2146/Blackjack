from InquirerPy import inquirer 

quiz_bank = [
    {
        "question": "Do you want to play again?:",
        "choices": ["Yes", "No"],
    },
    {
        "question": "Do you want to hit or stand?:",
        "choices": ["Hit", "Stand"],
    }
]

def questions(i):
    q = quiz_bank[i]

    answer = inquirer.select(
        message=q['question'],
        choices=q['choices'],
        cycle=True,  # Cho phép bấm xuống ở câu cuối thì tự cuộn lên câu đầu
    ).execute()

    q['user_answer'] = answer

    return q['user_answer']
