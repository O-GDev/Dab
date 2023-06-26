from typing import List

from fastapi import BackgroundTasks, FastAPI
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from starlette.config import Config

config = Config(".env")
print("==============================")
print(config("MAIL_USERNAME"))
print("==============================")
conf = ConnectionConfig(  
    MAIL_FROM=config("MAIL_FROM"),
    MAIL_SERVER=config("MAIL_SERVER"),
    MAIL_PORT=config("MAIL_PORT"),
    MAIL_USERNAME=config("MAIL_USERNAME"),
    MAIL_PASSWORD=config("MAIL_PASSWORD"),
    MAIL_SSL_TLS=config("MAIL_SSL_TLS"),
    MAIL_STARTTLS=config("MAIL_STARTTLS"),
    USE_CREDENTIALS=config("USE_CREDENTIALS"),
    VALIDATE_CERTS=config("VALIDATE_CERTS"),
)


async def simple_send(subject: str, recipient: List, message: str):

    message = MessageSchema(
        subject=subject,
        recipients=recipient,
        body=message,
        subtype="html",
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    