from reportlab.pdfgen import canvas

canvas.Canvas("output.pdf").drawString(100, 750, "Hello, ReportLab!").save()
