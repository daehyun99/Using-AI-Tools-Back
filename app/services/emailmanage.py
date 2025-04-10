from app.common.utils import logging_response

layer = "BUSINESS"

from app.api.response import SuccessResponse
from app.api import exceptions as ex

def send_email_sample_(session, correlation_id):
    """
    `Email API`
    :return:
    """
    try:
        # import
        from os import getenv
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.application import MIMEApplication
        from email.mime.image import MIMEImage

        # 환경변수
        test_receiver = getenv("EMAIL_RECEIVER")
        sender = getenv("Email_SENDER")
        smtp_server = getenv("SMTP_SERVER")
        smtp_port = getenv("SMTP_PORT")
        login_id = getenv("Email_LOGIN_ID")
        login_pw = getenv("Email_LOGIN_PW")
        
        # logging_request

        subject = "PDF 파일 첨부 메일 전송 테스트"
        receiver_name = test_receiver.split("@")[0]
        body = f"""<html>
            <head></head>
            <body>
                <h3 data-ke-size="size23"><b>안녕하세요!</b>&nbsp;{receiver_name}&nbsp;님. <br />PDF&nbsp;파일&nbsp;첨부&nbsp;<span style="background-color: #ee2323;">메일</span>&nbsp;<span style="color: #ee2323;">전송</span>&nbsp;<u>테스트</u>입니다. <br />✅🟥🗨✨😀 <br /><br />감사합니다. <br />{sender}&nbsp;드림.</h3>
                <img src="cid:image1">
            </body>
        </html>
        """
        msg = MIMEMultipart("related")
        msg["From"] = sender
        msg["To"] = test_receiver
        msg["Subject"] = subject

        msg_alternative = MIMEMultipart("alternative")
        msg.attach(msg_alternative)
        msg_alternative.attach(MIMEText(body, "html"))

        with open("tests/gooddog.jpg", "rb") as img:
            mime_img = MIMEImage(img.read())
            mime_img.add_header("Content-ID", "<image1>")
            msg.attach(mime_img)

        with open("tests/example.pdf", "rb") as f:
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