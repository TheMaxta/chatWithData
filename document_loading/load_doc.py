from langchain.document_loaders import PyPDFLoader


PDF_PATH = "../documents/Rich-Dad-Poor-Dad.pdf"

# create loader
loader = PyPDFLoader(PDF_PATH)

pages = loader.load_and_split()

print(pages[0])