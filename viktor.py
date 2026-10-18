import tkinter as tk
from tkinter import messagebox 
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Викторина")
        self.root.geometry("600x400")
        self.current_question = 0
        self.score = 0
        self.selected_answer = tk.StringVar()
        self.setup_ui()
        self.questions = [
            {
                'question': 'Если синий кит закричит в открытом космосе, услышит ли это рыба в аквариуме?',
                'options': {
                    'a': 'А) Да, если рыба в наушниках.',
                    'b': "Б) Нет, кит забыл текст песни.",
                    'c': "В) Рыба оглохнет от масштаба драмы.",
                    'd': "Г) Звук испугается вакуума и вернется домой."
                },
                'correct': 'd'
            },
            {
                'question': 'Сколько весит габен, если перевести его в Алькатрас?',
                'options': {
                    'a': 'А) Примерно три с половиной пушистых хвоста.',
                    'b': "Б) Бесконечность, так как коты любят спать.",
                    'c': "В) Ровно столько, сколько весит утренний туман на усах.",
                    'd': "Г) Нисколько, облака — это сахарная вата для гигантов."
                },
                'correct': 'b'
            },
            {
                'question': 'Почему макароны уходят в себя, когда на них смотрят пристально?',
                'options': {
                    'a': 'А) Они стесняются своей наготы без соуса.',
                    'b': "Б) Боятся сгореть от стыда в кастрюле.",
                    'c': "В) Отрабатывают технику скрытности от повара.",
                    'd': "Г) Считают калории под взглядом."
                },
                'correct': 'c'
            },
            {
                'question': 'Что делает стул, когда на него никто не садится?',
                'options': {
                    'a': 'А) Медитирует в позе «четыре точки опоры».',
                    'b': "Б) Скучает по чьей-то пятой точке.",
                    'c': "В) Рассказывает анекдоты тумбочке.",
                    'd': "Г) Замышляет восстание против дивана."
                },
                'correct': 'a'
            },
            {
                'question': 'Какого цвета срежет понедельник, если покрасить его в пятницу?',
                'options': {
                    'a': 'А) Серо-буро-малиновый с искрой.',
                    'b': "Б) Цвета спелого будильника.",
                    'c': "В) Прозрачный от усталости.",
                    'd': "Г) Никакого, у них раз    ный иммунитет."
                },
                'correct': 'b'
            }
            
        ]
        self.setup_ui()
        self.show_question()
    def setup_ui(self):
        self.question_frame = tk.Frame(self.root, bg='#f0f0f0', padx=10, pady=10)
        self.question_frame.pack()

        self.question_number_label = tk.Label(
            self.question_frame,
            bg='#f0f0f0',
            font=("Arial", 10, "bold")
        )
        self.question_number_label.pack()

        self.question_label = tk.Label(
            self.question_frame,
            text="",
            bg="#f0f0f0",
            font=("Arial", 12)
        )
        self.question_label.pack(pady = 10)   
        self.options_frame = tk.Frame(self.question_frame, bg="#f0f0f0")
        self.options_frame.pack(pady=10)
        self.radio_buttons = [self.question_frame, self.options_frame, ]
    
        rb = tk.Radiobutton(
            self.options_frame,
            text="",
            variable=self.selected_answer,
            value="",
            bg="#f0f0f0",
            font=("Arial", 11),
        )
        rb.pack(pady=5)
        self.radio_buttons.append(rb)
        self.sumbit_button = tk.Button(
            self.question_frame,
            text="Ответить",
            bg="#0  0FF2A",
            fg="white",
            font=("Arial", 12),
            command=self.check_answer()

        )
        self.sumbit_button.pack(pady=20)
        self.progress_label = tk.Label(
            self.progress_frame,
            height=20,
            bg="white"
        )
        self.progress_canvas.pack(padx=5)
        self.progress_bar = self.progress_canvas.create_rectangle(
            0, 0, 0, 20,
            fill="#1EFF00"
        )
        self.score_label = tk.Label(
            self.root,
            text=f"Счет: {self.score}/{len(self.questions)}",
            bg="#f0f0f0",
            font=("Arial", 12)
        )
        self.score_label.pack(pady=5)


    def show_question(self):
        if self.current_question < len(self.questions):
            self.question_data = self.questions[self.current_question]

            self.question_number_label.config(
                text = f"Вопрос {self.current_question + 1} из {len(self.questions)}"
            )
            self.question_label.config(text=self.question_data["question"])

        else:
            self.show_results()
    def check_answer(self):

        question_data = self.questions[self.current_question]
        user_answer = self.selected_answer.get()

        if user_answer == question_data["correct_answer"]:
            self.score += 1
            self.show_info("емое...", "как ты угадал?")
        else:
            correct_option = question_data['correct_answer']
            correct_text = question_data["options"][correct_option]
            self.show_info(
                "неверно аххахахахахахахахха, я так и знал что ты тупой",
                f"правильный ответ был:{correct_option}) {correct_text}")
        self.current_question += 1
        self.show_question()

    def show_info(self, title, message):
        info = tk.Toplevel(self.root)
        info.title(title)
        info.geometry("350x180")
        info.resizable(False, False)

        tk.Label(
            info,
            text=title,
            pady=10
        ).pack()

        tk.Label(
            info,
            text=message,
            pady=10
        ).pack()

        tk.Button(
            info,
            text="ОКЕЙ ВА",
            command=info.destroy,
            width=10,
        ).pack(pady=10)

    def restart_quiz(self):
        self.current_question = 0
        
        
    # def write_text(self, pos, text):
    #  x, y = pos
    # if text == 'X':
    #     self.canvas.create_text(x, y, text='X', font=('Arial', 40, 'bold'), fill='dodgerblue3')
    # else:
    #     self.canvas.create_text(x, y, text='O', font=('Arial', 40, 'bold'), fill='red')

    # def check_space(self):

    #     x, y = self.get_text_pos((event.x, event.y))
    #     return self.board[y] == ' '

    # def check_game_over(self):

    #     return ' ' not in self.board[1:] 
root = tk.Tk()
app = QuizApp(root)
root.mainloop()