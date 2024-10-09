# Ramchandra Carpentry Work - Quotation Web Application

This is a Flask-based web application for generating PDF quotations for carpentry services. Users can add work descriptions, quantities, unit prices, and client details. The system calculates the total price and generates a PDF document with the business's basic details, work details, and terms and conditions. The PDF can be downloaded and shared with clients.

## Features
- Dynamic form to add multiple work details.
- Automatic total price calculation.
- Client details and work information.
- Attractive, customizable PDF template.
- Static information about the business (name, contact, services).
- Option to download the PDF after submission.

## Project Structure

📦your-project ┣ 📂static ┃ ┣ 📂css ┃ ┃ ┗ 📜styles.css ┣ 📂templates ┃ ┣ 📜index.html ┃ ┗ 📜quote_template.html ┣ 📜app.py ┣ 📜README.md ┗ 📜requirements.txt

markdown
Copy code

## Prerequisites

- Python 3.x
- pip (Python package manager)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/quotation-template.git
   cd ramchandra-carpentry-quotation
Create and Activate Virtual Environment: It's a good practice to use a virtual environment to manage dependencies. Run the following commands:

bash
Copy code
python -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows
Install Dependencies: Install the required dependencies listed in the requirements.txt file:

bash
Copy code
pip install -r requirements.txt
Install wkhtmltopdf: The application uses pdfkit for generating PDFs, which requires wkhtmltopdf.

On macOS, install via Homebrew:

bash
Copy code
brew install --cask wkhtmltopdf
On Ubuntu/Debian:

bash
Copy code
sudo apt-get install -y wkhtmltopdf
On Windows:

Download wkhtmltopdf from here.
Install the executable and add the wkhtmltopdf binary to your system's PATH environment variable.
Set the Path for wkhtmltopdf (if necessary): If wkhtmltopdf is not in your PATH, you need to set it manually in the app.py file:

python
Copy code
import pdfkit
path_to_wkhtmltopdf = r'path\to\wkhtmltopdf.exe'  # Windows example
pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
Run the Application: After completing the setup, you can run the application locally with:

bash
Copy code
flask run
Access the Application: Open a browser and go to http://127.0.0.1:5000/ to use the application.

Usage
Fill out the client details form.
Add work descriptions, quantities, and unit prices.
Click "Add Work Details" to include more work items.
The total price will be calculated automatically.
Once all details are entered, submit the form to generate and download the PDF.
Customizing the Template
To change the static details like business name, address, phone, and email, modify the quote_template.html located in the templates folder.

Dependencies
Flask: Web framework for Python.
pdfkit: Python wrapper for wkhtmltopdf to generate PDFs.
wkhtmltopdf: Required for converting HTML to PDF.
License
This project is licensed under the MIT License - see the LICENSE file for details.

markdown
Copy code

### Explanation:

1. **Setup and Installation**: 
   This section covers the prerequisites, cloning the repo, setting up a virtual environment, installing dependencies, and configuring `wkhtmltopdf`.
   
2. **Usage**: 
   Instructions on how to use the web application, including adding work details and generating the PDF.

3. **Customization**: 
   Provides instructions on how to modify the template with static details like business name, phone number, etc.

4. **License**: 
   A placeholder for the license if needed.

Replace `your-username` with your GitHub username in the `git clone` command. This `README.md` file should cover all the steps for setting up and running the application on different systems.





