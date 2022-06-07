import streamlit as st
import snowflake.connector
import pandas as pd
import numpy as np
import altair as alt

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return snowflake.connector.connect(**st.secrets["snowflake"])

conn = init_connection()

@st.experimental_memo(ttl=600)
def run_query_pandas(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetch_pandas_all()

# Main
conn = init_connection()

df = run_query_pandas("select top 50 * from snowflake.account_usage.tables;")
st.write(df)