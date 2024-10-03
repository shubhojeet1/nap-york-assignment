import streamlit as st
import pandas as pd


st.set_page_config(page_title="GitHub Projects Dashboard", layout="wide")


@st.cache_data
def load_data():
    return pd.read_csv('github_dataset.csv')

df = load_data()


st.title("GitHub Projects Dashboard")


st.header("Dataset Overview")
st.write(f"Total number of projects: {len(df)}")
st.write(f"Number of languages: {df['language'].nunique()}")


st.header("Top Programming Languages")
top_languages = df['language'].value_counts().head(10)
st.bar_chart(top_languages)


st.header("Most Starred Projects")
top_starred = df.nlargest(10, 'stars_count')[['repositories', 'language', 'stars_count']]
st.table(top_starred)


st.header("Average Stars by Language")
avg_stars = df.groupby('language')['stars_count'].mean().sort_values(ascending=False).head(10)
st.bar_chart(avg_stars)


st.header("Forks vs Stars")
st.scatter_chart(df[['forks_count', 'stars_count']].sample(min(1000, len(df))))


st.header("Project Explorer")
selected_language = st.selectbox("Select a language", df['language'].value_counts().index)
filtered_df = df[df['language'] == selected_language].sort_values('stars_count', ascending=False).head(10)
st.write(f"Top 10 {selected_language} projects by stars:")
st.dataframe(filtered_df[['repositories', 'stars_count', 'forks_count', 'issues_count', 'pull_requests', 'contributors']])