from flask import Flask
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from io import BytesIO
from flask import request, render_template, send_file , url_for
app = Flask(__name__)

@app.route("/")
def wel():
  return render_template('welcome.html')
@app.route("/index")
def index():
  return render_template("index.html")
@app.route("/submit",methods=['POST'])
def submit():
    a= map(int,request.form.getlist("Transport"))
    s1= sum(a)
    b= map(int,request.form.getlist("Housing"))
    s2= sum(b)
    c= map(int,request.form.getlist("Clothing"))
    s3= sum(c)
    d= map(int,request.form.getlist("Food"))
    s4= sum(d)
    e= map(int,request.form.getlist("Utilities"))
    s5= sum(e)
    f= map(int,request.form.getlist("Education"))
    s6= sum(f)
    g= map(int,request.form.getlist("Others"))
    s7= sum(g)
    x=['transport', 'housing', 'clothing', 'education', 'utilities', 'food', 'others']
    y= [s1, s2, s3, s4, s5 , s6 , s7]
    plt.figure()
    if request.form["graph"]=="normal" :
      plt.plot(x,y)
    elif request.form["graph"]=="bar" :
      plt.bar(x, y, width = 0.8, color = ['red', 'green'])
    elif request.form["graph"]=="scatter" :
      plt.scatter(x, y, label= "stars", color= "green",  
            marker= "*", s=30)



    
 
    plt.xlabel("expenses")
    plt.ylabel("spent")
    s=BytesIO()
    plt.savefig(s)
    s.seek(0)
    return send_file(s,mimetype="image/png") 

if __name__=="__main__":
  app.run(debug=True)
