import base64
import os
from pathlib import Path
import time
import streamlit as st
from PIL import Image
import streamlit.components.v1 as components


def interface():

    st.set_page_config(
        page_title="Escaperoom",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("Digitaal lab")

    tab2, tab1 = st.tabs(["DNA-puzzle", "Achtergrondinformatie"])

    with tab1:
        col1_1, _1, col2_1 = st.columns([10, 1, 10])
        with col1_1:

            st.subheader("PCR")
            st.write("PCR is een techniek om korte stukken DNA heel vaak te kopiëren. Met al die kopieën kun je het genetisch materiaal van (micro)-organismen bestuderen. "
                     "Onderzoekers gebruiken PCR vaak om microben te identificeren: een soort Crime Scene Investigation op microniveau. "
                     "Alle levende organismen hebben genetisch materiaal: DNA. Microben, zoals bacteriën, zijn heel klein en hebben daardoor maar een kleine hoeveelheid DNA. "
                     "In die kleine hoeveelheid zit een hoop informatie verstopt. "
                     "Net als mensen hebben microben ook genen, die samen de instructies vormen voor alle processen in een cel. "
                     "Om het DNA te kunnen bestuderen en ontcijferen hebben we er een bepaalde hoeveelheid van nodig. "
                     "Hier komt PCR om de hoek kijken. Met behulp van een kettingreactie op moleculaire schaal (PCR staat voluit voor Polymerase Chain Reaction) wordt een bepaald stukje DNA heel vaak gekopieerd. "
                     "Hiermee maakt een onderzoeker zo veel kopieën van dat stukje DNA dat hij of zij er analyses mee kan uitvoeren.")
            st.subheader("Snelcursus DNA")
            st.write("De dubbele helixvorm van DNA is bij veel mensen wel bekend: het ziet er uit als een soort gedraaide touwladder. "
                     "Maar laten we eens wat verder inzoomen op de structuur van DNA. "
                     "DNA bestaat uit twee strengen, zeg maar de linker- en de rechterkant van de ladder. "
                     "Een enkele DNA-streng, zegge de linker, is opgebouwd uit bouwblokken (nucleotiden). "
                     "Er is keuze uit maar liefst vier soorten bouwblokken: Adenine (A), Cytosine (C), Guanine (G) en Thymine (T). "
                     "Elk van deze nucleotiden vormt een nieuwe trede op de halve ladder. Dan hebben we de rechter DNA-streng. "
                     "Die is precies tegenovergesteld aan de linker. Een Adenine past namelijk goed aan Thymine, en een Cytosine aan een Guanine. "
                     "Zo vind je altijd rechts een T waar links een A zit, en rechts een G waar links een C zit. "
                     "De dubbele helix bestaat dus uit twee strengen met daarop complementaire informatie: als je weet hoe de linker streng er uit ziet, weet je ook hoe de rechter streng er uit zal zien.")
        with col2_1:
            st.subheader("Wat heb je nodig?")
            st.write("Net als bij een recept, heb je een aantal dingen nodig om een PCR reactie uit te voeren. "
                     "Allereerst het stukje DNA dat gekopieerd moet worden, het origineel. "
                     "Dat wordt het template genoemd. Verder heb je heel veel bouwblokken (nucleotiden) nodig om de nieuwe DNA-streng op te bouwen. "
                     "Ook is er een zogeheten primer nodig. Een primer is een klein stukje enkelstreng DNA dat een beginnetje maakt aan de reactie. "
                     "Door zorgvuldig een primer te kiezen, kunnen wetenschappers precies dat stukje DNA kopiëren wat ze nodig hebben. "
                     "Ten slotte is er een belangrijk enzym nodig, dat Taq-polymerase heet. "
                     "Dit enzym plakt één voor één de juiste bouwblokken A, C, G of T aan de nieuwe streng totdat het hele stuk template DNA gekopieerd is.")
            path = os.path.dirname(__file__)
            dna_file = path+'/Docs/dna.jpg'
            image = Image.open(dna_file)
            st.image(image)
            st.text("")
            st.text("Bron: Artis Micropia")
    with tab2:

        col1_2, _2, col2_2 = st.columns([10, 1, 10])
        # Input layout
        with col1_2:
            st.subheader("Opdracht 1: Bodemmonster")
            st.write("Voer hier het juiste bodemmonster in. "
                     "Zorg er voor dat je zeker weet dat je het juiste monster kiest! "
                     "want bij een fout antwoord gaat de app 2 minuten op slot.")
            path = os.path.dirname(__file__)
            bodemlagen_file = path + "/Docs/bodemlagen.jpg"
            header_html = "<center><img src='data:image/png;base64,{}' class='img-fluid'></center>".format(
                img_to_bytes(bodemlagen_file)
            )
            st.markdown(
                header_html, unsafe_allow_html=True,
            )

            bp = st.selectbox(
                'Selecteer hier het gevraagde bodemmonster',
                ('bodemmonster', 'Bodemmonster A', 'Bodemmonster B', 'Bodemmonster C', 'Bodemmonster D', 'Bodemmonster E', 'Bodemmonster F'))

            # Results Layouts
        with col2_2:
            st.subheader("Opdracht 2: Microbial database")
            st.write(
                "De microbiele database bevat veel DNA sequences. Elke sequentie geeft een specifiek micro-organisme weer. "
                " Aan jullie de taak om de DNA code in te voeren waarmee je stikstof gerelateerde bacterien kunt opsporen!")
            #if submit_bp:
            if bp == "Bodemmonster A":
                wrong_answer()
            if bp == "Bodemmonster B":
                wrong_answer()
            if bp == "Bodemmonster C":
                right_answer()
            if bp == "Bodemmonster D":
                wrong_answer()
            if bp == "Bodemmonster E":
                wrong_answer()
            if bp == "Bodemmonster F":
                wrong_answer()

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def right_answer():
    placeholder = st.empty()
    with placeholder.container():
        with st.form(key='query_form'):
            path = os.path.dirname(__file__)
            krona_file = path + '/Docs/Escaperoom_krona_def.html'
            HtmlFile = open(krona_file, 'r', encoding='utf-8')
            source_code = HtmlFile.read()
            components.html(source_code, width=800, height=310)
            raw_code = st.text_input(max_chars=8, label="DNA sequentie van de primer die je nodig hebt voor stikstof-bacterien")
            submit_code = st.form_submit_button("Invoeren")

    if submit_code:
        if not raw_code.isupper():
            st.info('Dit is niet hoe je een Nucleotide schrijft :)')
        else:
            if raw_code == "TGGTACCT":
                st.success('Hoera! Je hebt de juiste code ingevoerd')
                placeholder.empty()
                popupanswer()

            elif raw_code == "ACCATGGA":
                st.warning('Oeps, je bent er bijna :)')
            else:
                st.warning('Oeps, dit is niet de juiste sequentie, probeer het opnieuw!')


def popupanswer():
    path = os.path.dirname(__file__)
    location_file = path+'/Docs/Locatie-Afsluitdijk.jpg'
    image = Image.open(location_file)
    st.image(image)


def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def wrong_answer():
    hide_btn_style = """
                    <style>
                    [data-baseweb="select"] {visibility: hidden;}
                    [kind="header"] {visibility: hidden;}
                    </style>
                    """

    show_streamlit_style = """
                        <style>
                        [data-baseweb="select"] {visibility: visible;}
                        </style>
                        """
    st.markdown(hide_btn_style, unsafe_allow_html=True)
    placeholder = st.empty()
    placeholder.warning('Sorry dat is het verkeerde antwoord, je kan pas over 2 minuten weer een antwoord indienen')
    with st.empty():
        for seconds in range(120):
            st.write(f"⏳ {seconds}")
            time.sleep(1)
        st.write("✔️ 2 minuten zijn voorbij!")
        placeholder.empty()
        st.markdown(show_streamlit_style, unsafe_allow_html=True)


interface()
