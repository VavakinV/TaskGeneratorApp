import random
import math

def generate_task11(task_doc, answer_doc, task_number):

    a = random.randint(400, 600)
    b = ["двух", "трех", "четырех"]
    c = random.randint(0, 2)

    task_text = f"На факультете обучается {a} студент{'' if (a%10 == 1 and (9>(a%100) or (a%100)>20)) else 'а' if (2<=(a%10)<=4 and (9>(a%100) or (a%100)>20)) else 'ов'}. Какова вероятность того, что 31 декабря является днем рождения одновременно {b[c]} студентов данного факультета?"

    n = a
    p = 1/365
    mean = n*p

    std_dev = (c - n*p)/math.sqrt(n*p*(1-p))

    answer = (1 / math.sqrt(2 * math.pi)) * math.exp(-(std_dev ** 2) / 2)

    task_answer = f"φ({round(std_dev, 4)}) ~ {round(answer, 4)}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")