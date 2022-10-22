import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title="PO Tracker", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="po_priority.xlsx",
        engine="openpyxl",
        sheet_name="sku",
        skiprows=0,
        usecols="A:AU",
        nrows=806,
    )
    # Add 'hour' column to dataframe
    #df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()

title_section = st.container()
pie_chart = st.container()
mcat_view = st.container()
turn_view = st.container()
collection_view = st.container()
search = st.container()
search_tab = st.container()
search_results = st.container()

# Title Section

with title_section:
    st.title("PO Dashboard")
# --- HIGH LEVEL OVERVIEW ---

# Season Distribution Pie Chart

labels = df.['MCAT'].unique()
sizes = df.

pie = df.groupby(['MCAT']).sum().plot(kind='pie', y='po_qty', autopct='%1.0f%%')
with pie_chart:
    st.plotly_chart(pie)
# MCAT View

# Turn View

# Collection View

# --- SEARCH ---

# Search Tab

# Display Results



















# GRAVEYARD - TO REFFERENCE IF NEEDED

# # ---- SIDEBAR ----
# st.sidebar.header("Please Filter Here:")
# mcat = st.sidebar.multiselect(
#     "Select MCAT:",
#     options=df["MCAT"].unique(),
#     default=None,
# )

# purchase_order = st.sidebar.multiselect(
#     "Select PO#:",
#     options=df["po"].unique().round(),
#     default=None,
# )


# vendor_name = st.sidebar.multiselect(
#     "Select Vendor:",
#     options=df["Vendor"].unique(),
#     default=None,
# )

# *** MAIN *** 

# ---PO Views---s


# PO Status by MCAT

# mcat_po_status_delivered = df.groupby("MCAT")["qty_delivered"].sum()
# mcat_po_status_total = (mcat_po_status_delivered / df.groupby("MCAT")["po_qty"].sum())


# left_column, right_column = st.columns(2)
# with left_column:
#     st.subheader("PO Percentage Delivered by MCAT")
#     st.write(df["MCAT"].unique())
# with right_column:
#     st.write(df["MCAT"].unique())
#     st.write(selection_po_total)


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