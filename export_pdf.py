from reportlab.pdfgen import canvas

def create_pdf(results, leave_results, total):

    file="arrear_statement.pdf"

    c=canvas.Canvas(file)

    y=800

    c.drawString(200,820,"Salary Arrear Statement")

    y-=40

    # salary rows
    for r in results:

        text=f"{r['month']}   Basic:{r['basic']}   Arrear:{r['arrear']}   Revised:{r['revised_basic']}"
        c.drawString(50,y,text)

        y-=20

        if y<50:
            c.showPage()
            y=800


    y-=20

    c.drawString(50,y,"Leave Surrender Arrear")

    y-=20

    # leave rows
    for r in leave_results:

        text=f"{r['year']}   Leave Amount:{r['amount']}   Arrear:{r['arrear']}"
        c.drawString(50,y,text)

        y-=20


    y-=40

    c.drawString(200,y,f"Total Arrear : {total}")

    c.save()

    return file