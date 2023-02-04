const questionEl = document.getElementById('question');
const choicesEl = document.getElementById('choices');
const submitBtn = document.getElementById('submit-btn');

let currentQuestionIndex = 0;
let questions = [];

// Fetch questions from the server
fetch('/questions')
  .then(response => response.json())
  .then(data => {
    questions = data;
    renderQuestion();
  });

// Render the current question and choices to the page
function renderQuestion() {
  const currentQuestion = questions[currentQuestionIndex];
  questionEl.innerHTML = currentQuestion.question;

  // Clear the previous choices
  choicesEl.innerHTML = '';

  // Render the new choices
  currentQuestion.choices.forEach(choice => {
    const choiceEl = document.createElement('div');
    choiceEl.innerHTML = choice;
    choiceEl.classList.add('choice');
    choicesEl.appendChild(choiceEl);
  });

  submitBtn.style.display = 'block';
}

// Handle submitting the answer
submitBtn.addEventListener('click', () => {
  const selectedChoice = document.querySelector('.choice.selected');
  if (!selectedChoice) {
    return alert('Please select an answer.');
  }

  const answer = selectedChoice.innerHTML;
  if (answer === questions[currentQuestionIndex].correct_answer) {
    alert('Correct!');
  } else {
    alert('Incorrect.');
  }

  currentQuestionIndex++;
  if (currentQuestionIndex === questions.length) {
    alert('Quiz complete!');
    return;
  }

  renderQuestion();
});

// Handle selecting an answer
choicesEl.addEventListener('click', e => {
  if (e.target.classList.contains('choice')) {
    const choices = document.querySelectorAll('.choice');
    choices.forEach(choice => {
      choice.classList.remove('selected');
    });
    e.target.classList.add('selected');
  }
});
