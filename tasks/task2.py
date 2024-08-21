import random
import math

def generate_task2(task_doc, answer_doc, task_number):
    a = random.randint(10, 20)
    b = random.randint(10, 15)
    c = random.randint(5, 10)
    d = random.randint(max(1, c-b), min(a, c))
    e = c-d
    task_text = f"В зале имеется {a} белых и {b} синих кресел. Случайным образом места занимают {c} человек. Найти вероятность того, что они займут:\nа) {d} белых и {e} синих кресел;\nб) хотя бы одно синее кресло."
    
    a_answer = round(math.comb(a, d)*math.comb(b,e)/math.comb(a+b, c), 4)
    b_answer = round(1-(math.comb(a, c)/math.comb(a+b, c)), 4)

    task_answer = f"а)C({a}, {d})C({b}, {e})/C({a+b}, {c}) ≈ {a_answer}; б)1 - (C({a}, {c})/C({a+b}, {c})) ≈ {b_answer}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")