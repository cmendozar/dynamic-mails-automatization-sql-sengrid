import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content,HtmlContent

def mail_json(from_email,to_email,subject,content):
    mail = Mail( Email(from_email), To(to_email), subject, Content('text/html',content) )
    return mail.get()


def sender(body):
    try:
        sg = SendGridAPIClient(os.environ.get(['SENGRID_KEY_API']))
        response = sg.client.mail.send.post(request_body = body)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print('failed') 
        #print(e.message)

if __name__ == '__main__':
    from_email = 'name1@example.com'
    to_email  = 'name2@example.com'
    subject = 'Sending with Twilio SendGrid is Fun'
    content = '<strong>and easy to do anywhere, even with Python</strong>'
    mail = mail_json(from_email,to_email,subject,content)
    sender(mail)




