from flask import *
import os
from utils.message import sendermessage,checkemilaccount
from utils.openconfigfile import *

app = Flask(__name__)
app.secret_key=os.urandom(8)  #session key
passwd="hahahaha"

@app.route('/')
def index():
   config_data=getconfigdata()
   if 'islogin' not in session:
       session['islogin']='0'
   return  render_template('index.html',sender=config_data['sender_email'])


@app.route('/result',methods=['POST'])
def note():
  try:
     email=request.form.get('email')
     title=request.form.get('title')
     note= request.form.get('note')
     config_data = getconfigdata()
     if sendermessage(config_data,email,title,note):
         return  render_template('result.html',receve=email,title=title,note=note)
     else:
         return render_template('index.html',result="email is wrong",sender=config_data['sender_email'])

  except:
       return  make_response("something wrong", 405)




@app.route('/login',methods=['GET','POST'])
def login():
     try:
       if request.method=='GET':
        if session['islogin'] =='1':
            return redirect(url_for('changee'))
        else:
            return render_template('login.html')
       elif request.method=='POST':
           if passwd==request.form.get('password'):
               session['islogin'] = '1'
               return redirect(url_for('changee'))

           else:
               return make_response("password error", 405)
     except:
         return make_response("something is wrong", 405)

@app.route('/changee',methods=['GET','POST'])
def changee():
    if request.method == 'GET':
        if session['islogin'] =='0' or 'islogin' not in session:
            return make_response("please login first", 405)
        elif  session['islogin'] =='1':
            return   render_template('csender.html')
    elif request.method == 'POST':
        try:
            smtpservice1=request.form['smtpservice']
            email=request.form['email']
            pwd=request.form['pwd']
            if checkemilaccount(smtpservice1,email,pwd):
                if setconfigdata(smtpservice1,email,pwd):
                  return  render_template('csender.html',results='change success')
                else:
                    return make_response("something is wrong", 405)
            else:
                return render_template('csender.html', results='wrong data')
        except:
            return make_response("something is wrong", 405)






if __name__ == '__main__':
    app.run()
