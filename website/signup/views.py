from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pn=''
dob=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pn,dob,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="gaurav",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="phone":
                pn=value
            if key=="dob":
                dob=value
            if key=="password":
                pwd=value
        
        c="insert into users Values('{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,s,em,pn,dob,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')