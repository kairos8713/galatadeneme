from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/emreercan/Documents/Web Projects/Egepres/database.db'
db = SQLAlchemy(app)
app.app_context().push()
@app.route("/")
def main():
	return render_template("main.html")
@app.route("/hakkımızda")
def hakkımızda():
	return render_template("hakkımızda.html")
@app.route("/menü")
def ürünlerimiz():
	return render_template("menü.html")
@app.route("/yemekmenü")
def yemekmenü():
	return render_template("ymenü.html")
@app.route("/içecekmenü")
def içecekmenü():
	return render_template("dmenü.html")
@app.route("/nargilemenü")
def nargilemenü():
    ürünler = nargile.query.all()
    return render_template("nmenü.html", ürünler = ürünler)
@app.route("/kahvaltı")
def kahvaltı():
    ürünler = Kahvalti.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/aparatif")
def aparatif():
    ürünler = aparatif.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/hamburger")
def hamburger():
    ürünler = hamburger.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/pizza")
def pizza():
    ürünler = pizza.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/makarna")
def makarna():
    ürünler = makarna.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/salata")
def salata():
    ürünler = salata.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/ana_yemek")
def yemek():
    ürünler = yemek.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/sıcak_içecek")
def sıcakiç():
    ürünler = sıcak.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/sıcak_kahve")
def sıcakka():
    ürünler = sıcak2.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/soğuk_içecek")
def soğukiç():
    ürünler = soğuk.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/soğuk_kahve")
def soğukka():
    ürünler = soğuk2.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/meşrubat")
def meşrubat():
    ürünler = meşrubat.query.all()
    return render_template("kahvaltı.html", ürünler = ürünler)
@app.route("/admin")
def admin():
    kahvaltı = Kahvalti.query.all()
    apara = aparatif.query.all()
    hamb = hamburger.query.all()
    pizz = pizza.query.all()
    maka = makarna.query.all()
    sala = salata.query.all()
    yeme = yemek.query.all()
    tatl = tatlı.query.all()
    sıiç = sıcak.query.all()
    sıka = sıcak2.query.all()
    soiç = soğuk.query.all()
    soka = soğuk2.query.all()
    meşr = meşrubat.query.all()
    narg = nargile.query.all()
    return render_template("admin.html",kahvaltı = kahvaltı,apara = apara,hamb = hamb,pizz = pizz,maka = maka,sala = sala,yeme = yeme,tatl = tatl,sıiç = sıiç,sıka = sıka,soiç = soiç,soka = soka,meşr = meşr,narg=narg)
@app.route("/add",methods = ["POST"])
def addürün():
    yeni = bos()
    isim = request.form.get("isim")
    fiyat = request.form.get("fiyat")
    resim = request.form.get("resim")
    dba = request.form.get("tables")
    print(dba)
    if len(isim) > 0:
        if len(fiyat) > 0:
            if len(dba) > 0:
                dba = str(dba)
                if dba == "Kahvaltı":
                    yeni = Kahvalti(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Aparatif":
                    yeni = aparatif(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Hamburger":
                    yeni = hamburger(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Pizza":
                    yeni = pizza(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Makarna":
                    yeni = makarna(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Salata":
                    yeni = salata(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Yemek":
                    yeni = yemek(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Tatlı":
                    yeni = tatlı(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Sıcak İçecek":
                    yeni = sıcak(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Sıcak Kahve":
                    yeni = sıcak2(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Soğuk İçecek":
                    yeni = soğuk(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Soğuk Kahve":
                    yeni = soğuk2(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Meşrubat":
                    yeni = meşrubat(resim = resim,fiyat=fiyat,isim=isim)
                elif dba == "Nargile":
                    yeni = nargile(resim = resim,fiyat=fiyat,isim=isim)
                db.session.add(yeni)
                db.session.commit()
    return redirect(url_for("admin"))

@app.route("/change/<string:dba>/<string:id>",methods = ["POST"])
def changeürün(dba,id):
    dba = str(dba)
    yeni = bos()
    fiyat = request.form.get("fiyat")
    if dba == "kahvaltı":
        yeni = Kahvalti.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "tost":
        yeni = aparatif.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "hamburger":
        yeni = hamburger.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "pizza":
        yeni = pizza.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "makarna":
        yeni = makarna.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "salata":
        yeni = salata.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "yemek":
        yeni = yemek.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "tatlı":
        yeni = tatlı.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "sıcak_içecek":
        yeni = sıcak.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "sıcak_kahve":
        yeni = sıcak2.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "soğuk_içecek":
        yeni = soğuk.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "soğuk_kahve":
        yeni = soğuk2.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "meşrubat":
        yeni = meşrubat.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    elif dba == "nargile":
        yeni = nargile.query.filter_by(id = id).first()
        yeni.fiyat = fiyat
    
    
    db.session.commit()
    return redirect(url_for("admin"))

@app.route("/changer/<string:dba>/<string:id>",methods = ["POST"])
def changeresim(dba,id):
    dba = str(dba)
    yeni = bos()
    fiyat = request.form.get("Resim")
    if dba == "kahvaltı":
        yeni = Kahvalti.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "tost":
        yeni = aparatif.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "hamburger":
        yeni = hamburger.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "pizza":
        yeni = pizza.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "makarna":
        yeni = makarna.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "salata":
        yeni = salata.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "yemek":
        yeni = yemek.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "tatlı":
        yeni = tatlı.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "sıcak_içecek":
        yeni = sıcak.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "sıcak_kahve":
        yeni = sıcak2.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "soğuk_içecek":
        yeni = soğuk.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "soğuk_kahve":
        yeni = soğuk2.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "meşrubat":
        yeni = meşrubat.query.filter_by(id = id).first()
        yeni.resim = fiyat
    elif dba == "nargile":
        yeni = nargile.query.filter_by(id = id).first()
        yeni.resim = fiyat
    
    
    db.session.commit()
    return redirect(url_for("admin"))


class Kahvalti(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer())
    isim = db.Column(db.String())
    resim = db.Column(db.String())
class aparatif(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())    
class hamburger(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())
class pizza(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())
class makarna(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())
class salata(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())
class yemek(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())
class tatlı(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())
class sıcak(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())
class sıcak2(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())
class soğuk(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())
class soğuk2(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())
class meşrubat(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String())
class nargile(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    fiyat = db.Column(db.Integer)
    isim = db.Column(db.String)
    resim = db.Column(db.String)
class bos(db.Model):
    id = db.Column(db.Integer,primary_key=True)
db.create_all()
if __name__ == "__main__":
	app.run(debug=True)