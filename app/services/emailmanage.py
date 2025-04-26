from app.common.utils import logging_response

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

from app.common.config import sender, smtp_server, smtp_port, login_id, login_pw, survey_form_url

from app.api.response import SuccessResponse
from app.api import exceptions as ex

layer = "BUSINESS"

def send_email_(file_path, receiver, session, correlation_id):
    """
    `Email API`
    :return:
    """
    try:
        # logging_request

        subject = "[Using-AI-tools] 요청하신 논문 번역본 송부드립니다."
        receiver_name = receiver.split("@")[0]
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.05);">
            <h2 style="color: #333;">안녕하세요, <span style="color: #007bff;">{receiver_name}</span> 님.</h2>

            <p style="font-size: 16px; color: #555;">
                <b>Using-AI-Tools 논문 번역 서비스</b>를 이용해주셔서 진심으로 감사드립니다.
            </p>

            <p style="font-size: 16px; color: #555;">
                저희 서비스에 대한 간단한 설문에 참여해주시면,  
                <span style="color: #e74c3c;"><b>번역된 논문 3편</b></span>을 추가로 보내드리고 있습니다. <br />
                아래 링크를 통해 설문에 응답해주시면 감사하겠습니다.
            </p>

            <div style="text-align: center; margin: 30px 0;">
                <a href="{survey_form_url}" style="background-color: #007bff; color: white; padding: 14px 24px; text-decoration: none; border-radius: 6px; font-size: 16px;">
                🔗 설문 참여하기
                </a>
            </div>

            <p style="font-size: 15px; color: #999; margin-top: 40px;">
                감사합니다.<br/>
                <b>Using-AI-Tools 드림</b>
            </p>
            </div>
        </body>
        </html>
        """
        msg = MIMEMultipart("related")
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        msg_alternative = MIMEMultipart("alternative")
        msg.attach(msg_alternative)
        msg_alternative.attach(MIMEText(body, "html"))

        with open(f"{file_path}", "rb") as f:
            pdf_attachment = MIMEApplication(f.read(), _subtype="pdf")
            pdf_attachment.add_header("Content-Disposition", "attachment", filename="paper.pdf")
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
    

async def send_email2_(id, pw, email, session, correlation_id):
    """
    `Email API`
    :return:
    """
    try:
        # logging_request

        subject = "[Using-AI-tools] 고유 IW와 PW 발급"
        receiver_name = email.split("@")[0]
        body = f"""
        <html>
        <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
            <div style="max-width: 600px; margin: auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.05);">
            <h2 style="color: #333;">안녕하세요, <span style="color: #007bff;">{receiver_name}</span> 님.</h2>

            <p style="font-size: 16px; color: #555;">
                <b>Using-AI-Tools 논문 번역 서비스</b>를 이용해주셔서 진심으로 감사드립니다.
            </p>

            <p style="font-size: 16px; color: #555;">
                요청하신 고유 ID와 PW 발급해드렸습니다.<br />
                아래의 정보를 활용해주시면 감사드리겠습니다.
            </p>

            <p style="font-size: 16px; color: #555;">
                <strong>ID :</strong> {id}<br />
                <strong>PW :</strong> {pw}
            </p>

            <p style="font-size: 15px; color: #999; margin-top: 40px;">
                감사합니다.<br/>
                <b>Using-AI-Tools 드림</b>
            </p>
            </div>
        </body>
        </html>
        """
        
        msg = MIMEMultipart("related")
        msg["From"] = sender
        msg["To"] = email
        msg["Subject"] = subject

        msg_alternative = MIMEMultipart("alternative")
        msg.attach(msg_alternative)
        msg_alternative.attach(MIMEText(body, "html"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(login_id, login_pw)
            server.send_message(msg)

        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)