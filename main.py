from dotenv import load_dotenv
# import os
import logging.config
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

load_dotenv('.env')
logging.config.fileConfig(fname='log.conf', disable_existing_loggers=False)
logger = logging.getLogger('Yahoo')

logger.info('Yahoo Mail Started')
# pass_ = os.environ.get('yahoo_app_password')

SMTP_SERVER = "smtp.mail.yahoo.com"
SMTP_PORT = 587
SMTP_USERNAME = "sebcin2001@yahoo.com"
SMTP_PASSWORD = "pass_"
EMAIL_FROM = "sebcin2001@yahoo.com"
EMAIL_TO = "setsebn@gmail.com"
EMAIL_SUBJECT = "REMINDER:"
co_msg = """
Hello sedat! Just wanted to send a friendly appointment
reminder for your appointment:
[Company]
Where: [companyAddress]
Time: [appointmentTime]
Company URL: [companyUrl]
Change appointment?? Add Service??
change notification preference (text msg/email)
"""


def send_email():
    logger.info('Send Mail Started')
    msg = MIMEText(co_msg)
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    debuglevel = True
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.set_debuglevel(debuglevel)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    try:
        logger.info('pass:', SMTP_PASSWORD)
        logger.info('Connecting to Server...')
        mail.login(SMTP_USERNAME, SMTP_PASSWORD)
        logger.info('pass:', SMTP_PASSWORD)
        mail.ehlo()
        mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    except Exception as e:
        logger.error('Error : ', e)
    else:
        logger.info('Mail sent')
    mail.quit()


def send_email_attachment():
    logger.info('Send Mail with attachment Started')
    attachment = 'train.csv'
    msg = MIMEMultipart()
    msg['Subject'] = EMAIL_SUBJECT
    msg['Body'] = 'find attachment below'
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    mail = MIMEBase('application', "octet-stream")
    mail.set_payload(open(attachment, "rb").read())

    logger.info(f'File {attachment} attached to email')
    encoders.encode_base64(mail)
    mail.add_header('Content-Disposition', 'attachment', filename=attachment)
    msg.attach(mail)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            logger.info('Connecting to Server...')
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        logger.error('Error : ', e)
    else:
        logger.info('Mail sent with attachment')


if __name__ == '__main__':
    send_email()
