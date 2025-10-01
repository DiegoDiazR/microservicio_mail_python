from fastapi import FastAPI
from models import EmailRequest
from email_sender import send_email

app = FastAPI(title="Microservicio de Correo en Python")

@app.post("/send-email")
async def send_email_endpoint(request: EmailRequest):
    success = await send_email(request.to_email, request.subject, request.body)
    return {"message": "Correo enviado" if success else "Fallo al enviar correo"}
