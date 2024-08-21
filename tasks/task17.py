import random
import math


def generate_task17(task_doc, answer_doc, task_number):

    a = random.randint(12, 24)

    task_text = f"Время T безотказной работы тягового электродвигателя распределено по экспоненциальному закону с математическим ожиданием {a} месяцев. Какова вероятность того, что данный двигатель откажет:\nа) менее чем через месяц после ремонта;\nб) не менее чем через год после ремонта?"

    a_answer = round(1 - math.exp(-(1/a)), 4)
    b_answer = round(math.exp((-12)*(1/a)), 4)

    task_answer = f"а) {a_answer}; б){b_answer}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")