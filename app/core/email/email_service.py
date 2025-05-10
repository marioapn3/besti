import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.core.config import settings  
from loguru import logger
from datetime import datetime
from app.core.config import settings



def send_email(data: dict, subject: str, template_path: str, replacements: dict):
    sender_email = settings.SMTP_SENDER_EMAIL

    # Setup MIME
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = data["email"]
    message["Subject"] = subject

    try:
        with open(template_path, "r") as template_file:
            html_body = template_file.read()
            # Replace placeholders in the template
            for placeholder, value in replacements.items():
                html_body = html_body.replace(placeholder, str(value))

        message.attach(MIMEText(html_body, "html"))

        # Mailtrap SMTP server
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)  # Mailtrap credentials
            server.sendmail(sender_email, data["email"], message.as_string())
        
        # Gmail SMTP server
        # with smtplib.SMTP(settings.SMTP_GMAIL_HOST, settings.SMTP_GMAIL_PORT) as server:
        #     server.starttls()
        #     server.login(settings.SMTP_GMAIL_USER, settings.SMTP_GMAIL_PASSWORD)  # Mailtrap credentials
        #     server.sendmail(sender_email, data["email"], message.as_string())

        logger.info(f"Email sent successfully to {data['email']} at {datetime.now()}")
    except Exception as e:
        logger.exception(f"Failed to send email to {data['email']}: {str(e)}")

def send_otp_email(data: dict, otp: str):
    subject = "Your OTP Code"
    replacements = {
        "{{name}}": data.get("name", "User"),
        "{{otp}}": otp
    }
    send_email(data, subject, "app/core/template/otp_email.html", replacements)

def send_forgot_password(data: dict, link: str):
    subject = "Forgot Password"
    replacements = {
        "{{name}}": data["name"],
        "{{link}}": link
    }
    send_email(data, subject, "app/core/template/reset_password_email.html", replacements)

def send_create_organisation_email(data: dict):
    subject = "Welcome to BESTI (Bot STI)"
    replacements = {
        "{{name}}": data["name"],
        "{{organisation_name}}": data["organisation_name"]
    }
    send_email(data, subject, "app/core/template/create_organisation.html", replacements)

def send_invitation_member(data: dict):
    subject = "Invitation Member on BESTI (Bot STI)"
    replacements = {
        "{{email}}": data["email"],
        "{{name}}": data["name"],
        "{{organisation_name}}": data["organisation_name"],
        "{{password}}": data["password"],
        "{{login_link}}": data["login_link"]
    }
    send_email(data, subject, "app/core/template/invitation_member.html", replacements)
