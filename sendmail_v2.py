import asyncio
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import aiosmtplib #pip install aiosmtplib

async def send_email(sender_email, password, receive_email, subject, body, smtp_server="smtp.gmail.com", smtp_port=587):
    # Criando o e-mail 
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receive_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    try:
        # Conectando ao servidor SMTP de forma assíncrona
        await aiosmtplib.send(
            message,
            hostname=smtp_server,
            port=smtp_port,
            start_tls=True,
            username=sender_email,
            password=password
        )
        print("Email enviado com sucesso")
    except Exception as e:
        print(f'Houve algum erro: {e}')

if __name__ == "__main__":
    sender_email = "seuemailaquiia@gmail.com"
    password ="insira a senha aqui"
    receive_email = "emaildestinoaqui1@gmail.com" 
    subject = "E-mail automático em python"
    body = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email Teste</title>
    </head>
    <body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f2f2f2;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="background-color: #f2f2f2;">
            <tr>
                <td align="center">
                    <table border="0" cellpadding="0" cellspacing="0" width="600" style="background-color: #ffffff;">
                        <tr>
                            <td align="center" style="padding: 40px 0;">
                                <img src="https://img.freepik.com/fotos-gratis/paisagem-de-nevoeiro-matinal-e-montanhas-com-baloes-de-ar-quente-ao-nascer-do-sol_335224-794.jpg" alt="Paisagem" width="400" style="display: block; margin: 0 auto;">
                                <p style="margin-top: 20px; text-align: center;">Olá,</p>
                                <p style="text-align: center;">Este é um e-mail de teste com uma imagem anexada.</p>
                                <p style="text-align: center;">Agradecemos por ter recebido este e-mail de teste.</p>
                                <p style="text-align: center;">Este e-mail foi enviado apenas para fins de demonstração e teste.</p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """

    asyncio.run(send_email(sender_email, password, receive_email, subject, body))
