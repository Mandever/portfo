from flask import Flask, render_template, url_for, request, redirect
import csv
# con render puedo enviar documentos html
app = Flask(__name__)
print(__name__)


"""
@app.route('/<username>/<int:post_id>')
def hello_world(username=None, post_id=None):  # None seria el valor de default
    return render_template("index.html", name=username, post_id=post_id)
    # El documento "index.html" se debe de guardar en una carpeta con el nombre "templates"
    # para que asi 'render_template' pueda ejecutar la accion de enseñar en pantalla
"""


@app.route('/')
def my_home():  # None seria el valor de default
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):  # lo que hace es que cuando se selecciona algo de la web, busca lo que se pone despues de / en los archivos html
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=",",
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'No se ha salvado los datos'
    else:
        return 'Algo salio mal. Intentalo otra vez!'


# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'Este es mi perro'

# (257) <- Ultimo video visto(28/09/2020)
# (268) <- Ultimo video cisto(29/09/2020)
# (273) <- Ultimo video visto(29/09/2020), seccion de GitHub
