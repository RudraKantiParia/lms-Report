import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="LMS Timestamp Remover")

st.title("LMS Report – Remove Timestamp Columns")

uploaded_file = st.file_uploader(
    "Upload LMS Excel file",
    type=["xlsx"]
)

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    keep_columns = []
    for i, col in enumerate(df.columns):
        if i < 2:
            keep_columns.append(col)
        elif (i - 2) % 2 == 0:
            keep_columns.append(col)

    clean_df = df[keep_columns]

    st.success("Timestamps removed successfully")

    st.download_button(
    label="Download cleaned Excel file",
    data=buffer,
    file_name="lms_report_without_timestamps.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

