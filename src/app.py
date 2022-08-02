import os
import streamlit as st
from PIL import Image


def interface():

    st.set_page_config(
        page_title="Escaperoom",
        page_icon="🧊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("Digitaal lab")

    tab1, tab2 = st.tabs(["Informatie", "Sequentie invoeren"])

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
                     "Hiermee maakt een onderzoeker zo veel kopieën van dat stukje DNA dat hij of zij er analyses mee kan uitvoeren. ")
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
            dna_file = path+'/dna.jpg'
            image = Image.open(dna_file)
            st.image(image)
            st.text("")
            st.text("Bron: Artis Micropia")
    with tab2:
        col1_2, _2, col2_2 = st.columns([10, 1, 10])
        # Input layout
        with col1_2:
            st.subheader("Microbial database")
            st.write("De microbial database bevat veel DNA sequences. Elke sequentie kan worden vertaald naar een micro-organisme. "
                     "Met de gevonden primer vind je het DNA dat past bij een micro-organisme!")
            with st.form(key='query_form'):
                raw_code = st.text_input(max_chars=18, label="Primer sequentie")
                submit_code = st.form_submit_button("Execute")

            # Results Layouts
        with col2_2:
            st.subheader("Password resultaat")
            st.write("Met dit resultaat kun je naar de volgende opdracht.")
            st.text("")
            st.text("")
            if submit_code:
                if not raw_code.isupper():
                    st.info('Dit is niet hoe je een Nucleotide schrijft :)')
                else:
                    if raw_code == "ACGGGGATTCTTGGAGAG":
                        st.success('Hoera! De code is: Bacillus')
                    elif raw_code == "TGCCCCTAAGAACCTCTC":
                        st.warning('Oeps, je bent er bijna :)')
                    else:
                        st.warning('Oeps, dit is niet de goede sequentie, probeer het opnieuw!')

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


interface()
