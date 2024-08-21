import random
import math
import scipy.stats as stats
from scipy.special import erf

def phi(x):
    return stats.norm.cdf(x)

def generate_task10(task_doc, answer_doc, task_number):

    a = random.randint(1, 9)/10
    b = random.randint(25, 75)*2
    c = random.randint(int(b*a)-4, int(b*a)+4)

    task_text = f"Вероятность выхода из строя за время Т одного конденсатора равна {a}. Определить вероятность того, что за время Т из {b} конденсаторов, работающих независимо, выйдут из строя:\nа) не менее {c} конденсаторов;\nб) ровно половина."

    n = b
    p = a
    mean = n*p
    std_dev = (n*p*(1-p))**0.5

    x1 = (c - 0.5 - mean) / std_dev
    x2 = (n + 0.5 - mean) / std_dev
    
    a_answer = phi(x2) - phi(x1)

    std_dev = (n//2 - n*p)/math.sqrt(n*p*(1-p))

    b_answer = (1 / math.sqrt(2 * math.pi)) * math.exp(-(std_dev ** 2) / 2)

    task_answer = f"а)Φ({round(x2, 4)}) - Φ({round(x1, 4)}) ~ {round(a_answer, 4)}; б) φ({round(std_dev, 4)}) ~ {round(b_answer, 4)}"
    
    task_doc.add_paragraph(f"{task_number}) {task_text}")
    answer_doc.add_paragraph(f"{task_number}) {task_answer}")