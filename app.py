# # Advanced Uber Analytics Dashboard (8+ Years Experience Style)

# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go
# from sklearn.linear_model import LinearRegression
# import numpy as np

# # ---------------- PAGE CONFIG ---------------- #

# st.set_page_config(
#     page_title="Uber Advanced Analytics Dashboard",
#     page_icon="🚖",
#     layout="wide"
# )

# # ---------------- LOAD DATA ---------------- #

# @st.cache_data

# def load_data():
#     df = pd.read_csv("My Uber Drives - 2016.csv")

#     # Remove null purposes
#     df = df.dropna(subset=['PURPOSE*'])

#     # Convert datetime
#     df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], errors='coerce')

#     # Extra columns
#     df['MONTH'] = df['START_DATE*'].dt.month_name()
#     df['DAY'] = df['START_DATE*'].dt.day_name()
#     df['HOUR'] = df['START_DATE*'].dt.hour

#     return df



# df = load_data()

# # ---------------- CUSTOM CSS ---------------- #

# st.markdown("""
# <style>

# .stApp {
#     background: linear-gradient(to right, #edf2f7, #dbeafe);
# }

# .main-title {
#     text-align:center;
#     font-size:55px;
#     font-weight:bold;
#     color:#111827;
#     margin-bottom:20px;
# }

# .card {
#     background:white;
#     padding:25px;
#     border-radius:18px;
#     box-shadow:0px 4px 20px rgba(0,0,0,0.08);
#     text-align:center;
# }

# .metric {
#     font-size:35px;
#     font-weight:bold;
#     color:#2563eb;
# }

# .label {
#     font-size:18px;
#     color:#4b5563;
# }

# [data-testid="stSidebar"] {
#     background-color:#111827;
# }

# [data-testid="stSidebar"] * {
#     color:white;
# }

# </style>
# """, unsafe_allow_html=True)

# # ---------------- TITLE ---------------- #

# st.markdown(
#     "<div class='main-title'>🚖 Uber Drivers Advanced Analytics Dashboard</div>",
#     unsafe_allow_html=True
# )

# # ---------------- SIDEBAR ---------------- #

# st.sidebar.title("📌 Dashboard Filters")

# selected_category = st.sidebar.multiselect(
#     "Select Category",
#     options=df['CATEGORY*'].unique(),
#     default=df['CATEGORY*'].unique()
# )

# selected_purpose = st.sidebar.multiselect(
#     "Select Purpose",
#     options=df['PURPOSE*'].unique(),
#     default=df['PURPOSE*'].unique()
# )

# filtered_df = df[
#     (df['CATEGORY*'].isin(selected_category)) &
#     (df['PURPOSE*'].isin(selected_purpose))
# ]

# # ---------------- KPI CARDS ---------------- #

# c1, c2, c3, c4 = st.columns(4)

# with c1:
#     st.markdown(f"""
#     <div class='card'>
#         <div class='label'>Total Trips</div>
#         <div class='metric'>{len(filtered_df)}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with c2:
#     st.markdown(f"""
#     <div class='card'>
#         <div class='label'>Total Miles</div>
#         <div class='metric'>{round(filtered_df['MILES*'].sum(),2)}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with c3:
#     st.markdown(f"""
#     <div class='card'>
#         <div class='label'>Average Miles</div>
#         <div class='metric'>{round(filtered_df['MILES*'].mean(),2)}</div>
#     </div>
#     """, unsafe_allow_html=True)

# with c4:
#     st.markdown(f"""
#     <div class='card'>
#         <div class='label'>Top Purpose</div>
#         <div class='metric'>{filtered_df['PURPOSE*'].mode()[0]}</div>
#     </div>
#     """, unsafe_allow_html=True)

# st.markdown("##")

# # ---------------- DATASET ---------------- #

# st.subheader("📄 Uber Dataset Preview")
# st.dataframe(filtered_df.head(15))

# st.markdown("---")

# # ---------------- FIRST ROW ---------------- #

# col1, col2 = st.columns(2)

# with col1:

#     fig1 = px.pie(
#         filtered_df,
#         names='CATEGORY*',
#         title='Trips by Category',
#         hole=0.5,
#         color_discrete_sequence=px.colors.sequential.Blues
#     )

#     fig1.update_layout(
#         paper_bgcolor='white',
#         plot_bgcolor='white'
#     )

#     st.plotly_chart(fig1, use_container_width=True)

# with col2:

#     fig2 = px.histogram(
#         filtered_df,
#         x='MILES*',
#         nbins=30,
#         title='Miles Distribution',
#         color_discrete_sequence=['#2563eb']
#     )

#     fig2.update_layout(
#         paper_bgcolor='white',
#         plot_bgcolor='white'
#     )

#     st.plotly_chart(fig2, use_container_width=True)

# # ---------------- SECOND ROW ---------------- #

# col3, col4 = st.columns(2)

# with col3:

#     purpose_df = filtered_df['PURPOSE*'].value_counts().head(10)

#     fig3 = px.bar(
#         purpose_df,
#         x=purpose_df.index,
#         y=purpose_df.values,
#         title='Top Trip Purposes',
#         color=purpose_df.values,
#         color_continuous_scale='Viridis'
#     )

#     fig3.update_layout(
#         xaxis_title='Purpose',
#         yaxis_title='Count',
#         paper_bgcolor='white',
#         plot_bgcolor='white'
#     )

#     st.plotly_chart(fig3, use_container_width=True)

# with col4:

#     monthly_df = filtered_df['MONTH'].value_counts().reset_index()
#     monthly_df.columns = ['Month', 'Trips']

#     fig4 = px.line(
#         monthly_df,
#         x='Month',
#         y='Trips',
#         markers=True,
#         title='Monthly Trips Analysis'
#     )

#     fig4.update_layout(
#         paper_bgcolor='white',
#         plot_bgcolor='white'
#     )

#     st.plotly_chart(fig4, use_container_width=True)

# # ---------------- THIRD ROW ---------------- #

# col5, col6 = st.columns(2)

# with col5:

#     day_df = filtered_df['DAY'].value_counts().reset_index()
#     day_df.columns = ['Day', 'Trips']

#     fig5 = px.area(
#         day_df,
#         x='Day',
#         y='Trips',
#         title='Trips by Day'
#     )

#     fig5.update_layout(
#         paper_bgcolor='white',
#         plot_bgcolor='white'
#     )

#     st.plotly_chart(fig5, use_container_width=True)

# with col6:

#     hour_df = filtered_df['HOUR'].value_counts().reset_index()
#     hour_df.columns = ['Hour', 'Trips']

#     fig6 = px.scatter(
#         hour_df,
#         x='Hour',
#         y='Trips',
#         size='Trips',
#         color='Trips',
#         title='Hourly Trip Analysis'
#     )

#     fig6.update_layout(
#         paper_bgcolor='white',
#         plot_bgcolor='white'
#     )

#     st.plotly_chart(fig6, use_container_width=True)

# # ---------------- BOX PLOT ---------------- #

# fig7 = px.box(
#     filtered_df,
#     y='MILES*',
#     title='Miles Box Plot Analysis',
#     color_discrete_sequence=['#7c3aed']
# )

# fig7.update_layout(
#     paper_bgcolor='white',
#     plot_bgcolor='white'
# )

# st.plotly_chart(fig7, use_container_width=True)

# # ---------------- FOOTER ---------------- #

# st.markdown("---")

# st.markdown("""
# <center>
# <h3 style='color:#111827;'>
# Created by Subalakshmi 🚀
# </h3>
# </center>
# """, unsafe_allow_html=True)




# Advanced Uber Analytics Dashboard (8+ Years Experience Style)

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Uber Advanced Analytics Dashboard",
    page_icon="🚖",
    layout="wide"
)

# ---------------- LOAD DATA ---------------- #

@st.cache_data

def load_data():
    df = pd.read_csv("My Uber Drives - 2016.csv")

    # Remove null purposes
    df = df.dropna(subset=['PURPOSE*'])

    # Convert datetime
    df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], errors='coerce')

    # Extra columns
    df['MONTH'] = df['START_DATE*'].dt.month_name()
    df['DAY'] = df['START_DATE*'].dt.day_name()
    df['HOUR'] = df['START_DATE*'].dt.hour

    return df


df = load_data()

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #edf2f7, #dbeafe);
}

.main-title {
    text-align:center;
    font-size:55px;
    font-weight:bold;
    color:#111827;
    margin-bottom:20px;
}

.card {
    background:white;
    padding:25px;
    border-radius:18px;
    box-shadow:0px 4px 20px rgba(0,0,0,0.08);
    text-align:center;
}

.metric {
    font-size:35px;
    font-weight:bold;
    color:#2563eb;
}

.label {
    font-size:18px;
    color:#4b5563;
}

[data-testid="stSidebar"] {
    background-color:#111827;
}

[data-testid="stSidebar"] * {
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #

st.markdown(
    "<div class='main-title'>🚖 Uber Drivers Advanced Analytics Dashboard</div>",
    unsafe_allow_html=True
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("📌 Dashboard Filters")

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df['CATEGORY*'].unique(),
    default=df['CATEGORY*'].unique()
)

selected_purpose = st.sidebar.multiselect(
    "Select Purpose",
    options=df['PURPOSE*'].unique(),
    default=df['PURPOSE*'].unique()
)

filtered_df = df[
    (df['CATEGORY*'].isin(selected_category)) &
    (df['PURPOSE*'].isin(selected_purpose))
]

# ---------------- KPI CARDS ---------------- #

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class='card'>
        <div class='label'>Total Trips</div>
        <div class='metric'>{len(filtered_df)}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class='card'>
        <div class='label'>Total Miles</div>
        <div class='metric'>{round(filtered_df['MILES*'].sum(),2)}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class='card'>
        <div class='label'>Average Miles</div>
        <div class='metric'>{round(filtered_df['MILES*'].mean(),2)}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class='card'>
        <div class='label'>Top Purpose</div>
        <div class='metric'>{filtered_df['PURPOSE*'].mode()[0]}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("##")

# ---------------- DATASET ---------------- #

st.subheader("📄 Uber Dataset Preview")
st.dataframe(filtered_df.head(15))

st.markdown("---")

# ---------------- FIRST ROW ---------------- #

col1, col2 = st.columns(2)

with col1:

    fig1 = px.pie(
        filtered_df,
        names='CATEGORY*',
        title='Trips by Category',
        hole=0.5,
        color_discrete_sequence=px.colors.sequential.Blues
    )

    fig1.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig1, use_container_width=True)

with col2:

    fig2 = px.histogram(
        filtered_df,
        x='MILES*',
        nbins=30,
        title='Miles Distribution',
        color_discrete_sequence=['#2563eb']
    )

    fig2.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig2, use_container_width=True)

# ---------------- SECOND ROW ---------------- #

col3, col4 = st.columns(2)

with col3:

    purpose_df = filtered_df['PURPOSE*'].value_counts().head(10)

    fig3 = px.bar(
        purpose_df,
        x=purpose_df.index,
        y=purpose_df.values,
        title='Top Trip Purposes',
        color=purpose_df.values,
        color_continuous_scale='Viridis'
    )

    fig3.update_layout(
        xaxis_title='Purpose',
        yaxis_title='Count',
        paper_bgcolor='white',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig3, use_container_width=True)

with col4:

    monthly_df = filtered_df['MONTH'].value_counts().reset_index()
    monthly_df.columns = ['Month', 'Trips']

    fig4 = px.line(
        monthly_df,
        x='Month',
        y='Trips',
        markers=True,
        title='Monthly Trips Analysis'
    )

    fig4.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig4, use_container_width=True)

# ---------------- THIRD ROW ---------------- #

col5, col6 = st.columns(2)

with col5:

    day_df = filtered_df['DAY'].value_counts().reset_index()
    day_df.columns = ['Day', 'Trips']

    fig5 = px.area(
        day_df,
        x='Day',
        y='Trips',
        title='Trips by Day'
    )

    fig5.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig5, use_container_width=True)

with col6:

    hour_df = filtered_df['HOUR'].value_counts().reset_index()
    hour_df.columns = ['Hour', 'Trips']

    fig6 = px.scatter(
        hour_df,
        x='Hour',
        y='Trips',
        size='Trips',
        color='Trips',
        title='Hourly Trip Analysis'
    )

    fig6.update_layout(
        paper_bgcolor='white',
        plot_bgcolor='white'
    )

    st.plotly_chart(fig6, use_container_width=True)

# ---------------- BOX PLOT ---------------- #

fig7 = px.box(
    filtered_df,
    y='MILES*',
    title='Miles Box Plot Analysis',
    color_discrete_sequence=['#7c3aed']
)

fig7.update_layout(
    paper_bgcolor='white',
    plot_bgcolor='white'
)

st.plotly_chart(fig7, use_container_width=True)

# ---------------- PREDICTION CHART ---------------- #

# Future Prediction using Linear Regression
monthly_trips = df.groupby(df['START_DATE*'].dt.month).size()

months = np.array(monthly_trips.index).reshape(-1,1)
trips = monthly_trips.values

model = LinearRegression()
model.fit(months, trips)

future_months = np.array([13,14,15]).reshape(-1,1)
predictions = model.predict(future_months)

future_df = pd.DataFrame({
    'Month':[13,14,15],
    'Predicted Trips':predictions
})

st.subheader("🔮 Future Trip Prediction")

fig_pred = go.Figure()

fig_pred.add_trace(go.Scatter(
    x=monthly_trips.index,
    y=monthly_trips.values,
    mode='lines+markers',
    name='Actual Trips'
))

fig_pred.add_trace(go.Scatter(
    x=future_df['Month'],
    y=future_df['Predicted Trips'],
    mode='lines+markers',
    name='Predicted Trips'
))

fig_pred.update_layout(
    paper_bgcolor='white',
    plot_bgcolor='white'
)

st.plotly_chart(fig_pred, use_container_width=True)

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown("""
<center>
<h3 style='color:#111827;'>
Created by Subalakshmi 🚀
</h3>
</center>
""", unsafe_allow_html=True)


