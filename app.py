from flask import Flask, render_template, Blueprint, request
from quiz import run_quiz, display_score


quiz_blueprint = Blueprint('quiz', __name__, template_folder='templates', static_folder='static')

@quiz_blueprint.route('/')
def index():
    return render_template('index.html')

@quiz_blueprint.route('/quiz', methods= ['POST', 'GET'])
def quiz():
    quiz_data = run_quiz("questions.xlsx")
    return render_template('quiz.html', quiz=quiz_data)

    
@quiz_blueprint.route("/score", methods=["GET", "POST"])
def score():
    quiz = run_quiz("questions.xlsx")
    print(request.form)
    answers = []
    for i in range(len(quiz)):
        answer = request.form.get(f'answer{i}')
        answers.append(answer)
        print(answers)
    result = display_score(quiz, answers)
    score = result[0]
    incorrect_answers = result[1:]
    return render_template("score.html", score=score, incorrect_answers=incorrect_answers)
 
 

'''def score():
    quiz = run_quiz("questions.xlsx")
    answers = []
    for i in range(len(quiz)):
        answer = request.form.get(f'answer{i}')
        answers.append(answer)
        print(answer)
    score, incorrect_answers = display_score(quiz, answers)
    return render_template("score.html", score=score, incorrect_answers=incorrect_answers)'''

app = Flask(__name__)
app.register_blueprint(quiz_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
