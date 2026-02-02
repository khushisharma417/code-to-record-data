k=int(input("Press 1 for result result,2 for insert data : "))

import mysql.connector
# MySQL se connection
conn = mysql.connector.connect(
        host="127.0.0.1",  # Force IPv4
        user="root",
        password="khushi",
        database="day7",
        port=3306,
        auth_plugin="mysql_native_password",
        use_pure=True,
        connection_timeout=5
)
cursor = conn.cursor()
def insert():
    roll=int(input("Enter Rollno  : "))
    name=input("Enter name : ")
    branch=input("Enter branch. : ")
    c=eval(input("Enter marks of C : "))
    cpp=eval(input("Enter maks of cpp : "))
    py=eval(input("Enter marks of python : "))
    total=c+cpp+py
    # print("total : ",total)    
    percentage=total/3
    # pass/fail
    if percentage>=33:
        x="Pass"
    else:
        x="Fail"    
    # print(x)    
    sql='''insert into records1 
    values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    values=(roll,name,branch,c,cpp,py,total,percentage,x)
    cursor.execute(sql,values)
    conn.commit()
    print("Data inserted")

def d_result():
    roll=int(input("Enter Rollno  : "))

    rollno=(roll,)
    # r=str(rollno)
    a='''select name from records1 where rollno=%s'''
    cursor.execute(a,(rollno))
    name=cursor.fetchone()
    b='''select branch from records1 where rollno=%s'''
    cursor.execute(b,(rollno))
    branch=cursor.fetchone()
    c='''select C from records1 where rollno=%s'''
    cursor.execute(c,(rollno))
    C=cursor.fetchone()
    d='''select Cpp from records1 where rollno=%s'''
    cursor.execute(d,(rollno))
    Cpp=cursor.fetchone()
    e='''select Python from records1 where rollno=%s'''
    cursor.execute(e,(rollno))
    Py=cursor.fetchone()
    t='''select Total from records1 where rollno=%s'''
    cursor.execute(t,(rollno))
    Total=cursor.fetchone()
    per='''select Percentage from records1 where rollno=%s'''
    cursor.execute(per,(rollno))
    per=cursor.fetchone()
    q='''select pf from records1 where rollno=%s'''
    cursor.execute(q,(rollno))
    result=cursor.fetchone()  

    # print("result :",result)
    
    #for file
    na=str(name[0])
    r=str(roll)
    m=str(C[0])
    n=str(Cpp[0])
    o=str(Py[0])
    to=str(Total[0])
    p=str(per[0])
    res=str(result[0])
    br=str(branch[0])
    file=r
    f=open(file+".txt","w")
    f.write("Name : "+na+"\nRollno : "+r+"\nBranch : "+br+"\n-------Marks---------"+"\nC :"+m+"\nCPP "+n+"\nPython : "+o+"\nTotal : "+to+"\nPercentage : "+p+"\nResult : "+res) 
    f.close()
    print("file generated : ",file+".txt" ) 
if k==1:
    d_result()
elif k==2:
    insert()
else:
    print("invalid input")        
conn.close()