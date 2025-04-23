import pandas as pd
import plotly.express as px
import preswald as pw
import matplotlib.pyplot as plt
import numpy as np

from preswald import (
    chat,
    get_df,
    plotly,
    sidebar,
    table,
    text, 
    query,
    connect,
    checkbox
)

sidebar()
# Title
text("# Graduate Predict Dashboard 🎓")   
connect()

try:
    df = get_df('admissions')       
    df.columns = ['ID', 'GRE', 'TOEFL', 'RATING', 'SOP', 'LOR', 'GPA', 'RESEARCH', 'ADMIT']
except ValueError as e:
    print(f"Configuration error: {e}")
except Exception as e:
    print(f"Error retrieving data: {e}")
    
text("## Sample data") 
table(df, title="Data View")


text("## Exploring the data with histograms") 
#checkbox
CGPA_histogram = checkbox(default = True, label="GPA", size=0.1)
LOR_histogram = checkbox(default = True, label="LOR",  size=0.1)
GRE_histogram = checkbox(default = True, label="GRE",  size=0.1)
TOEFL_histogram = checkbox(default = True, label="TOEFL",  size=0.1)
RATING_histogram = checkbox(default = True, label="RATING",  size=0.1)
SOP_histogram = checkbox(default = True, label="SOP",  size=0.1)
RESEARCH_histogram = checkbox(default = True, label="RESEARCH", size=0.1)
ADMIT_histogram = checkbox(default = True, label="ADMIT", size=0.1)

if CGPA_histogram:
    fig_hist_CGPA = px.histogram(
        df["GPA"], x="GPA", title="Distribution of GPA", width=300, height=300
    )
    plotly(fig_hist_CGPA, size = 0.30)

if LOR_histogram:
    fig_hist_LOR = px.histogram(
        df["LOR"], x="LOR", title="Distribution of Letter of Recommendation", width=300, height=300
    )
    plotly(fig_hist_LOR, size = 0.30)

if GRE_histogram:
    fig_hist_GRE = px.histogram(
        df["GRE"], x="GRE", title="Distribution of GRE SCORE", width=300, height=300
    )
    plotly(fig_hist_GRE, size = 0.30)

if TOEFL_histogram:
    fig_hist_TOEFL = px.histogram(
        df["TOEFL"], x="TOEFL", title="Distribution of TOEFL SCORE", width=300, height=300
    )
    plotly(fig_hist_TOEFL, size = 0.30)
    
if RATING_histogram:
    fig_hist_RATING = px.histogram(
        df["RATING"], x="RATING", title="Distribution of University Rating", width=300, height=300
    )
    plotly(fig_hist_RATING, size = 0.30)

if SOP_histogram:
    fig_hist_SOP = px.histogram(
        df["SOP"], x="SOP", title="Distribution of Statement of Purpose", width=300, height=300
    )
    plotly(fig_hist_SOP, size = 0.30)

if RESEARCH_histogram:
    fig_hist_RESEARCH = px.histogram(
        df["RESEARCH"], x="RESEARCH", title="Distribution of Research", width=300, height=300
    )
    plotly(fig_hist_RESEARCH, size = 0.30)

if ADMIT_histogram:
    fig_hist_ADMIT = px.histogram(
        df["ADMIT"], x="ADMIT", title="Distribution of Chance of Admit", width=300, height=300
    )
    plotly(fig_hist_ADMIT, size = 0.30)


text("## Correlation")

# CGPA
x = df["ADMIT"] 
y = df["GPA"]
fig = px.scatter(df, x, y, labels={"x": "ADMIT", "y": "GPA"}, title="Chance of admit VS GPA", width=300, height=300)
plotly(fig, size= 0.3)

# GRE
x = df["ADMIT"] 
y = df["GRE"]
fig = px.scatter(df, x, y, labels={"x": "ADMIT", "y": "GRE"}, title="Chance of admit VS GRE", width=300, height=300)
plotly(fig, size=0.3)

# TOFEL
x = df["ADMIT"] 
y = df["TOEFL"]
fig = px.scatter(df, x, y, labels={"x": "ADMIT", "y": "TOEFL"}, title="Chance of admit VS TOEFL", width=300, height=300)
plotly(fig, size=0.3)

# RATING
x = df["ADMIT"] 
y = df["RATING"]
fig = px.scatter(df, x, y, labels={"x": "ADMIT", "y": "RATING"}, title="Chance of admit VS University rating", width=300, height=300)
plotly(fig, size=0.3)

# SOP
x = df["ADMIT"] 
y = df["SOP"]
fig = px.scatter(df, x, y, labels={"x": "ADMIT", "y": "SOP"}, title="Chance of admit VS Statement of Purpose", width=300, height=300)
plotly(fig, size=0.3)

# LOR
x = df["ADMIT"] 
y = df["LOR"]
fig = px.scatter(df, x, y, labels={"x": "ADMIT", "y": "LOR"}, title="Chance of admit VS Letter of Recommendation", width=300, height=300)
plotly(fig, size=0.3)

# RESEARCH
x = df["ADMIT"] 
y = df["RESEARCH"]
fig = px.scatter(df, x, y, labels={"x": "ADMIT", "y": "RESEARCH"}, title="Chance of admit VS Research", width=300, height=300)
plotly(fig, size=0.3)


# Add an interactive chat interface
text(
    "## Ask a question\nUse this chat interface to ask questions about the admission predict dataset analysis. You can inquire about specific patterns, request explanations of the visualizations, or ask for additional insights."
)
chat(source="admissions")



