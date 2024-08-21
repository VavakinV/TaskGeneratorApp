import random
import math
from scipy.stats import norm


def generate_task18(task_doc, answer_doc, task_number):

    a = random.randint(10, 30)
    b = random.randint(1, a)

    task_text = f"Случайные ошибки измерения подчинены нормальному закону со средним квадратическим отклонением {a} мм и математическим ожиданием, равным нулю. Найти вероятность того, что измерение будет произведено с ошибкой, не превосходящей по абсолютной величине {b} мм."

    answer = round(norm.cdf(b/a) - norm.cdf(-b/a), 4)

    task_answer = f"{answer}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")