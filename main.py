from flask import *
import mysql.connector


ab=mysql.connector.connect(host="localhost",user="root",password="Root@123",database="abc")
crs=ab.cursor()
app = Flask(__name__)
gg=[[]]
@app.route('/')
def hello_worlda():
   return render_template('index.html')
@app.route('/login',methods=['POST'])
def hello_world():
   if(request.method=='POST'):
      a=request.form['u']
      b=request.form['p']
      sql="select role,name from users where user_id=%s and passwd=%s;"
      val=a,b
      crs.execute(sql,val)
      gg=crs.fetchall()
      try:
         if(len(gg)==1): 
            if(gg[0][0]=='admin'):
               return render_template('adminmain.html',user=gg[0][1],userrole=gg[0][0])
            elif(gg[0][0]=='student'):
               return render_template('usermain.html',user=gg[0][1],userrole=gg[0][0])
            elif(gg[0][0]=='faculty'):
               return render_template('facultymain.html',user=gg[0][1],userrole=gg[0][0])
         else:
            erro="The User Id And else Password is Incorrect"
            return render_template('index.html',erro=erro)
      except:
         erro="The User Id And Password is Incorrect"
         return render_template('index.html',erro=erro)

@app.route('/COURSE_BRANCH')
def admin_course():
   return render_template('admin_course.html')  
@app.route('/EXAM')
def admin_exam():
   return render_template('admin_exam.html')  
@app.route('/FACULTY')
def admin_faculty():
   return render_template('admin_faculty.html')  
@app.route('/FEES')
def admin_fees():
   return render_template('admin_fees.html')
@app.route('/HOSTEL')
def admin_hostel():
   return render_template('admin_hostel.html')  
@app.route('/LIBRARY')
def admin_library():
   return render_template('admin_library.html')  
@app.route('/NOTICE')
def admin_notice():
   return render_template('admin_notice.html')

@app.route('/RESULT',methods=['POST'])
def admin_result():
   ctr=0
   abc=request.form['ct']
   return render_template('abc.html',ctr=abc)  
@app.route('/ROOM')
def admin_room():
   return render_template('admin_room.html')
@app.route('/STUDENT')
def admin_student():
   return render_template('admin_student.html')  

@app.route('/TIME_TABLE')
def admin_add_timetable():
   return render_template('admin_timetable.html',b=['m','m','m','m','m','m'],a=[['a','a','a','a','a','a','a'],['a','a','a','a','a','a','a'],['a','a','a','a','a','a','a'],['a','a','a','a','a','a','a'],['a','a','a','a','a','a','a'],['a','a','a','a','a','a','a']])  
@app.route('/TRANSPORT')
def admin_transport():
   return render_template('admin_transport.html')  



@app.route('/loadurl',methods=['POST'])
def Url_fetching():
   admin=request.form['abc']
   return render_template('adminmain.html',frame="/"+admin)   
@app.route('/loadstu',methods=['POST'])
def Url_stu_fetching():
   stu=request.form['abc']
   return render_template('usermain.html',frame="/"+stu)
@app.route('/loadfac',methods=['POST'])
def Url_fac_fetching():
   fac=request.form['abc']
   return render_template('facultymain.html',frame="/"+fac)
if __name__ == '__main__':
    app.run()
    

print(crs.fetchall())
