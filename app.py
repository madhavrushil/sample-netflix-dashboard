import pandas as pd
import streamlit as st
import plotly.express as px

# Page title
st.title("Netflix Data Analysis Dashboard")

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Dataset preview
st.subheader("Dataset Preview")
st.write(df.head())

# Movies vs TV Shows
type_count = df['type'].value_counts()

fig = px.pie(
    values=type_count.values,
    names=type_count.index,
    title="Movies vs TV Shows"
)

st.plotly_chart(fig)
# Top 10 countries
country_count = df['country'].value_counts().head(10)

fig2 = px.bar(
    x=country_count.index,
    y=country_count.values,
    title="Top 10 Countries with Netflix Content"
)

st.plotly_chart(fig2)
year_data = df['release_year'].value_counts().sort_index()

fig3 = px.line(
    x=year_data.index,
    y=year_data.values,
    title="Content Released Over Years"
)

st.plotly_chart(fig3)
st.sidebar.header("Filters")

selected_type = st.sidebar.selectbox(
    "Choose Type",
    df['type'].unique()
)

filtered_df = df[df['type'] == selected_type]

st.write(filtered_df.head())
st.metric("Total Titles", len(df))


selected_type = st.sidebar.selectbox(
    "Select Type",
    df['type'].unique()
)

filtered_df = df[df['type'] == selected_type]

st.write(filtered_df.head())