//глобальные переменные
//ссылка на контейнер
var container = document.getElementById("container");
//массив вопросов с сылками на dom
var questions = [];
//текущий вопрос !счёт с единицы для использования переменной в представлении
var currentQuestion = 1;
//классы
//Вариант
function Option(text, id, type, questionId){
	this.div = document.createElement('div');
	this.div.className = "option";

	this.input = document.createElement('input');

	this.input.type = type;
	this.input.name = questionId;
	this.input.id = id;
	this.input.value = id;
	this.div.appendChild(this.input);

	this.label = document.createElement('label');
	this.label.innerHTML = text;
	this.label.htmlFor = id;
	this.div.appendChild(this.label);
};
//Вопрос
function Question(text, type, id, options_data){
   	//создаём контейнер для вопроса
	this.questionBlock = document.createElement('div');
	//даём классы, описанные в css
	this.questionBlock.className = "question-block hidden";

	//блок с текстом вопроса
	this.questionText = document.createElement('div');
	//даём ему класс, описанный в css
	this.questionText.className = "question-text";
	//наполняем блок текстом
	//( можно было-бы использовать поле .text, но .innerHTML обрабатывает теги, так-что это позволит добивить <img> <b> <i> <br>, в общем, любые необходимые плюхи для представления вопроса )
	this.questionText.innerHTML = text;
	//запрепляем questionText за questionBlock
	this.questionBlock.appendChild(this.questionText);

	//создаём контейнер, содержащий ответы
	this.optionsBlock = document.createElement('div');
	//как всегда задаём ему класс
	this.optionsBlock.className = "option-block";
	//закрепляем optionBlock за questionBlock
	this.questionBlock.appendChild(this.optionsBlock);

	//создадим массив в котором будем хранить ссылки на элементы
	this.options = [];
	//не понял как обратится к этому объекту внутри функции, поэтому создал question, чтобы к нему обращатся
	var question = this;
	//теперь в цикле для каждого варианта создадим элемент и поместим их в optionBlock
	options_data.forEach(function(option_data, i){
		//создаём и добавляем вариант в массив с вариантами :E
		var option = new Option(option_data.choice_text,
								option_data.choice_id,
								type,
								id);
		question.options.push(option);
		//добавляем вариант в dom
		question.optionsBlock.appendChild(question.options[i].div);
	});

	container.appendChild(this.questionBlock);
};

//Функции
//наполняет переменную questions, заполняет container элементами dom
function buildStructure(){
	//разбор json, создание вопросов
	data.forEach(function(question_data){
		var question = new Question(	question_data.question_text,
										question_data.question_input_type,
										question_data.question_id,
										question_data.question_choice);
		questions.push(question);
	})

	//добавление элементов управления
	var nextButton = document.createElement('div');
	nextButton.id = "nextQuestion";
	nextButton.onclick = function(){ nextQuestion();};
	nextButton.className = "controlElement";
	container.appendChild(nextButton);

	var prevButton = document.createElement('div');
	prevButton.id = "previousQuestion";
	prevButton.onclick = function(){ previousQuestion();};
	prevButton.className = "controlElement";
	container.appendChild(prevButton);

	var submitButton = document.createElement('input');
	submitButton.type = "submit";
	submitButton.id = "finishButton";
	var submitButtonLabel = document.createElement('label');
	submitButtonLabel.htmlFor = "finishButton";
	submitButtonLabel.className = "std controlElement";
	submitButtonLabel.innerHTML = "Завершить тестирование";
	container.appendChild(submitButton);
	container.appendChild(submitButtonLabel);

    //Отображение первого вопроса
    showQuestion(1)
};
//показать вопрос
function showQuestion(questionNumber){
	questions[currentQuestion - 1].questionBlock.className = 
		questions[currentQuestion - 1].questionBlock.className.replace("visible", "hidden");
	questions[questionNumber - 1].questionBlock.className = 
		questions[questionNumber - 1].questionBlock.className.replace("hidden", "visible");
	currentQuestion = questionNumber;
}
//следующий вопрос
function nextQuestion(){
	if (currentQuestion != questions.length){
		showQuestion(currentQuestion + 1);
	}else{
		alert("it is a last question");
	}
}
//Предыдущий вопрос
function previousQuestion(){
	if (currentQuestion != 1){
		showQuestion(currentQuestion - 1);
	}else{
		alert("it is a first question");
	}
}