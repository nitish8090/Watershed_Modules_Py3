from flask import Flask, render_template
from shp_display import *

app = Flask(__name__)


def script():
    return ['hades2']


def get_table(db):
    db = db

    script = "<table>"
    # Header Generator
    code = "<tr>"
    for s in db:
        if str(s) != "MULTIPOLYGON" and str(s) != 'geometry':
            code = code + "<th>" + str(s) + "</th>"
    script = script + code

    # Data Generator
    for i in range(len(db.index)):
        code = "<tr>"
        for item in list(db.loc[i]):
            if not str(item).startswith("MULTIPOLYGON") and not str(item).startswith("POLYGON "):
                code = code + "<td>" + str(item) + "</td>"
        code = code + "</tr>"
        script = script + code
    script = script + "</table>"
    return script


@app.route('/')
def index():
    value = script()

    return render_template('index.html',
                           entry1=value[0],
                           path_to_image=some[0],
                           lis=some[1].shape,
                           table_n=get_table(some[1])
                           )


@app.route('/up_pop')
def up_pop():
    some = get_file()
    return render_template('up_population.html',
                           table_n=get_table(some[1]),
                           path_to_image=some[0])


if __name__ == "__main__":
    app.run(debug=True, host='10.68.69.29')
