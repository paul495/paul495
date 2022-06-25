import pandas as pd
import numpy as np
import streamlit as st
import docx2txt
import re
import os
import base64

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


dictMonth={'JAN':'01','FEB':'02','MAR':'03','APR':'04','MAY':'05','JUN':'06','JUL':'07','AUG':'08','SEP':'09','OCT':'10','NOV':'11','DEC':'12'}
dictRep={"IR MONTHLY":"MMIR","IR SB":"SBIR", "QUARTERLY BOARD":"QBR", "NEWS LETTER":"NL","GUIDELINES":"GL","MEDIA LEAD SHEET":"MSLS","SB LEAD SHEET":"SBLS"}

add_select_Report = st.sidebar.selectbox("SELECT REPORT",("IR MONTHLY","IR SB", "QUARTERLY BOARD", "NEWS LETTER","GUIDELINES","MEDIA LEAD SHEET","SB LEAD SHEET"))
add_selectyear = st.sidebar.selectbox(
    "SELECT YEAR",
    ("2019","2020","2021","2022","2023"))
add_selectmonth = st.sidebar.selectbox(
    "SELECT MONTH",
    ("JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"))

path1 = r"/Users/cbnindia/Library/CloudStorage/Box-Box/PRODUCTION/PRODUCTION_CONTENT/CONTENT/FY21-22/KINGSLEY_PAUL/Reports/DOCS/CBN_DOCS"
if add_select_Report== "IR MONTHLY" or "IR SB" or "QUARTERLY BOARD":
    srcstr=dictRep[add_select_Report]+dictMonth[add_selectmonth]+add_selectyear[2:]
    
    st.markdown("<h1 style='text-align: center; color: red;'>CBN DOCUMENTS DATABASE</h1>", unsafe_allow_html=True)
    
    for r, d, f in os.walk(path1):
        for file in f:
            file_path=os.path.join(r, file)
            if srcstr in file_path:
            
                if file_path.endswith(".docx"):
                    st.title(add_select_Report)
                    st.header(add_selectyear)
                    text = docx2txt.process(file_path)
                    st.write(text)
            
                elif file_path.endswith(".pdf"):
                    
                    displayPDF(file_path)
        else:    
            st.write("File not available")
            
       
        
