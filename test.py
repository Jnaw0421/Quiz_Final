from quiz import read_excel_file, display_quiz, display_score

quiz = read_excel_file('questions.xlsx')
display_quiz(quiz)
for index, q in enumerate(quiz):
    print(f"{index}. {q['question']}")
    options = ['A', 'B', 'C', 'D']
    for i, option in enumerate(q['options']):
            print(f"{options[i]}. {option}")
    user_answer = input("Enter the correct option letter (A, B, C, or D): ")
    if user_answer == q['correct_option']:
        print("Correct!")
    else:
        incorrect_answer = {
         "question": q['question'],
         "correct_answer": q['correct_option'],
         "explanation": q['explaination']
         }
    print(f"Incorrect the answer is: {q['correct_option']} \n {q['explaination']}\n")
