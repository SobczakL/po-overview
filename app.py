import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import time

st.set_page_config(page_title="PO Tracker", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="po_priority.xlsx",
        engine="openpyxl",
        sheet_name="sku",
        skiprows=0,
        usecols="A:AR",
        nrows=2000,
    )
    # Add 'hour' column to dataframe
    #df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()


# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
mcat = st.sidebar.multiselect(
    "Select MCAT:",
    options=df["MCAT"].unique(),
    default=None,
)

purchase_order = st.sidebar.multiselect(
    "Select PO#:",
    options=df["po"].unique().round(),
    default=None,
)


vendor_name = st.sidebar.multiselect(
    "Select Vendor:",
    options=df["Vendor"].unique(),
    default=None,
)

df_selection = df.query(
    "MCAT == @mcat & po ==@purchase_order & Vendor ==@vendor_name"
)
# *** MAIN *** 

# ---PO Views---

#Based off query selection, fetch and update chart to display the total number of ordered units delivered
selection_po_qty_total = int(df_selection["po_qty"].sum())
selection_po_delivered_total = int(df_selection["qty_delivered"].sum())
selection_po_total = float(selection_po_delivered_total/ selection_po_qty_total)*100


# PO Status by MCAT

mcat_po_status_delivered = df.groupby("MCAT")["qty_delivered"].sum()
mcat_po_status_total = (mcat_po_status_delivered / df.groupby("MCAT")["po_qty"].sum().round())*100

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("PO Percentage Delivered by MCAT")
    st.write(selection_po_total)

# Calendar


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)