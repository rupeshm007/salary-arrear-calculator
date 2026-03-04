from reportlab.pdfgen import canvas

def create_pdf(results,total):

    file="arrear_statement.pdf"

    c=canvas.Canvas(file)

    y=800

    c.drawString(200,820,"Salary Arrear Statement")

    for r in results:

        text=f"{r['month']}  Basic:{r['basic']}  Arrear:{r['arrear']}"
        c.drawString(50,y,text)

        y-=20

    c.drawString(200,y-20,f"Total Arrear : {total}")

    c.save()

    return file