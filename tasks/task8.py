import random

def generate_task8(task_doc, answer_doc, task_number):
    
    a = random.randint(10, 50)
    b = random.randint(10, 40)
    c = 100-a-b
    d = random.randint(1, 9)/10
    e = random.randint(1, 9)/10
    f = random.randint(1, 9)/10

    task_text = f"Три студента — Дима, Егор и Максим — на лабораторной работе по физике производят {a}, {b} и {c}% всех измерений, допуская ошибки с вероятностями {d}, {e} и {f} соответственно. Преподаватель проверяет наугад выбранное измерение и объявляет его ошибочным. Кто из трех студентов вероятнее всего сделал это измерение?"

    a_prob = a*(d*10)
    b_prob = b*(e*10)
    c_prob = c*(f*10)

    max_prob = max(a_prob, b_prob, c_prob)

    answer = ""
    if a_prob == max_prob:
        answer += "Дима "
    if b_prob == max_prob:
        if len(answer) > 0:
            answer += "или "
        answer += "Егор"
    if c_prob == max_prob:
        if len(answer) > 0:
            answer += "или "
        answer += "Максим"
      

    task_answer = f"{answer}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")