import random

def generate_task7(task_doc, answer_doc, task_number):
    
    a = random.randint(1, 5)/10
    b = random.randint(1, 9-a*10)/10
    c = (10-(b*10)-(a*10))/10
    d = random.randint(1, 8)/10
    e = ((d*10) + random.randint(1, 9-d*10))/10

    task_text = f"В ночь перед экзаменом по математике студенту Дудкину с вероятностью {a} снится экзаменатор, с вероятностью {b} — тройной интеграл и с вероятностью {c} — то же, что и всегда. Если Дудкину снится преподаватель, то экзамен он сдает с вероятностью {d}, если тройной интеграл, то успех на экзамене ожидает его с вероятностью {e}. Если же Дудкину снится то же, что и всегда, то экзамен он точно «заваливает». Какова вероятность, что Дудкин сдаст математику в ближайшую сессию?"

    answer = ((a*10)*(d*10)+(b*10)*(e*10))/100

    task_answer = f"{answer}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")