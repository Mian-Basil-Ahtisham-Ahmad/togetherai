import PyPDF2
from extra.together import Together

# Initialize the Together client
client = Together(api_key="")

# Function to extract text from a PDF
def extract_pdf_text(pdf_path):
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# Extract text from the given PDF
pdf_text = extract_pdf_text("./sample.pdf")

# Function to ask a question based on the PDF content
def ask_question(question):
    response = client.chat.completions.create(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        messages=[{"role": "user", "content": f"PDF content: {pdf_text}\nQuestion: {question}"}]
    )
    return response.choices[0].message.content

# Example question
question = "What is OOP ?"

# Get the response
answer = ask_question(question)

# Print the answer
print(answer)
