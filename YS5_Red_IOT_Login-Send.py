#importing the Yagmail library
!pip install yagmail #Install this line in Command Prompt
import yagmail

def login():
  #Creation of user1 with a 6 digit password
  user1 = "Andy"
  pw1 = "123a@S"

  #Key to exit while loop and error key to stop new login
  key = True
  ekey = 0

  #Loop for login
  while key == True:
    print("Enter your login information")
    user = input("Enter your username: ")
    pw = input("Enter your password: ")
    if user == user1 and pw == pw1:
      key = False
      print("login successful... Welcome to your SMART LIGHT")
    else:
      print("Error username or password incorrect...")
      ekey+=1 
    if ekey == 3: 
      key = False
def sende():
  try:
    #initializing the server connection
    yag = yagmail.SMTP(user='ys5red2@gmail.com', password='ltbcomkwymjrwqfd')
    #sending the email
    yag.send(to='ys5red2@gmail.com', subject='Smart Life - Smart Living', 
             contents='<img src="https://images.unsplash.com/photo-1606812667169-0e1991ed3742?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80" alt="Lightbuld" width="70" height="60"> <br></br>' + 
             '<h2> Due to the unexpected breach, we are requiring a mandatory password change. ' +
             '</h2> <br></br> Please verify username and old password to recive a temporary password link to reset your password.')
    print("Email sent successfully")
  except:
    print("Error, email was not sent")

#comment out as needed
login()
sende()