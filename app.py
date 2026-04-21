# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# -------------------------------
# Streamlit page configuration
# -------------------------------
st.set_page_config(page_title="House Price Dashboard", layout="wide")

# -------------------------------
# Title
# -------------------------------
st.title("🏡 Interactive House Price Dashboard")

# -------------------------------
# Load CSV file
# -------------------------------
df = pd.read_csv("house_prices.csv")
st.subheader("Dataset Preview")
st.dataframe(df.head())

# -------------------------------
# Numeric Columns
# -------------------------------
numeric_df = df.select_dtypes(include=['int64', 'float64'])

# -------------------------------
# Correlation Heatmap (Seaborn)
# -------------------------------
import plotly.figure_factory as ff

# Select numeric columns for correlation
numeric_cols = ["price", "area", "bedrooms", "bathrooms", "stories", "parking"]
corr_matrix = df[numeric_cols].corr().values

# Create heatmap
fig = ff.create_annotated_heatmap(
    z=corr_matrix,
    x=numeric_cols,
    y=numeric_cols,
    annotation_text=corr_matrix.round(2),  # show correlation values
    colorscale='Viridis',
    showscale=True,
    hoverinfo="z"
)

# Update layout to fully fit the screen
fig.update_layout(
    title="Correlation Heatmap of Numeric Features",
    autosize=True,
    width=None,   # None allows Streamlit to control width
    height=600,
    margin=dict(l=20, r=20, t=50, b=20)
)

# Display in Streamlit with full container width
st.plotly_chart(fig, use_container_width=True)



# -------------------------------
# Interactive Bar Plot (Plotly)
# -------------------------------
# Auto-detect bedroom column

# ----- Bedrooms Bar Chart -----
if "BedroomAbvGr" in df.columns:
    bedroom_count = df["BedroomAbvGr"].value_counts().sort_index()
    fig = px.bar(
        x=bedroom_count.index,
        y=bedroom_count.values,
        title="Bedroom Count",
        labels={"x": "Bedrooms", "y": "Number of Houses"}
    )
    st.plotly_chart(fig)
else:
    st.error("Column 'BedroomAbvGr' not found!")




# -------------------------------
# Interactive Pie Chart (Plotly)
# -------------------------------
import plotly.express as px

# Count number of houses per bedroom
bedroom_count = df["bedrooms"].value_counts().reset_index()
bedroom_count.columns = ["Bedrooms", "Count"]

# Create pie chart with fixed size
fig = px.pie(
    bedroom_count,
    names="Bedrooms",
    values="Count",
    title="Distribution of Bedrooms",
    width=900,   # width of the chart
    height=600   # height of the chart
)

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)



# -------------------------------
# Treemap: Distribution by Area (Plotly)
# -------------------------------
if 'area' in df.columns:
    st.subheader("Treemap: Distribution by Area")
    area_count = df['area'].value_counts().reset_index()
    area_count.columns = ['Area', 'Count']
    fig = px.treemap(area_count, path=['Area'], values='Count', 
                     color='Count', color_continuous_scale='Viridis',
                     title="Area Distribution Treemap")
    st.plotly_chart(fig)


# -------------------------------
# Interactive Scatter Plot (Plotly)
# -------------------------------
if 'area' in df.columns and 'price' in df.columns:
    st.subheader("Scatter Plot: Area vs Price")
    fig = px.scatter(df, x='area', y='price', color='bedroom' if 'bedroom' in df.columns else None,
                     size='price', hover_data=df.columns,
                     title="Area vs Price by Bedrooms")
    st.plotly_chart(fig)

# -------------------------------
# Box Plot (Plotly)
# -------------------------------
import plotly.express as px

# Create box plot for price by number of bathrooms
fig = px.box(
    df,
    x="bathrooms",
    y="price",
    title="Box Plot: Price by Number of Bathrooms",
    labels={"bathrooms": "Number of Bathrooms", "price": "House Price"},
    width=600,   # width of the chart
    height=400   # height of the chart
)

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


import plotly.express as px

# Select first 10 rows (10 houses)
top10 = df.head(10)  # first 10 houses

# Create bar chart
fig = px.bar(
    top10,
    x=top10.index + 1,        # House number (1 to 10)
    y="bedrooms",             # Number of bedrooms
    title="Number of Bedrooms for 10 Houses",
    labels={"x": "House Number", "bedrooms": "Number of Bedrooms"},
    color_discrete_sequence=["skyblue"],  # all bars sky blue
    width=200,
    height=600
)

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

import plotly.express as px

# Select first 10 rows (10 houses)
top10 = df.head(10)  # first 10 houses

# Create bubble chart
fig = px.scatter(
    top10,
    x=top10.index + 1,        # House number (1 to 10)
    y="price",                # House price
    size="bedrooms",          # Bubble size = number of bedrooms
    color_discrete_sequence=["pink"],  # Baby pink bubbles
    title="Bubble Chart: Price vs House Number (Bubble Size = Bedrooms)",
    labels={"x": "House Number", "price": "House Price", "bedrooms": "Number of Bedrooms"},
    width=800,
    height=600
)

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)


import plotly.express as px
import numpy as np

# Select first 10 houses
top10 = df.head(10)

# X-axis: house numbers 1–10
x = list(range(1, len(top10) + 1))

# Y-axis: create “wave” effect by slightly modifying actual prices
# This adds small fluctuations to make it visibly up and down
y = top10["price"].values + np.random.randint(-5000, 5000, size=len(top10))

# Create line chart
fig = px.line(
    x=x,
    y=y,
    title="Wave-Like Line Chart (Mountain Peaks)",
    labels={"x": "House Number", "y": "Wave Price"},
    markers=True,
    width=700,
    height=400
)

# Customize line and markers
fig.update_traces(
    line=dict(color='green', width=3),
    marker=dict(color='yellow', size=12)
)

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

import plotly.express as px
import numpy as np

# Simulate heart-wave data
# x-axis: 100 time points
x = np.arange(0, 100, 1)

# y-axis: combine sine wave + spikes to mimic heartbeat
y = np.sin(x / 3) * 5       # base wave
y[::10] += 10               # spikes every 10 points like heartbeats
y[::25] += 15               # bigger spikes occasionally

# Create line chart
fig = px.line(
    x=x,
    y=y,
    title="Heart-Wave / ECG Style Chart",
    labels={"x": "Time", "y": "Amplitude"},
    markers=True,
    width=800,
    height=400
)

# Customize line and markers
fig.update_traces(
    line=dict(color='blue ', width=3),
    marker=dict(color='pink', size=6)
)

# Show chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

import plotly.express as px

fig = px.violin(
    df,
    y="price",
    x="bedrooms",
    color="bedrooms",
    color_discrete_sequence=["violet", "green", "violet", "green", "violet", "green"],  # alternating colors
    box=True,        # show box inside violin
    points="all",    # show all data points
    title="Violin Plot: Price by Number of Bedrooms",
    width=700,
    height=400
)

st.plotly_chart(fig, use_container_width=True)


import plotly.express as px

fig = px.sunburst(
    df,
    path=["mainroad", "bedrooms", "furnishingstatus"],
    values="price",
    title="Sunburst: Price Hierarchy by Road Access, Bedrooms, and Furnishing",
    color="price",  # optional, to color by price
    color_continuous_scale=["yellow", "light green"],  # yellow to orange
    width=700,
    height=500
)

st.plotly_chart(fig, use_container_width=True)
