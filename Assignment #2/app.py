
from flask import Flask, render_template, request
import qrcode
from reportlab.pdfgen import canvas
import os

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Retrieve form data
    full_name = request.form['full_name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    
    # Generate QR code
    data = f"Full name: {full_name}\nEmail: {email}\nPhone number: {phone_number}"
    qr = qrcode.make(data)
    
    # Check if file already exists and delete it
    file_path = "qr_code.pdf"
    if os.path.exists(file_path):
        os.remove(file_path)

    # Create PDF document and add QR code image
    c = canvas.Canvas("qr_code.pdf")
    c.drawInlineImage(qr, 0, 0)
    c.showPage()
    c.save()
    
    with open('templates/success.html', 'r') as f:
        html_text = f.read()

    return html_text
