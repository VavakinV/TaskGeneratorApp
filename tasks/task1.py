import random
from docx.shared import Pt, Cm

def generate_task1(task_doc, answer_doc, task_number):
    a = random.randint(3, 6)
    b = random.randint(a, 10)
    task_text = f"Цифровой кодовый замок на сейфе имеет на общей оси {a} диск{'а' if a < 5 else 'ов'}, каждый из которых разделен на {b} сектор{'а' if b < 5 else 'ов'}. Какова вероятность открыть замок, выбирая код наудачу, если кодовая комбинация:\nа) неизвестна;\nб) не содержит одинаковых цифр?"
    
    b_answer = b
    for i in range(1, a):
        b_answer*=(b-i)

    task_answer = f"а) 1/{b**a}; б)1/{b_answer}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")