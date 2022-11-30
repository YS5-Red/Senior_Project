#Importing modules/packages
import smtplib
import imaplib
import email
import traceback 

#Defining email used to send phishing attack
FROM_EMAIL = "ys5red2@gmail.com"
#Using APP password to log into gmail
FROM_PWD = "ltbcomkwymjrwqfd" 
#Connecting to Internet Message Access with gmeil.com
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993

#Reading the emails in gmail
def read_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER) #Connecting to server, using the logins from above, and targeting 'inbox
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, '(SUBJECT "Smart Life - Smart Living")') #Sifting emails for targeted subject
        mail_id = data[1]
        id_list = mail_id[0].split()   
        first_email = int(id_list[0]) #Making a list of the emails
        latest_email = int(id_list[-1])

        for i in range(latest_email, first_email, -1): #Searching through emails and fetching requirements
            data = mail.fetch(str(i), '(RFC822)' )
            for response in data:
                array = response[0]
                if isinstance(array, tuple): #Traversing data list of emails
                    msg = email.message_from_string(str(array[1],'utf-8')) #Pulling email message
                    e_subject = msg['subject'] #Pulling subject
                    e_from = msg['from'] #Pulling from whom
                    e_body = str(msg.get_payload(0)) #Pulling email body

                    print('From : ' + e_from + '\n')
                    print('Subject : ' + e_subject + '\n')
                    print('Body: ' + e_body + '\n')
    except Exception as e:
      print(str(e))

#Solution algorithm to authenticate emails
def solve_email():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER) #Connecting to email server and logging in
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, '(SUBJECT "Smart Life - Smart Living")') #Selecting suspicious emails
        mail_id = data[1]
        id_list = mail_id[0].split() #Creating list of emails from subject
        first_email = int(id_list[0])
        latest_email = int(id_list[-1])

        for i in range(latest_email, first_email, -1): #Traversing email list
            data = mail.fetch(str(i), '(RFC822)' )
            for response in data: 
                array = response[0]
                if isinstance(array, tuple): #Checking if message from component is credible
                    msg = email.message_from_string(str(array[1],'utf-8'))
                    e_from = msg['from']
                    #Checking to see if the domain is from an organization or business
                    if e_from.__contains__('.inc') or e_from.__contains__('.org') or e_from.__contains__('.net'): 
                      print('Credible')
                    else:
                      print('DO NOT TRUST ' + e_from)
    except Exception as e:
      print(str(e))

#Calling functions
read_gmail()
solve_email()