# Chroma Pdf Search

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Chroma Pdf Search is a Python application built with Streamlit that allows users to upload PDF files, extract text from them, and search for specific data within the PDFs. It utilizes the `pdfplumber` library for PDF text extraction and the `chromadb` library for creating a searchable database of extracted text.


## Author

- [Naveen Manoj](https://github.com/neevan0842?tab=repositories)
- [Sreelal S S](https://github.com/sreelaltom?tab=repositories)

## streamlit output look
![Screenshot 2023-09-02 211721](https://github.com/sreelaltom/titianic_prediction/assets/121371200/8ae3445f-3450-433e-9137-d4c662594dd2)

## Demo video
![video](https://github.com/sreelaltom/titianic_prediction/assets/121371200/4ecb9608-f3ea-4feb-93d3-d0b7def3ded3)

## Features

- **Upload PDF Files**: Easily upload PDF files for text extraction.
- **Text Extraction**: Extract text from the uploaded PDFs.
- **Paragraph Splitting**: Split extracted text into paragraphs for easier analysis.
- **Text Search**: Store extracted text in a searchable database using ChromaDB and perform text queries to find specific data within the PDFs.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sreelaltom/Thinkerhub-sat
   ```
2. **Install Dependencies:**

```
pip install streamlit pdfplumber chromadb
```

3. **Run the Application:**

```
streamlit run "chroma_pdf_search.py"

```

## Usage

1. **Open the Application**: Run the application using the `streamlit run` command.

2. **Upload a PDF File**: Use the provided interface to upload a PDF file.

3. **Text Extraction**: The application will extract text from the PDF and split it into paragraphs.

4. **Search Queries**: Enter text queries to search for specific data within the PDF.

5. **View Results**: The application will display matching text found in the PDF.

## Dependencies

- [Streamlit](https://www.streamlit.io/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [ChromaDB](https://docs.trychroma.com/api-reference)

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.


