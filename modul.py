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
        <div class="anggota">1. Wulan Ramadani</div>
        <div class="anggota">2. Siti Fadila Siregar</div>
        <div class="anggota">3. Zahra Praharani</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

st.header("""1. Text Element""")
st.write("Hello")
st.write("World!")
st.title("This is our Title")
st.header("""This our Header""")
st.subheader("""This is our Sub-header""")
st.caption("""This is our Caption""")

st.markdown("---")

#Displaying Plain Text
st.text("Hi, \nPeople\t!!!!!!!!!")
st.text('welcome to')
st.text("""Streamlit's World""")

st.markdown("---")

#Displaying Markdown
st.markdown("# Hi, \n# ***People*** \t!!!!!!!!!")
st.markdown('## Welcome to')
st.markdown("""### Streamlit's World""")

st.markdown("---")

#Displaying Latex
st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t} 
= h^2 \left( \frac{\partial^2 u}{\partial x^2} 
+ \frac{\partial^2 u}{\partial y^2} 
+ \frac{\partial^2 u}{\partial z^2} \right)''')

st.markdown("---")

#Displaying Python Code
st.subheader("""Python Code""")
code = '''def hello():
print("Hello, Streamlit!")'''
st.code(code, language='python')

st.markdown("---")

# Displaying Java Code
st.subheader("""Java Code""")
st.code("""public class GFG {
public static void main(String args[]) {
    System.out.println("Hello World");
}
""", language="javascript")

st.subheader("""JavaScript Code""")
st.code("""<p id="demo"></p>
<script>
try {
    adddlert("Welcome guest!");
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message;
}
</script> """)

st.markdown("---")


st.header("2. Data Elements")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> DataFrames")
import streamlit as st
import pandas as pd 
import numpy as np

#defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=['col_no %d' % i for i in range(10)])
st.dataframe(df)

st.markdown("---")

import streamlit as st
import pandas as pd
import numpy as np
#defining random values in a dataframe using pandas and numpy
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns= ['col_no %d' % i for i in range(10)])
#Higlighting minimum value objects
st.dataframe(df.style.highlight_min(axis=0))

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Table")
import streamlit as st
import pandas as pd
import numpy as np
# defining  random values in a dataframe using pandas and numpy
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=['col_no %d' % i for i in range(10)])
#defining data in table
st.table(df)

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Metrics")
import streamlit as st

# defining metrics
st.metric(label="Temperature", value="31 °C", delta="1.2 °C")

st.markdown("---")

import streamlit as st 
# defining columns
c1, c2, c3 = st.columns(3)

# defining metrics
c1.metric("Rainfall", "100 cm", "10 cm")
c2.metric(label="Population", value="123 Billions", delta="1 Billions", delta_color="inverse")
c3.metric(label="Customers", value=100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees", "91456", "-1132649")

st.markdown("---")

import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=['col_no %d' % i for i in range(10)]
)

# defining multiple arguments in write function
st.write('Here is our Data', df, 'Data is in dataframe format.\n', '\nWrite is Super function')

st.markdown("---")

# importing necessary libraries
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

# defining random values for Chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b']
)

# defining chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b']
)

# defining chart in write() function
st.write(chart)

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Magic")

# math calculations with no functions defined
"Adding 5 & 4 =", 5+4
# displaying variable 'a' and its value
a = 5
'a', a

# markdown with magic
"""
# magic feature
markdown working without defining its function explicitly.
"""

# dataframe using magic
import pandas as pd
df = pd.DataFrame({'col': [1,2]})
'dataframe', df

st.markdown("---")

# magic working on Charts
import matplotlib.pyplot as plt
import numpy as np

s = np.random.logistic(10, 5, size=5)
fig, ax = plt.subplots()
ax.hist(s, bins=15)

# magic chart
"chart", chart

st.markdown("---")

st.header("3. Data and Media Elements")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Images")
import streamlit as st

st.write("displaying an images")
# displaying image by specifying path
st.image("C:/image_visdat.jpeg")

# image courtesy by unplash
st.write("image courtesy: unplash.com")

st.markdown("---")

import streamlit as st
# image courtesy
st.write("displaying multiple images")
# listing out animal iamges
animal_images = [
    'C:/image/image1.jpeg',
    'C:/image/image2.jpeg',
    'C:/image/image3.jpeg',
    'C:/image/image4.jpeg',
    'C:/image/image5.jpeg',
    'C:/image/image6.jpeg'
]

cols = st.columns(3)

for i, img in enumerate(animal_images):
    with cols[i % 3]:
        st.image(img, width=200)

# displaying multiple images with width 150
#st.image(animal_images, width=150)
# image courtesy
st.write("image courtesy: unplash")

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Background Image")

import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image_(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: unsplash")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("Background Image")
# Calling Image in function
add_local_background_image_('C:/image/download.jpeg')

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Resizing an Image")

import streamlit as st
from PIL import Image

original_image = Image.open("C:/image/home.jpeg")
# display original image
st.title("Original Image")
st.image(original_image)
# resizing image to 600*400
resized_image = original_image.resize((600, 400))
# displaying resized image
st.title("Resized image")
st.image(resized_image)


st.markdown("---")

st.header("4. Buttons and Sliders")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Buttons")
import streamlit as st
st.title('Creating a button')
# defining a button
button = st.button('click here')
if button:
    st.write('you have clicked the Button')
else:
    st.write('you have not clicked the button')

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Radio Buttons")
import streamlit as st
st.title("Creating Radio Buttons")
# defining radio buttons
gender = st.radio(
    "Select your Gender",
    ('Male', 'Female', 'Others'))
if gender == 'Male':
    st.write("You have selected Male")
elif gender == 'Female':
    st.write("You have selected Female")
else:
    st.write("You have selected Others.")

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Check Boxes")
import streamlit as st
st.title('Creating Checkboxes')
st.write('Select your Hobies')
# defining Chexboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Drop-Downs")
import streamlit as st
st.title('Creating Dropdown')
# creating dropdown
hobby = st.selectbox('Choose your hobby: ', ('Books', 'Movies', 'Sports'))

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Multiselects")
import streamlit as st
st.title('Multi-Slect')
# defining Multi_Select with Pre-Seletion
hobbies = st.multiselect(
    'What are your hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing'])

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Download Buttons")
import streamlit as st
st.title('Download  Button')
# creating download button
down_btn = st.download_button(
    label ="Downloa image",
    data=open("C:/image/renjun.jpeg", "rb"),
    file_name="renjun.jpg",
    mime="image/jpg" )

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Progress Bars")
import streamlit as st
import time
st.title('Progress Bar')
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Spinners")
import streamlit as st
import time
st.title('Spinner')
# defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')

st.markdown("---")

st.header("5. Forms")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Text Box")
import streamlit as st
st.title("Text Box")
# creating Text box
name = st.text_input("Enter your name")
st.write("Your name is", name)

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Text Area")
import streamlit as st
# creating text area
input_text = st.text_area("Enter your Review")
# printing entered text
st.write("""You entered: \n""", input_text)

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Number Input")
import streamlit as st
# create number input
st.number_input("Enter your number")

st.markdown("---")

import streamlit as st
# create number input
num = st.number_input("Enter your number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. is 10")
st.write("Default Value is 5, \n Step Size value is 2")
st.write("Total value after adding number entered with dtep value is:", num)

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Time")
import streamlit as st
st.title("Time")
# defining time function
st.time_input("Select your time")

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Date")
import streamlit as st
st.title("Date")
# defining date function
st.date_input("Select Date")

st.markdown("---")

import streamlit as st
import datetime
st.title("Date")
# defining time function
st.date_input("Select your date", value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1,1),
    max_value=datetime.date(2005, 12, 1))

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Color")
import streamlit as st
st.title("Select color")
# defining color picker
color_code = st.color_picker("Select your Color")
st.header(color_code)

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Dataset Upload")
import streamlit as st
import pandas as pd

st.title("CSV Data")

data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")

if details:
    if data_file is not None:
        file_details = {
            "file_name": data_file.name,
            "file_type": data_file.type,
            "file_size": data_file.size
        }
        st.write(file_details)

        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")

st.markdown("---")

# Bikin jarak besar antar bagian
st.markdown("<br>", unsafe_allow_html=True)

st.subheader("> Submit Button")
import streamlit as st
my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')
# defining submit button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)