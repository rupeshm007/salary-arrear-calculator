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

            # Store all form data for display
            form_data[key] = value

            # Leave surrender fields
            if key.startswith("leave_"):
                # Only add if value is not empty
                if value and value.strip():
                    try:
                        leave_data[key] = float(value)
                    except ValueError:
                        # Skip invalid values
                        pass

            # Monthly salary fields (excluding employee details)
            elif key not in ["emp_name", "designation", "emp_id"]:
                # Only add if value is not empty
                if value and value.strip():
                    try:
                        data[key] = float(value)
                    except ValueError:
                        # Skip invalid values
                        pass

        # Only calculate if there's data
        if data or leave_data:
            results, leave_results, total = calculate_arrear(data, leave_data)
        else:
            results, leave_results, total = [], [], 0

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

    return send_file(file, as_attachment=True, download_name="arrear_statement.xlsx")


@app.route("/pdf")
def pdf():

    file = create_pdf(results, leave_results, total)

    return send_file(file, as_attachment=True, download_name="arrear_statement.pdf")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)