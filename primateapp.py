import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# file paths
logo_path = r"C:\Users\daisy\Downloads\bblogo.png"
csv_path = r"C:\Users\daisy\Downloads\primate_data - Sheet1.csv"

# Page configuration
st.set_page_config(
    page_title="Primate Life History Explorer",
    page_icon=logo_path,
    layout="wide"
)

st.markdown("""
    <style>
        /* Background gradient and fonts */
        body, .stApp, .main {
            background: linear-gradient(to right, #f4f7f4, #dce4dc) !important;
            font-family: 'Segoe UI', sans-serif;
        }

        /* Title styling */
        h1 {
            color: #2f4f4f;
            font-size: 2.5em;
            margin: 0;
        }

        /* Subheaders styling */
        h2, .stSubheader {
            color: #3b4e3b;
            border-bottom: 1px solid #a8c0a8;
            padding-bottom: 4px;
        }

        /* White background for expander boxes */
        .streamlit-expanderContent {
            background-color: #ffffff !important;
            border-radius: 8px;
            padding: 1rem;
        }

        /* Sidebar forest-green background */
        [data-testid="stSidebar"] > div {
            background-color: #1b3d1b !important;
        }

        /* Sidebar text color white */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] span {
            color: #ffffff !important;
        }

        /* Expander header text */
        .streamlit-expanderHeader {
            font-weight: bold;
            font-size: 1.1em;
            color: #4a684a;
        }

        /* Trait value styling */
        .trait-label {
            font-weight: bold;
            color: #333333;
        }
        .trait-value {
            font-size: 1.4em;
            color: #ff7f0e;
            margin-top: -5px;
            margin-bottom: 1em;
            display: block;
        }

        /* Hide plotly modebar */
        .modebar {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)


# logo and title side by side
col_logo, col_title = st.columns([1, 6], gap="small")
with col_logo:
    st.image(Image.open(logo_path), width=100)
with col_title:
    st.markdown("<h1>Primate Life History Explorer</h1>", unsafe_allow_html=True)
    st.markdown("Explore life history traits of primates in an interactive dashboard.")

# load data
df = pd.read_csv(csv_path)
df.columns = df.columns.str.strip()

# sidebar for species selection
st.sidebar.header("Choose a Primate Species")
common_names = df["Common Name"].dropna().unique()
selected_common = st.sidebar.selectbox("Species:", sorted(common_names))

row = df[df["Common Name"] == selected_common].iloc[0]
binomial_name = row.get("Species", "Not available")
Suborder = row.get("Suborder", "Not available")
Superfamily = row.get("Superfamily", "Not available")
family = row.get("Family", "Not available")
# Display selected species info
col_info, col_image = st.columns([3, 2])

with col_info:
    st.subheader(f"{selected_common}")
    st.subheader(f"{binomial_name}")
    st.markdown(f"**Suborder**: {Suborder}")
    st.markdown(f"**Superfamily**: {Superfamily}")
    st.markdown(f"**Family**: {family}")


with col_image:
    if selected_common.lower() == "aye-aye":  # For Aye-Aye
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/2/2c/Aye-aye_at_night_in_the_wild_in_Madagascar.jpg",
            caption="Photo by Frank Vassen, CC BY-SA 3.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "western lowland gorilla":  # For Western Lowland Gorilla
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/7/71/Western_lowland_gorilla_%28Gorilla_gorilla_gorilla%29.jpg",
            caption="Photo by Mira Meijer, Burgers' Zoo, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "eulemur macaco":  # For Eulemur macaco
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/b/ba/Maki_Nosy_Komba.JPG",
            caption="Photo by Lebelot, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "black-and-white ruffed lemur":  # For Black-and-white Ruffed Lemur
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/5/51/Varecia_variegata_71814266.jpg",
            caption="Photo by Sönke Bonde, CC0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "blue monkey":  # For Blue Monkey
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/7/72/Blue_monkey_%28Cercopithecus_mitis_stuhlmanni%29_pair.jpg",
            caption="Photo by Charles J. Sharp, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "bornean orangutan":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/c/ce/Bornean_orangutan_%28Pongo_pygmaeus%29%2C_Tanjung_Putting_National_Park_11.jpg",
            caption="Photo by Thomas Fuhrmann, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "brown lemur":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/4/45/Eulemur_fulvus_-_akomba_-_varika.jpg",
            caption="Photo by Mendel264, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "calabar angwantibo":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/2/2b/ArctocebusCalabarensisWolf.jpg",
            caption="Illustration by Joseph Wolf, Public domain, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "chimpanzee":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/1/1f/007_Chimpanzee_mother_climbing_a_tree_with_its_baby_at_Kibale_forest_National_Park_Photo_by_Giles_Laurent.jpg",
            caption="Photo by Giles Laurent, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "drill":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/7/7c/Drill_Monkey.jpg",
            caption="Photo by Dotun55, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "eastern lesser bamboo lemur":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/a/a3/Grijze_halfmaki_11.JPG",
            caption="Photo by Heinonlein, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "eastern woolly lemur":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/3/39/Eastern_Avahis_%28Avahi_laniger%29_%2844984841702%29.jpg",
            caption="Photo by Bernard DUPONT from FRANCE, CC BY-SA 2.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "gelada":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/d/dc/Southern_gelada_%28Theropithecus_gelada_obscura%29_female_with_baby.jpg",
            caption="Photo by Charles J. Sharp, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "gray mouse lemur":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/0/09/Gray_Mouse_Lemur_1_edit.JPG",
            caption="Photo by Gabriella Skollar; edited by Rebecca Lewis, CC BY-SA 3.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "hanuman langur":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/b/b4/20191215_Semnopithecus_entellus%2C_Pushkar_1112_8713.jpg",
            caption="Photo by Jakub Hałun, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "indri":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/0/0d/Indri_%28Indri_indri%29.jpg",
            caption="Photo by unknown, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "king colobus":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/b/bd/Colobus_guereza_001.jpg",
            caption="Photo by Ikiwaner, CC BY-SA 3.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "lar gibbon":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/0/08/Gibbon_MichaelMalz.jpg",
            caption="Photo by Michael Malz, CC BY-SA 3.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "long-tailed macaque":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/d/d2/Long-tailed_Macaque_with_infant%2C_Labuk_Bay.jpg",
            caption="Photo by Charlesjsharp, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "mandrill":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/1/18/Mandrillus_sphinx_-_Buffalo_Zoo.jpg",
            caption="Photo by Dave Pape, Public domain, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "mongoose lemur":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/b/bc/Mongoose_Lemur_%2848712005122%29.jpg",
            caption="Photo by Derek Rankine, CC BY-SA 3.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "olive baboon":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/f/fd/Olive_baboon_%28Papio_anubis%29_with_juvenile.jpg",
            caption="Photo by Charles J. Sharp, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "pig-tailed macaque":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/b/b4/Northern_Pig-tailed_Macaque_%28Macaca_leonina%29.jpg",
            caption="Photo by Swapnil Borah, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "potto":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/8/81/Perodicticus_potto_1.jpg",
            caption="Photo by Tom Junek, CC BY 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "red slender loris":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/8/80/Loris_tardigradus_tardigradus_001.jpg",
            caption="Photo by Dr. K.A.I. Nekaris, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "ring-tailed lemur":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/b/ba/Ring-tailed_Lemur_%28Lemur_catta%29.jpg",
            caption="Photo by Tom Junek, CC BY-SA 3.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "siamang":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/0/05/Siamang%281%29.jpg",
            caption="Photo by Rinando Eko Saputra, CC BY-SA 4.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "sunda slow loris":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/7/71/Nycticebus_coucang%2C_the_Sunda_Slow_Loris_%2811662803076%29.jpg",
            caption="Photo by Dick Culbert from Gibsons, B.C., Canada, CC BY 2.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "verreaux's sifaka":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/8/8e/Verreaux%27s_Sifaka_%28Propithecus_verreauxi%29_%288604206716%29.jpg",
            caption="Photo by Ron Knight from Seaford, East Sussex, United Kingdom, CC BY 2.0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "weasel sportive lemur":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/f/fb/Lepilemur_mustelinus.jpg",
            caption="Photo by Brendansoloughlin, CC0, via Wikimedia Commons",
            use_container_width=True
        )
    elif selected_common.lower() == "yellow baboon":
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/d/de/Papio_cynocephalus02.jpg",
            caption="Photo by Esculapio (assumed), Public domain, via Wikimedia Commons",
            use_container_width=True
        )

st.divider()
#  trait categories
trait_categories = {
    "Reproductive Traits": [
        "Gestation Length (days)",
        "Offspring per Litter",
        "Weaning Age (days)",
        "Esterous Cycle Length (days)",
        "Interbirth Interval (days)"
    ],
    "Growth & Maturity": [
        "Female Weight (kg)",
        "Male Weight (kg)",
        "Male Age at First Breeding (months)",
        "Female Age at Sexual Maturity (months)",
        "Male Age at Sexual Maturity",
        "Max Recorded Lifespan (years)",
        "Neonatal Brain Weight (g)",
        "Adult Brain Weight (g)"
    ],
    "Social": ["Mating System","Group Size"]
}

for category, traits in trait_categories.items():
    with st.expander(category, expanded=True):
        cols = st.columns(2)
        for i, trait in enumerate(traits):
            val = row.get(trait, "Not available")
            display_value = "Not available" if pd.isna(val) or val == "-" else val
            # Use custom span for larger orange text
            cols[i % 2].markdown(
                f"<div class='trait-label'>{trait}</div><span class='trait-value'>{display_value}</span>",
                unsafe_allow_html=True
            )

st.divider()
# trait selection for comparison plot
st.subheader("Compare Traits Across Species")

def is_mostly_numeric(series, threshold=0.6):
    cleaned = pd.to_numeric(series.replace(["-", ""], pd.NA), errors='coerce')
    return cleaned.notna().mean() >= threshold

valid_numeric = [col for col in df.columns if is_mostly_numeric(df[col])]
for col in valid_numeric:
    df[col] = pd.to_numeric(df[col].replace(["-", ""], pd.NA), errors='coerce')

col1, col2 = st.columns(2)
with col1:
    x_axis = st.selectbox("X-axis trait:", valid_numeric)
with col2:
    y_axis = st.selectbox("Y-axis trait:", valid_numeric)

plot_df = df.dropna(subset=[x_axis, y_axis])

fig = px.scatter(
    plot_df,
    x=x_axis,
    y=y_axis,
    hover_name="Common Name",
    hover_data=["Species"],
    color="Common Name",
    title=f"{x_axis} vs {y_axis}"
)
fig.update_traces(marker=dict(size=11, line=dict(width=1, color='DarkSlateGrey')))
fig.update_layout(
    legend_title_text='Species',
    title_x=0.5,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(250,250,250,0.95)'
)

st.plotly_chart(fig, use_container_width=True)
