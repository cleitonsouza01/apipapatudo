import os
from typing import Union

from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()

import smtplib
from email.message import EmailMessage


load_dotenv()
try:
    EMAIL_SOURCE = os.environ["email_source"]
    EMAIL_PASSWORD = os.environ["email_source_pass"].replace('"', '')
except:
    raise Exception("Erro ao ler variaveis de ambiente")


def send_email(destinatario, assunto, mensagem):
    msg = EmailMessage()

    msg['Subject'] = assunto
    msg['From'] = EMAIL_SOURCE
    msg['To'] = destinatario

    msg.set_content(mensagem)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_SOURCE, EMAIL_PASSWORD)
        smtp.send_message(msg)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# post send email
@app.post("/send_email")
def send_email_post(destinatario: str, assunto: str, mensagem: str):
    send_email(destinatario, assunto, mensagem)
    return {"destinatario": destinatario, "assunto": assunto, "mensagem": mensagem}
