import random
import math

def generate_task5(task_doc, answer_doc, task_number):

    b = random.randint(5, 20)
    a = random.randint(1, b-1)
    d = random.randint(5, 20)
    c = random.randint(1, d-1)
    e = random.randint(5, 20)

    task_text = f"Экзаменационный билет по математике содержит три вопроса (по одному из трех разделов). Студент знает {a} из {b} вопросов первого раздела, {c} из {d} — второго и все {e} вопросов третьего раздела. Преподаватель ставит положительную оценку при ответе хотя бы на два вопроса билета. Какова вероятность того, что студент не сдаст экзамен?"

    numerator = (b-a)*(d-c)
    denominator = b*d
    gcd = math.gcd(numerator, denominator)
    numerator /= gcd
    denominator /= gcd

    task_answer = f"{int(numerator)}/{int(denominator)}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")