import streamlit as st

# nama anggota kelompok
st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #d63384;
        font-size: 36px;
        font-family: 'Arial Rounded MT Bold', sans-serif;
        margin-bottom: 30px;
    }

    .box {
        background-color: #ffe6f0;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(214, 51, 132, 0.2);
        width: 70%;
        margin: 0 auto;
    }

    .anggota {
        font-size: 20px;
        padding: 5px 0;
        font-family: 'Segoe UI', sans-serif;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Judul
st.markdown('<div class="title">🌸 Daftar Nama Anggota Kelompok 🌸</div>', unsafe_allow_html=True)

# Daftar nama dalam box
st.markdown("""
    <div class="box">
        <div class="anggota">1. Wulan Ramadani (0110223259) </div>
        <div class="anggota">2. Siti Fadila Siregar (0110223245) </div>
        <div class="anggota">3. Zahra Praharani (0110223182)</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

st.header("""1. Visualisasi""")

st.markdown("---")

import streamlit as st
import pandas as pd
import numpy as np
st.title('Area')
# defining dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["c1", "C2", "C3", "C4"])

# bar chart
st.bar_chart(df)

st.markdown("---")

import streamlit as st
import pandas as pd
import numpy as np
st.title('Area')
# defining dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["c1", "C2", "C3", "C4"])

# bar chart
st.line_chart(df)

st.markdown("---")
import streamlit as st
import pandas as pd
import numpy as np
st.title('Area')
# defining dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["c1", "C2", "C3", "C4"])

# bar chart
st.area_chart(df)

st.markdown("---")

import streamlit as st
import pandas as pd
import numpy as np
st.title('Map')
# defining latitude and longitude
locate_map = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns= ['latitude', 'longitude'])

# map function
st.map(locate_map)

st.markdown("---")

import streamlit as st
import graphviz as graphviz

st.title('Graphviz')

# Creating graph object
st.graphviz_chart('''
digraph {
    "Training Data" -> "ML Algorithm"
    "ML Algorithm" -> "Model"
    "Model" -> "Result Forecasting"
    "New Data" -> "Model"
}
''')

import streamlit as st
import graphviz as graphviz

st.title('Graphviz')

# Create a graphlib graph object
graph = graphviz.Digraph()

graph.edge('Training Data', 'ML Algorithm')
graph.edge('ML Algorithm', 'Model')
graph.edge('Model', 'Result Forecasting')
graph.edge('New Data', 'Model')

st.graphviz_chart(graph)

st.markdown("---")

st.header("""2. Columns and Navigation""")

st.markdown("---")

import streamlit as st
st.title('Columns')
col1, col2 = st.columns(2)

# inserting elements in columns 1
col1.write("First Column")
col1.image("C:/image_visdat.jpeg")
# inserting elements in columns 2
col2.write("Second Columns")
col2.image("C:/image_visdat.jpeg")

st.markdown("---")

import streamlit as st
from PIL import Image

img = Image.open("C:/image_visdat.jpeg")
st.title("Spaced-Out Columns")

# Defining two Rows
for _ in range(2):
    # Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)













