from flask import Flask, render_template, request, send_file
from io import BytesIO
import pdfkit

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/generate_quote', methods=['POST'])
def generate_quote():
    # Get client details
    client_name = request.form['client_name']
    phone = request.form['phone']
    address = request.form['address']

    # Get work details dynamically
    work_descriptions = request.form.getlist('work_description[]')
    quantities = request.form.getlist('quantity[]')
    unit_prices = request.form.getlist('unit_price[]')

    total_price = 0
    works = []
    
    for i in range(len(work_descriptions)):
        work = {
            'description': work_descriptions[i],
            'quantity': int(quantities[i]),
            'unit_price': float(unit_prices[i]),
            'price': int(quantities[i]) * float(unit_prices[i])
        }
        works.append(work)
        total_price += work['price']

    # Pass data to the template
    rendered = render_template('quote_template.html', client_name=client_name, phone=phone, address=address, 
                               works=works, total_price=total_price, carpenter_name="John Doe", 
                               carpenter_phone="123-456-7890", carpenter_address="Carpenter's Address", 
                               terms="Payment due upon completion.")

    # Generate PDF from rendered HTML
    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Update this path accordingly
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    pdf = pdfkit.from_string(rendered, False, configuration=config)

    # Download the PDF
    response = BytesIO(pdf)
    return send_file(response, as_attachment=True, download_name="quotation.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)
