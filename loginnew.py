import sqlite3
conn=sqlite3.connect('login system.sqlite')
cur=conn.cursor()
def login():
    while(True):
     username=input('USERNAME:')
     password=input('PASSWORD:')
     user=('SELECT * FROM userdata WHERE username=? AND password=?')
     cur.execute(user,[(username),(password)])
     output=cur.fetchall()
     if output:
       print('welcome')
       break
     else:
       print('wrong username or password')
       a=input('IF YOU WANT TO SIGN UP PRESS S\n IF YOU WANT TO TRY AGAIN PRESS ANY KEY\n IF YOU WANT TO STOP PRESS n\n')
       if(a=='s'):
         while(True):
           new_username=input('Enter your username\n')
           new_password=input('Enter your password\n')
           confirm_password=input('Re-enter your password\n')
           if(new_password!=confirm_password):
               print('passwords does not match')
               continue
           new_user=('SELECT * FROM userdata WHERE username=?')
           cur.execute(new_user,[(new_username)])
           result=cur.fetchall()
           if result:
               print('user already exists \n please try again')
               continue
           else:
               new_data=('INSERT INTO userdata(username,password)VALUES(?,?)')
               cur.execute(new_data,[(new_username),(new_password)])
               conn.commit()
               print('Account Successfully Created')
               break
     if(a=='n'):
      print('thank you')
      break
def signup():
    while(true):
     new_username=input('Enter your username\n')
     new_password=input('Enter your password\n')
     confirm_password=input('Re-enter your password\n')
     if(new_password!=confirm_password):
        print('passwords does not match')
        continue
     new_user=('SELECT * FROM userdata WHERE username=?')
     cur.execute(new_user,[(new_username)])
     result=cur.fetchall()
     if result:
        print('user already exists \n please try again')
        continue
     else:
        new_data=('INSERT INTO userdata(username,password)VALUES(?,?)')
        cur.execute(new_data,[(new_username),(new_password)])
        conn.commit()
        print('Account Successfully Created')
        break
while(True):
 inp=input('press s for sign up and l for login')
 inp.lower()
 if(inp=='l'):
    login()
    break
 elif(inp=='s'):
    signup()
    break
 else:
    print("please choose a walid option")
