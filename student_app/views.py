
from .models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render,redirect
from mysql.connector import connect, Error
from django.contrib import messages
# Create your views here.




def registeruser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.info(request,'email already exists')
            return redirect('register')
        else:
            u=User()
            u.email=email
            u.password=password
            u.save()        
        return HttpResponse("Registration Successful!")
    else:
        return render(request, 'register.html')



def loginuser(request):
    try:
        if request.method=="POST":
            email = request.POST.get('email')
            password = request.POST.get('password')
            result=User.objects.all()

            for reg in result:
                if reg.email == email and reg.password == password:
                    return render(request,"index.html")
            return HttpResponse("invalid email or password")
        else:
            return render(request,"login.html")
    except Exception as e:
        return HttpResponse(e)

def connection():
    try:
        con = connect(
            host="localhost",
            user="root",
            password="system",
            database="dbstudent"
        )
        return con
    except Error as e:
        return HttpResponse(f"Error : {e}")





def index(request):
    return render(request, 'index.html')


def insertdata(request):
    if request.method == "POST":
        try:
            rno = int(request.POST.get('rno'))
            nm = request.POST.get('nm')
            c = int(request.POST.get('c'))
            cpp = int(request.POST.get('cpp'))
            py = int(request.POST.get('py'))

            con = connection()
            if con is not None:
                cursor = con.cursor()
                cursor.callproc('insert_student', (rno, nm, c, cpp, py))
                con.commit()
                cursor.close()
                con.close()
                # return redirect('index') 
                return HttpResponse("record inserted..") # Redirect to the index page
            else:
                return HttpResponse("Connection failed.")
        except Error as e:
            return HttpResponse(f"Error: {e}")
    else:
        return render(request, 'insert.html')

def updatedata(request):
    if request.method == 'POST':
        try:
            rno = int(request.POST.get('rno')) 
            nm = request.POST.get('nm')
            c = int(request.POST.get('c'))
            cpp = int(request.POST.get('cpp'))
            py = int(request.POST.get('py'))    

            con = connection()
            if con is not None:
                cursor = con.cursor()
                cursor.callproc('update_student', (rno, nm, c, cpp, py))
                con.commit()
                cursor.close()
                con.close()
                # return redirect('index')  # Redirect to the index page

                return HttpResponse("Record updated")
            else:
                return HttpResponse("Connection failed")
        except Error as e:
            return HttpResponse(f"Error: {e}")
    else:
        return render(request, 'update.html')




def searchdata(request):
    try:
        if request.method == "POST":
            rno = int(request.POST.get('rno'))
            con = connection()

            if con is not None:
                cursor = con.cursor()
                cursor.callproc('search_student', (rno,))

                student_data = None
                for result in cursor.stored_results():
                    student_data = result.fetchall()

                cursor.close()
                con.close()


                if student_data:
                    return render(request, "search.html", {"students": student_data, "searched": True})
                else:
                    return render(request, "search.html", {"students": None, "searched": True})
            else:
                return HttpResponse("Connection failed.")
        else:
            return render(request, "search.html", {"searched": False})
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

def deletedata(request):
    if request.method == "POST":
        try:
            rno = int(request.POST.get('rno'))
            
            con = connection()
            if con is not None:
                cursor = con.cursor()
                cursor.callproc('delete_student', (rno,))
                con.commit()
                cursor.close()
                con.close()

                return HttpResponse("Record deleted successfully.")
            else:
                return HttpResponse("Connection failed.")
        except Error as e:
            return HttpResponse(f"Error occurred: {str(e)}")
    else:
        return render(request, 'delete.html')







def top_scorers(request):
    con = connection()
    cursor = con.cursor()
    try:
        sql = """ 
        SELECT *  
        FROM tblstudent
        ORDER BY (c_marks + cpp_marks + python_marks) DESC
        LIMIT 3
        """
        
        cursor.execute(sql)
        rows = cursor.fetchall()
        listrecord=[]
        for row in rows:
            rno,nm,c,cpp,py=row
            total=c+cpp+py
            listrecord.append((rno,nm,c,cpp,py,total))
        return render(request, 'top3.html', {'records': listrecord})
    except Error as e:
        return HttpResponse(e)



