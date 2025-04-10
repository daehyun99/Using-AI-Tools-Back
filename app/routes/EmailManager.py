from fastapi import APIRouter, Depends

from os import getenv

from app.api.response import SuccessResponse
from app.common.utils import logging_response
from app.common.utils import generate_metadata

from app.api import exceptions as ex

from sqlalchemy.orm import Session
from app.database.conn import db

router = APIRouter(prefix="/email")

layer = "PRESENTATION"

@router.post("/send/")
async def email_send_sample(session: Session = Depends(db.get_db)):
    """
    `Email API`
    :return:
    """
    try:
        # import
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.application import MIMEApplication

        # 환경변수
        test_receiver = getenv("EMAIL_RECEIVER")
        sender = getenv("Email_SENDER")
        smtp_server = getenv("SMTP_SERVER")
        smtp_port = getenv("SMTP_PORT")
        login_id = getenv("Email_LOGIN_ID")
        login_pw = getenv("Email_LOGIN_PW")
        
        # 코드
        correlation_id = generate_metadata()
        # logging_request
        subject = "PDF 파일 첨부 메일 전송 테스트"
        receiver_name = test_receiver.split("@")[0]
        body = f"""안녕하세요! {receiver_name} 님.
                PDF 파일 첨부 메일 전송 테스트입니다.
                ✅🟥🗨✨😀

                감사합니다.
                {sender} 드림.
                """
        
        msg = MIMEMultipart()
        msg["From"] = sender
        msg["To"] = test_receiver
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        pdf_path = "tests/example.pdf"  # 여기에 첨부할 PDF 파일 경로 입력
        with open(pdf_path, "rb") as f:
            pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
            pdf_attachment.add_header("Content-Disposition", "attachment", filename="테스트용-첨부파일.pdf")
            msg.attach(pdf_attachment)

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(login_id, login_pw)
            server.send_message(msg)

        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)