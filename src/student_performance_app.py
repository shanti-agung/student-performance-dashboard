import streamlit as st
import os
import pandas as pd
import seaborn as sns


st.title("Student Performance Demo")

student_df = pd.read_csv("../data/student-mat.csv", delimiter=";")

st.sidebar.info("Enter your preferences below")
unique_fam_size = sorted(student_df["famsize"].unique())
selected_family_size = st.sidebar.radio("Pick family size", unique_fam_size,
                                        captions=["Greater than 3", "Less than 3"])

df = student_df.query("famsize in @selected_family_size")

sns.set_style("ticks")
g=sns.catplot(data=df, kind="box", x="sex", y="G3", col="guardian", col_wrap= 2, hue="sex", palette=sns.color_palette("Set2",2))
g.set_axis_labels("Student gender", "Final grade").set_titles("Guardian : {col_name}", weight="bold")
st.pyplot(g)

st.write("Data source: Cortez,Paulo. (2014). Student Performance. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T.")