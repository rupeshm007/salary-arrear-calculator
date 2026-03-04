from flask import Flask, render_template, request, send_file
from arrear_calculator import calculate_arrear
from export_excel import create_excel
from export_pdf import create_pdf

app = Flask(__name__)

results = []
leave_results = []
total = 0


@app.route("/", methods=["GET", "POST"])
def index():

    global results, leave_results, total

    form_data = {}

    if request.method == "POST":

        data = {}
        leave_data = {}

        for key, value in request.form.items():

            if value:

                form_data[key] = value

                # Leave surrender fields
                if key.startswith("leave_"):
                    leave_data[key] = float(value)

                # Monthly salary fields
                else:
                    data[key] = float(value)

        results, leave_results, total = calculate_arrear(data, leave_data)

    return render_template(
        "index.html",
        results=results,
        leave_results=leave_results,
        total_arrear=total,
        form_data=form_data
    )


@app.route("/excel")
def excel():

    file = create_excel(results, leave_results, total)

    return send_file(file, as_attachment=True)


@app.route("/pdf")
def pdf():

    file = create_pdf(results, leave_results, total)

    return send_file(file, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)