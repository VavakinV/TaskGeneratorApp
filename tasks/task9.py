import random
import math

def generate_task9(task_doc, answer_doc, task_number):
    
    a = random.randint(1, 9)/10
    b = random.randint(3, 7)
    c = b//2 if b%2==0 else (b+1)//2

    task_text = f"Вероятность выхода из строя за время Т одного (любого) элемента равна {a}. Определить вероятность того, что за время Т из {b} элементов из строя выйдет:\nа) {c} элемент{'а' if c < 5 else 'ов'};\nб) меньше {c} элементов."

    q = 1-a
    a_answer = math.comb(b, c)*(a**c)*(q**(b-c))
    b_answer = 0
    for i in range(c):
        b_answer += math.comb(b, i)*(a**i)*(q**(b-i))

    task_answer = f"а){round(a_answer, 4)}; б){round(b_answer, 4)}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")