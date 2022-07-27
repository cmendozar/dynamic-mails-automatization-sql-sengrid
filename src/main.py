from data.sql import SQL
from utils.preprocessing import call_to_action, capital_name
from utils.sender import mail_json, sender


#CREATE CONECTION TO ODS_PSS AND GET QUERY 

ODS = SQL('YOUR_OPERATIONAL_DATA_STORE')
data= ODS.get_query_df(file = 'src/data/queries/query.sql')


# Define sender email.
sender_email = 'name@example.com'

#opean an read the template html mail to send.
with open('src/templates/example.html',"r",encoding="utf-8") as html_file:
    html_file = html_file.read()

# this is a for loop to end for every contact in data. 
for item in range(len(data)):

    #define the dynamics variables 
    email = data.email[item]
    first_name = capital_name(data.first_name[item])
    last_name = data.last_name[item]
    pnr = data.pnr[item]
    link = call_to_action(pnr,last_name)

    subject = 'Hola {} listo para tu compra'.format(first_name)

    #configure and define the mail
    mail = mail_json( sender_email, email, subject, html_file.format(**locals()))
    #send the mail
    sender(mail)

    print('The email has been sended to {}, count: {} emails sended'.format(data.email[item],item+1))
