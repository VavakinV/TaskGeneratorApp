import random

def generate_task4(task_doc, answer_doc, task_number):
    a = random.randint(5, 9)/10
    b = random.randint(5, 9)/10

    task_text = f"Два баскетболиста делают по одному броску мячом по корзине. Для первого спортсмена вероятность попадания равна {a}, для второго — {b}. Какова вероятность того, что в корзину попадут:\nа) оба игрока;\nб) хотя бы один из них;\nв) попадет только первый спортсмен?"

    a_answer = (a*10)*(b*10)/100
    b_answer = 1-((10-a*10)*(10-b*10)/100)
    c_answer = ((a*10)*(10-b*10))/100

    task_answer = f"а){a_answer}; б){b_answer}; в){c_answer}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")