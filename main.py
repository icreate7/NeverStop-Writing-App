from flask import Flask, render_template, url_for, redirect
from flask.cli import load_dotenv
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor, CKEditorField
from flask_wtf import FlaskForm
from wtforms.fields.simple import SubmitField, TextAreaField
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')  # Required for FlaskForm to work
ckeditor = CKEditor(app)
Bootstrap5(app)


class WriteForm(FlaskForm):
    typed_content = TextAreaField("Keep typing....")


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/write', methods=["GET"])
def write_text():
    form = WriteForm()
    return render_template("write.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)