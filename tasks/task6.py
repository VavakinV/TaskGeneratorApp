import random

def generate_task6(task_doc, answer_doc, task_number):
    
    a = random.randint(3, 8)
    b = random.randint(1, a)
    
    task_text = f"Работа некоторого устройства прекращается, если из строя выходит 1 из {a} элементов. Последовательная замена каждого элемента новым производится до тех пор, пока устройство не начнет работать. Какова вероятность того, что придется заменить ровно {b} элемент{'' if b == 1 else 'а' if b < 5 else 'ов'}?"

    task_answer = f"1/{a}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")