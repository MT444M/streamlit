import streamlit as st



backgroundColor = "#FFF0F0"

colum1, colum2=st.columns(2)
with colum1:
    st.image("seatech.png")
with colum2:
    st.image("univtln.png")

# Sidebar with clickable titles
st.sidebar.title("Blue Technology challenges")

# Links to scroll to specific sections on the page
st.sidebar.markdown("""
    <style>
        a {
            text-decoration: none;
            color: black;
            font-weight: bold;
            padding: 8px 0;
            display: block;
        }
        a:hover {
            background-color: #0072C6;
            color: white;
        }
    </style>
    """
    "<a href='#introduction'>Introduction</a>"
    "<a href='#awareness'>Awareness</a>"
    "<a href='#blue-tech-solutions'>Blue Tech Solutions</a>",
    unsafe_allow_html=True,)


st.markdown(
        """
        <div style="background-color:#0072C6;padding:10px;border-radius:10px">
        <h2 style="color:white;text-align:center;">Blue Technology challenges</h2>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Introduction Section
st.markdown(
    """
    <div style="background-color:#FFFFFF; padding:10px; border-radius:10px; border: 2px solid #0072C6; color:Black;">
        <h3 style="color:Blue; text-align:center;">Introduction</h3>
        <p style="text-align: justify;">
            Welcome to our Blue Technology Challenges application, where we delve into the critical issues facing our oceans and explore innovative technological solutions to address them.<br>
            - Overfishing: Examining the impact of overfishing on marine ecosystems and exploring sustainable fishing practices.<br>
            - Pollution of the Sea: Investigating the different forms of pollution affecting the sea, such as plastic pollution, oil spills, and chemical contaminants.<br>
            - Rubbish in the Sea: Addressing the issue of marine debris and exploring initiatives to reduce and clean up waste in our oceans.<br>
            - Climate Change: Understanding the effects of climate change on marine environments and showcasing technological solutions to mitigate its impact.<br>
            - Underwater Installations: Exploring the challenges and advancements in underwater installations, such as offshore wind farms and marine research facilities.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

#st.video("demo.mp4")
st.image("intro.png")
st.write("To find out more, click on the link below to watch the introductory video :"
        "\n https://drive.google.com/file/d/1EyMF5gtRijTV5jM1dZkHJBITl_uR4HwH/view?usp=drivesdk", unsafe_allow_html=True)
#st.write('https://drive.google.com/file/d/1EyMF5gtRijTV5jM1dZkHJBITl_uR4HwH/view?usp=drivesdk', unsafe_allow_html=True)
st.write("\n\n\n\n\n")


# Awareness Section
st.markdown(
    """
           <div style="background-color:#FFFFFF; padding:10px; border-radius:10px; border: 2px solid #0072C6;">
           <h3 style="color:Blue; text-align:center;">Awareness</h3>
           <p style="color:Black; text-align: justify;">
               In order to enhance understanding of the impact of human activities on marine life, we offer a series of interactive quizzes. These quizzes are designed to engage users and test their knowledge on various aspects of marine challenges and conservation efforts.<br>
               The quizzes cover a range of topics, including overfishing, pollution, marine debris, climate change, and underwater installations. By participating in these quizzes, you not only test your knowledge but also contribute to raising awareness about the importance of preserving our oceans.<br>
               Feel free to explore the quizzes, learn more about marine issues, and join us in our mission to protect and sustain our marine ecosystems.
           </p>
        </div>
       """,
        unsafe_allow_html=True,
    )


# Add QR code images with links and passwords
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("quizz_1.jpg", caption="Quiz 1", use_column_width=True)
    st.markdown('https://qruiz.net/Q/?1BVv6e', unsafe_allow_html=True)
    st.write("Code: W5RSDehM")

with col2:
    st.image("quizz_2.jpg", caption="Quiz 2", use_column_width=True)
    st.markdown('https://qruiz.net/Q/?dAFZi6', unsafe_allow_html=True)
    st.write("Code: RfdyhgpA")

with col3:
    st.image("quiz3.png", caption="Quiz 3", use_column_width=True)
    st.markdown('https://qruiz.net/Q/?pVDXsu', unsafe_allow_html=True)
    st.write("Code: 7hwEDR4V")

with col4:
    st.image("quiz4.png", caption="Quiz 4", use_column_width=True)
    st.markdown('https://qruiz.net/Q/?JG7BSx', unsafe_allow_html=True)
    st.write("Code: 2HEe7yW3")

# Blue Tech Solutions Section
st.markdown(
     """
    <div style="background-color:#FFFFFF; padding:10px; border-radius:10px; border: 2px solid #0072C6; color:Black;">
        <h3 style="color:Blue; text-align:center;">Blue Tech Solutions</h3>
        <p style="text-align: justify;">
            We propose 2 Blue Tech solutions to combat degradation in the marine environment:<br>
            - Solution 1: Sea waste collection vessels.<br>
            - Solution 2: Microalgae, ecological allies in water treatment.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# Solution 1

st.image("solution_11.jpg", use_column_width=True)
st.image("solution_12.jpg", use_column_width=True)

# Solution 2

st.image("solution_21.jpg", use_column_width=True)
st.image("solution_22.jpg",  use_column_width=True)

