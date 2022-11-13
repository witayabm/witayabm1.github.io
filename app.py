from flask import Flask,render_template,request,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,RadioField,SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
Bootstrap(app)

class MyForm(FlaskForm):
    name = StringField("ป้อนชื่อของคุณ",validators=[DataRequired()])
    isAccept= BooleanField("ยอมรับเงื่อนไขบริการข้อมูล")
    gender = RadioField('เพศ',choices=[('male','ชาย'),('female','หญิง')])
    skill = SelectField('ความสามารถพิเศษ',choices=[('พูดภาษาอังกฤษ','พูดภาษาอังกฤษ'),('ร้องเพลง','ร้องเพลง')])
    submit = SubmitField("บันทึก")

@app.route("/",methods=['GET',"POST"])
def index():
    session['name'] = False
    form = MyForm()
    if form.validate_on_submit():
        flash("บันทึกข้อมูลเรียบร้อย")
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender'] = form.gender.data
        session['skill'] = form.skill.data
        # ลบข้อมูล
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
        form.skill.data = ""

    return render_template("index.html", form=form, )

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/admin")
def profile():
    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True) 