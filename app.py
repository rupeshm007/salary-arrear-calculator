from flask import Flask,render_template,request,send_file
from arrear_calculator import calculate_arrear
from export_excel import create_excel
from export_pdf import create_pdf

app=Flask(__name__)

results=[]
total=0


@app.route("/",methods=["GET","POST"])
def index():

    global results,total

    if request.method=="POST":

        data={}

        for key,value in request.form.items():

            if value:
                data[key]=float(value)

        results,total=calculate_arrear(data)

    return render_template(
        "index.html",
        results=results,
        total_arrear=total
    )


@app.route("/excel")
def excel():

    file=create_excel(results)

    return send_file(file,as_attachment=True)


@app.route("/pdf")
def pdf():

    file=create_pdf(results,total)

    return send_file(file,as_attachment=True)


# if __name__=="__main__":
#     app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)