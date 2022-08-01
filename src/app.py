import streamlit as st
from PIL import Image


def interface():

    st.set_page_config(
        page_title="Escaperoom",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("Escaperoom")

    tab1, tab2 = st.tabs(["Information", "Insert sequence"])

    with tab1:
        col1_1, _1, col2_1 = st.columns([10, 1, 10])
        with col1_1:

            st.subheader("PCR")
            st.write("PCR is a technique for copying short pieces of DNA many times. "
                     "With all those copies you can study the genetic material of (micro)organisms. "
                     "Researchers often use PCR to identify microbes: Crime Scene Investigation at the micro level. "
                     "All living organisms have genetic material: DNA. Microbes, such as bacteria, are very small and therefore have only a small amount of DNA. "
                     "A lot of information is hidden in that small amount of DNA. Just like humans, microbes have genes, which together form the instructions for all processes in a cell. "
                     "In order to study and decipher DNA, we need a certain amount of it. This is where PCR comes in. "
                     "Using a chain reaction on a molecular scale (PCR stands for Polymerase Chain Reaction), a certain piece of DNA is copied very often. "
                     "With this, a researcher makes so many copies of that piece of DNA that he or she can carry out analysis with it.")
            st.subheader("DNA crash course")
            st.write("The double helix shape of DNA is well known to many people: it looks like a kind of twisted rope ladder. "
                     "But let's take a closer look at the structure of DNA. DNA consists of two strands, say the left and the right side of the ladder. "
                     "A single strand of DNA, say the left one, is made up of building blocks (nucleotides). "
                     "There is a choice of four types of building blocks: Adenine (A), Cytosine (C), Guanine (G) and Thymine (T). "
                     "Each of these nucleotides forms a new rung on the half ladder. Then we have the right strand of DNA. "
                     "It's exactly opposite to the left. An Adenine fits well to Thymine, and a Cytosine to a Guanine. "
                     "You will always find a T on the right where there is an A on the left, and a G on the right where there is a C on the left. "
                     "The double helix therefore consists of two strands containing complementary information: "
                     "if you know what the left strand looks like, you also know what the right strand will look like.")
        with col2_1:
            st.subheader("What do you need?")
            st.write("Just like a recipe, you need a few things to run a PCR reaction. "
                     "First of all, the piece of DNA that needs to be copied: the original. "
                     "That's called the template. You also need a lot of building blocks (nucleotides) to build the new DNA strand. "
                     "Additionally, a so-called primer is required. A primer is a small piece of single-stranded DNA that initiates the reaction. "
                     "By carefully choosing a primer, scientists can copy exactly the piece of DNA they need. "
                     "Finally, an important enzyme is needed, which is called Taq polymerase. "
                     "This enzyme attaches the correct building blocks A, C, G or T one by one to the new strand until the entire piece of template DNA has been copied.")
            image = Image.open('../Docs/dna.jpg')

            st.image(image, caption='Caption')
    with tab2:
        col1_2, _2, col2_2 = st.columns([10, 1, 10])
        # Input layout
        with col1_2:
            st.subheader("Microbial database")
            st.write("The microbial database holds lots of DNA sequences. Each sequence can be translated to microorganism. "
                     "The found primer will attach to the complementary strand which is in the database and will give you the microorganism!")
            with st.form(key='query_form'):
                raw_code = st.text_input(max_chars=18, label="Complementary primer sequence")
                submit_code = st.form_submit_button("Execute")

            # Results Layouts
        with col2_2:
            st.subheader("Password result")
            st.write("With this result you can go to the next assignment.")
            st.text("")
            st.text("")
            if submit_code:
                if not raw_code.isupper():
                    st.info('This is not how a base pair is written :)')
                else:
                    if raw_code == "TAGC":
                        st.success('Success! The code is: Bacillus')
                    else:
                        st.warning('Oeps, that is not the right sequence, please try again!')


interface()
