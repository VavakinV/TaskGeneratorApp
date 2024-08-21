import random
import math


def generate_task16(task_doc, answer_doc, task_number):

    a = random.randint(2, 4)
    b = random.randint(10, 25)

    task_text = f"Интервал движения теплоходов «Москва» на реке Иртыш составляет {a} ч. Дачники подходят к пристани в некоторый момент, не зная расписания. Какова вероятность того, что они опоздали на очередной теплоход не более чем на {b} мин?"

    a_minutes = a*60
    numerator = b
    denominator = a_minutes
    gcd = math.gcd(numerator, denominator)
    numerator /= gcd
    denominator /= gcd

    task_answer = f"{int(numerator)}/{int(denominator)}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")