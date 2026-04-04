import streamlit as st
from datetime import datetime

# --- 1. CONFIGURATION & DESIGN ---
st.set_page_config(page_title="Numérologie Prestige", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #051937 0%, #1a1c4b 100%) !important; background-attachment: fixed; }
    h1, h2, h3 { color: #D4AF37 !important; text-align: center; text-transform: uppercase; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #FBF5B7) !important; color: #051937 !important; font-weight: bold !important; width: 100% !important; border-radius: 10px !important; }
    div[data-testid="stExpander"] { background-color: white !important; border: 2px solid #D4AF37 !important; border-radius: 10px !important; margin-bottom: 10px; }
    div[data-testid="stExpander"] p, div[data-testid="stExpander"] b, div[data-testid="stExpander"] span { color: black !important; }
    label { color: #D4AF37 !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. AUTHENTIFICATION ---
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("ACCÈS RÉSERVÉ")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        email_i = st.text_input("Email professionnel")
        code_i = st.text_input("Code d'accès", type="password")
        if st.button("SE CONNECTER"):
            if email_i == "tfb13@wanadoo.fr" and code_i == "Barfle041390":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Identifiants incorrects")
    st.stop()

# --- 3. FONCTIONS DE CALCUL ---
def reduire(n):
    while n > 9: n = sum(int(digit) for digit in str(n))
    return n

def calculer_expression(nom_complet):
    table = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,
             'j':1,'k':2,'l':3,'m':4,'n':5,'o':6,'p':7,'q':8,'r':9,
             's':1,'t':2,'u':3,'v':4,'w':5,'x':6,'y':7,'z':8}
    total = sum(table.get(char.lower(), 0) for char in nom_complet if char.isalpha())
    return reduire(total)

def obtenir_nom_mois(numero_mois, annee):
    noms = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
    return f"{noms[numero_mois - 1]} {annee}"

# --- 4. BASE DE DONNÉES (PROFIL DE PERSONNALITÉ) ---
PROFIL_NOM = {
    1: "Votre nom vibre sur la fréquence du leader. Vous possédez une force de caractère innée qui influence votre manière de traverser chaque cycle.",
    2: "Votre nom révèle une nature diplomate et intuitive. Vous agissez avec finesse et cherchez l'harmonie dans vos relations professionnelles.",
    3: "Votre identité porte la vibration de la créativité et de la communication. Vous brillez par votre aisance sociale naturelle.",
    4: "Votre nom est ancré dans la structure et la loyauté. Vous abordez vos projets avec une rigueur et un sens de l'organisation remarquables.",
    5: "Votre nom vibre sous le signe de la liberté et de l'adaptation. Vous avez un besoin vital de mouvement et de renouveau constant.",
    6: "Votre identité reflète un sens profond des responsabilités et de l'harmonie familiale. Vous êtes le pilier sur lequel on se repose.",
    7: "Votre nom porte une vibration d'analyse et de sagesse. Vous traversez la vie avec une profondeur d'esprit et un besoin de vérité.",
    8: "Votre nom vibre avec la réussite matérielle et l'autorité. Vous possédez le talent nécessaire pour transformer vos idées en empire.",
    9: "Votre nom révèle une âme humaniste et altruiste. Votre vision dépasse les frontières et cherche toujours un idéal supérieur."
}

# --- 5. BASE DATA_VIBRATIONS (RÉSUMÉ POUR LE CODE) ---
# Note : J'utilise ici vos textes longs fournis précédemment.
DATA_VIBRATIONS = {
    1: {
        "A": {"pro": "L'aube d'un cycle nouveau se lève sur votre Œuvre, marquant le début d'une ère où votre volonté individuelle devient le moteur principal de votre réussite...", "coeur": "Un souffle de renouveau anime votre sphère affective, invitant à une conquête de soi...", "argent": "Les flux de l'abondance répondent favorablement à votre audace...", "bienetre": "Votre vitalité est à son zénith, vous offrant une réserve d'énergie physique..."},
        "B": {"pro": "L'élan créateur initié précédemment demande une structuration plus audacieuse...", "coeur": "L'indépendance affective acquise devient votre plus bel atout...", "argent": "La prospérité est liée à votre capacité d'auto-détermination...", "bienetre": "Une vitalité débordante vous anime..."},
        "C": {"pro": "L'aboutissement de votre positionnement. Vous atteignez une forme de maîtrise...", "coeur": "Une maturité affective exceptionnelle s'installe...", "argent": "Consolidation de vos flux financiers...", "bienetre": "Équilibre parfait entre force et sérénité..."}
    },
    2: {
        "A": {"pro": "L'heure est à l'Alliance stratégique et à l'exercice subtil de la diplomatie...", "coeur": "Une vibration de douceur et de réceptivité enveloppe vos échanges...", "argent": "La prospérité ce mois-ci dépend étroitement de votre équilibre intérieur...", "bienetre": "Votre sensibilité est actuellement votre boussole la plus précieuse..."}
    },
    # ... Ajoutez ici les autres vibrations 3 à 9 avec vos textes complets ...
}

# --- 6. INTERFACE ET GÉNÉRATION ---
st.title("🔮 VOTRE THÈME ANNUEL PRESTIGE")

with st.form("form_global"):
    col_nom, col_prenom = st.columns(2)
    nom = col_nom.text_input("Nom")
    prenom = col_prenom.text_input("Prénom")
    
    st.write("📅 **DATE DE NAISSANCE**")
    c1, c2, c3 = st.columns([1, 1, 1.5]) 
    
    jour = c1.selectbox("Jour", list(range(1, 32)))
    mois = c2.selectbox("Mois", list(range(1, 13)))
    annee = c3.selectbox("Année", list(range(2026, 1919, -1))) 
    
    submit = st.form_submit_button("GÉNÉRER L'ANALYSE DÉTAILLÉE SUR 12 MOIS")

if submit:
    if nom and prenom:
        try:
            # CALCULS
            date_naiss = datetime(annee, mois, jour)
            v_annee = reduire(date_naiss.day + date_naiss.month + reduire(2026))
            v_expression = calculer_expression(f"{prenom} {nom}")
            
            # --- AFFICHAGE DU RÉSULTAT ---
            st.divider()
            st.header(f"✨ ANALYSE DE {prenom.upper()} {nom.upper()}")

            # --- 1. PROFIL D'EXPRESSION (GRIS CLAIR / NOIR NET) ---
            st.markdown(f"""
                <div style="background-color: #f0f2f6; padding: 25px; border-radius: 10px; border: 2px solid #dcdcdc; margin-bottom: 20px; text-align: center;">
                    <h3 style="color: #000000 !important; margin-bottom: 10px; text-shadow: none !important; text-transform: uppercase;">
                        🧬 PROFIL D'EXPRESSION : NOMBRE {v_expression}
                    </h3>
                    <p style="color: #000000 !important; font-size: 1.1em; font-style: italic; line-height: 1.5; text-shadow: none !important; margin: 0;">
                        "{PROFIL_NOM[v_expression]}"
                    </p>
                </div>
            """, unsafe_allow_html=True)

            # --- 2. ANNÉE PERSONNELLE (BLANC / NOIR NET) ---
            st.markdown(f"""
                <div style="background-color: #ffffff; padding: 15px; border-radius: 8px; border-left: 10px solid #D4AF37; margin-bottom: 30px;">
                    <p style="color: #000000 !important; font-size: 1.2em; margin: 0; text-align: center; font-weight: bold; text-shadow: none !important;">
                        📅 VOTRE ANNÉE PERSONNELLE 2026 : VIBRATION {v_annee}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            st.divider()

            # BOUCLE 12 MOIS
            m_start, y_start = 5, 2026
            occurrences = {}

            for i in range(12):
                curr_m = (m_start + i - 1) % 12 + 1
                curr_y = y_start + (m_start + i - 1) // 12
                v_mois = reduire(v_annee + curr_m)
                
                count = occurrences.get(v_mois, 0)
                variant_key = "A" if count == 0 else "B" if count == 1 else "C"
                occurrences[v_mois] = count + 1
                
                data = DATA_VIBRATIONS.get(v_mois, DATA_VIBRATIONS.get(1))
                txt = data.get(variant_key, data["A"])

                with st.expander(f"📅 {obtenir_nom_mois(curr_m, curr_y).upper()} — VIBRATION {v_mois}"):
                    st.markdown(f"#### 💼 Vie Professionnelle")
                    st.write(txt['pro'])
                    st.markdown(f"#### ❤️ Vie Affective")
                    st.write(txt['coeur'])
                    st.markdown(f"#### 💰 Finances & Abondance")
                    st.write(txt['argent'])
                    st.markdown(f"#### 🌿 Énergie & Bien-être")
                    st.write(txt['bienetre'])
                    
        except ValueError:
            st.error("Date invalide.")
    else:
        st.error("Veuillez remplir votre nom et votre prénom.")
