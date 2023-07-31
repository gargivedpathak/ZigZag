from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///ZigZagbd.sqlite3"
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()


class Cafe(db.Model):
    __tablename__ = 'cafes'
    cid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    cname = db.Column(db.String, nullable=False)
    cdesc = db.Column(db.String)
    clocation = db.Column(db.String, nullable=False)
    cstreet = db.Column(db.String)
    cpin = db.Column(db.Integer)
    ctimings = db.Column(db.String)
    cwebsite = db.Column(db.String)
    cprice = db.Column(db.Integer)
    cratings = db.Column(db.Integer)
    cimg = db.Column(db.String)
    

class Shopping(db.Model):
    __tablename__ = 'shopping'
    sid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sname = db.Column(db.String, nullable=False)
    sdesc = db.Column(db.String)
    stype = db.Column(db.String)
    scontact = db.Column(db.String)
    saddress = db.Column(db.String, nullable=False)
    slocation = db.Column(db.String, nullable=False)
    sstreet = db.Column(db.String)
    spin = db.Column(db.Integer)
    swebpage = db.Column(db.String)
    sprice = db.Column(db.Integer)
    simg = db.Column(db.String)
   
class Tourist(db.Model):
    __tablename__ = 'tourists'
    tid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tname = db.Column(db.String, nullable=False)
    tdesc = db.Column(db.String)
    tlocation = db.Column(db.String, nullable=False)
    tstreet = db.Column(db.String)
    tpin = db.Column(db.Integer)
    ttimings = db.Column(db.String)
    tcontact = db.Column(db.String)
    tprice = db.Column(db.Integer)
    timg = db.Column(db.String)

class Hostel(db.Model):
    __tablename__ = 'hostels'
    hid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    hname = db.Column(db.String, nullable=False)
    hdesc = db.Column(db.String)
    htype = db.Column(db.String)
    hcontact = db.Column(db.String)
    hlocation = db.Column(db.String, nullable=False)
    hstreet = db.Column(db.String)
    hpin = db.Column(db.Integer)
    hamentities = db.Column(db.String)
    hpeople = db.Column(db.String)
    hkm = db.Column(db.Integer)
    hmin = db.Column(db.Integer)
    hprice = db.Column(db.String, nullable=False)
    himg = db.Column(db.String)
    
class Feedback(db.Model):
    __tablename__ = 'feedback'
    fid = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String, nullable=False)
    femail = db.Column(db.String, nullable=False)
    fphone = db.Column(db.String, nullable=False)
    fsubject = db.Column(db.String, nullable=False)
    fmessage = db.Column(db.String, nullable=False)


@app.route("/", methods=["GET", "POST"])
def zigzag():
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        search = request.form['name']
        print(search)
        f= Cafe.query.filter_by(cname=search).all()
        if len(f) != 0:
            return render_template("cafelist.html", cafes = f)
        else:
            f = Shopping.query.filter_by(sname=search).all()
            if len(f) != 0:
                return render_template("shoppinglist.html", shopping = f)
            else:
                f = Hostel.query.filter_by(hname=search).all()
                if len(f) != 0:
                    return render_template("hostellist.html", hostels = f)
                else:
                    f = Tourist.query.filter_by(tname=search).all()
                    return render_template("touristlist.html", tourists = f)
               
        print(f)
        

@app.route("/cafelist", methods=["GET", "POST"])
def cafe():
    cafes = Cafe.query.all()
    for i in cafes:
        print(i.cimg)
    return render_template("cafelist.html", cafes = cafes)

@app.route("/shoppinglist", methods=["GET", "POST"])
def shopping():
    shopping = Shopping.query.all()
    return render_template("shoppinglist.html", shopping = shopping)

@app.route("/touristlist", methods=["GET", "POST"])
def tourist():
    tourists = Tourist.query.all()
    return render_template("touristlist.html", tourists = tourists)

@app.route("/hostellist", methods=["GET", "POST"])
def hostel():
    hostels = Hostel.query.all()
    return render_template("hostellist.html", hostels = hostels)

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "GET":
        return render_template("feedback.html")
    elif request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        subj = request.form['subject']
        mes = request.form['message']

        f = Feedback(fname = name, femail = email, fphone = phone, fsubject = subj, fmessage = mes)
        db.session.add(f)
        db.session.commit()


        return redirect(url_for('zigzag'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug= True, port= 8000 )