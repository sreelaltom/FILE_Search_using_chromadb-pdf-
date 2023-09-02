import streamlit as st
import pdfplumber
import chromadb
import re                                                                              #importing modules

def main():

    st.title("Chroma Pdf Search")
    pdf_file = st.file_uploader("Upload the file here", accept_multiple_files=False)     #creating a ui for user to uplode the file 
    paragraphs = []                                                                      #using streamlit
    if pdf_file is not None:
    
        pdf = pdfplumber.open(pdf_file)
        text = ""                                                                        #convert the pdf to a text

    
        for page in pdf.pages:
            text += page.extract_text()

    
        pdf.close()
                                                                                        #spliting it to paragraphs
        paragraphs = []
        current_paragraph = ""
        for line in text.splitlines():
            if line.strip().endswith("."):
            
                current_paragraph += line + "\n"
                paragraphs.append(current_paragraph)
                current_paragraph = ""
            elif line.strip().endswith(":"):
    
                current_paragraph = line + "\n"
            else:
            
                current_paragraph += line + "\n"
        documents=[]
        Ids=[]

        for index,item in enumerate(paragraphs,start=1):
            documents.append(item)                                                 #creating a list of ids
            Ids.append('id{}'.format(index))
                
        Collection_name = re.sub(r'[^a-zA-Z0-9_-]', '_', pdf_file.name[:-4])                 #add it to chromadb
        chroma_client = chromadb.Client()
        collection = chroma_client.create_collection(name=Collection_name)
        

        collection.add(documents=documents, ids=Ids)
        input_text = st.text_input("Enter the data you want to learn from the uploaded PDF")
        results = collection.query(query_texts=[input_text], n_results=5)
        st.subheader("Query Results:")                                             #query through the created collections
        for result in results["documents"][0]:
            st.write(f"Matching Text: {result}")                                            
        
                
    
if __name__ == "__main__":
    main()