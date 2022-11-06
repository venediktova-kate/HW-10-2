from flask import Flask

from utils import *

# Загружаем информацию о кандидатах в список из файла
candidates = load_candidates('candidates.json')

app = Flask(__name__)


# Создаем представление для главной страницы и выводим информацию о всех кандидатах
@app.route("/")
def page_index():
    return get_all(candidates)


# Создаем представление для кандидата по номеру
@app.route("/candidate/<int:pk>/")
def page_candidate(pk):
    return get_by_pk(candidates, pk)


# Создаем представление для страницы по навыку, выводим информацию о всех кандидатах с навыком
@app.route("/skills/<x>")
def page_skills(x):
    return get_by_skill(candidates, x)


app.run(host='0.0.0.0', port=8000)
