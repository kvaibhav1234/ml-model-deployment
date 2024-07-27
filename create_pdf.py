
"""
Step 4: Create PDF Document
"""
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to create the PDF
def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 40, "Model Deployment Documentation")

    # Personal Details
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 80, "Name: Kashish Vaibhav")
    c.drawString(100, height - 100, "Batch code: LISUM35")
    c.drawString(100, height - 120, "Submission date: July 27, 2024")
    c.drawString(100, height - 140, "Submitted to: Data Glacier - Week 4: Deployment on Flask")

    # Step 1: Select Any Toy Data
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, height - 180, "Step 1: Select Any Toy Data")

    c.setFont("Helvetica", 12)
    c.drawString(100, height - 200, "Using a simple manually created dataset.")
    c.drawString(100, height - 220, "Data:")
    c.drawString(100, height - 240, str([
        [1, 1, 1], 
        [2, 1, 1], 
        [3, 2, 0], 
        [4, 2, 0], 
        [5, 3, 1], 
        [6, 3, 1]
    ]))

    # Step 2: Save the Model
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, height - 280, "Step 2: Save the Model")

    c.setFont("Helvetica", 12)
    c.drawString(100, height - 300, "Training a Logistic Regression model on the simple dataset and saving it as simple_model.pkl.")

    # Step 3: Deploy the Model on Flask
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, height - 340, "Step 3: Deploy the Model on Flask")

    c.setFont("Helvetica", 12)
    c.drawString(100, height - 360, "Creating a Flask web application to serve the model.")

    c.save()

# Create the PDF document
create_pdf("model_deployment_documentation.pdf")
