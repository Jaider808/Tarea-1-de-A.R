from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)

@app.route('/person_delete/<string:id_person>')
def people_delete(id_person):
    for person_delete in model:
        if person_delete.id_person==id_person:
            model.remove(person_delete)
    return render_template('person_detail.html', value="Was delete")


@app.route('/person_update/<string:id_person>')
def people_update(id_person):
    persona = None
    for person_update in model:
        if person_update.id_person==id_person:
            persona = person_update
            break
    return render_template('person_update.html',value=persona)


@app.route('/person_updated', methods=['POST'])
def people_updated():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    for person_updated in model:
        if person_updated.id_person==id_person:
            person_updated.name = first_name
            person_updated.last_name = last_name
            break
    return render_template('person_detail.html', value = "Was updated")



if __name__ == '__main__':
    app.run()