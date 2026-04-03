import streamlit as st
from datetime import datetime

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Numérologie Pro", page_icon="✨", layout="centered")

# --- FONCTION DE CALCUL NUMÉROLOGIQUE ---
def reduire(n):
    """Réduit un nombre à un chiffre (1-9) sauf maîtres nombres 11, 22, 33"""
    while n > 9 and n not in [11, 22, 33]:
        n = sum(int(digit) for digit in str(n))
    return n

# --- DONNÉES ET TEXTES ---
INTRO = """Le thème numérologique des 12 mois glissants est une boussole vibratoire qui vous permet d'anticiper les énergies dominantes..."""
CONCLUSION = """Que ces vibrations vous guident vers votre plus bel accomplissement..."""

DATA_TEXTES = {
    1: {
        "v1": {
            "pro": "L'aube d'un cycle nouveau se lève sur votre Œuvre...", 
            "coeur": "Un souffle de renouveau anime votre sphère affective...",
            "argent": "Les flux de l'abondance répondent favorablement...",
            "bienetre": "Votre vitalité est à son zénith..."
        },
        "v2": {"pro": "Consolidez votre trône...", "coeur": "Équilibre dans le partage...", "argent": "Récolte des initiatives...", "bienetre": "Maîtrisez votre feu..."},
        "v3": {"pro": "Avènement définitif...", "coeur": "Amour de soi et de l'autre...", "argent": "Maîtrise totale...", "bienetre": "Harmonie souveraine..."}
    },
    2: {
        "v1": {
            "pro": "L'heure est à l'Alliance stratégique...",
            "coeur": "Une vibration de douceur...",
            "argent": "La prospérité dépend de votre équilibre...",
            "bienetre": "Votre sensibilité est votre boussole..."
        },
        "v2": {"pro": "Art du compromis...", "coeur": "Écoute profonde...", "argent": "Prudence payante...", "bienetre": "Attention au fardeau d'autrui..."},
        "v3": {"pro": "Synergie totale...", "coeur": "Fusion accomplie...", "argent": "Cercle vertueux...", "bienetre": "Équilibre Yin/Yang..."}
    },
    # Note : Ajoute ici les blocs 3, 4, 5, 6, 7 que tu as dans ton bloc-notes
}

# --- GESTION DE LA CONNEXION ---
if 'authentifie' not in st.session_state:
    st.session_state['authentifie'] = False

def check_login(email, code):
    # Remplace par tes vrais identifiants si besoin
    return email == "test@pro.com" and code == "1234"

# --- INTERFACE ---
if not st.session_state['authentifie']:
    st.title("🔐 Espace Client Pro")
    with st.form("login"):
        u_email = st.text_input("Email")
        u_code = st.text_input("Code d'accès", type="password")
        if st.form_submit_button("Accéder à mes vibrations"):
            if check_login(u_email, u_code):
                st.session_state['authentifie'] = True
                st.rerun()
            else:
                st.error("Identifiants incorrects")

else:
    st.title("✨ Vos Vibrations Mensuelles")
    st.sidebar.button("Déconnexion", on_click=lambda: st.session_state.update({"authentifie": False}))

    with st.form("infos"):
        col1, col2 = st.columns(2)
        prenom = col1.text_input("Prénom")
        nom = col1.text_input("Nom")
        date_n = col2.date_input("Date de Naissance", min_value=datetime(1940,1,1))
        submit = st.form_submit_button("Générer mon rapport")

    if submit:
        st.markdown(f"### Rapport pour {prenom} {nom}")
        st.write(INTRO)
        
        # Calculs de base
        d = date_n.day
        m = date_n.month
        
        # Départ : mois prochain
        maintenant = datetime.now()
        m_start = maintenant.month + 1
        a_start = maintenant.year
        if m_start > 12: m_start = 1; a_start += 1

        mois_noms = ["Janvier", "Février", "Mars", " Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
        compteur_vibrations = {}

        for i in range(12):
            curr_m_idx = (m_start - 1 + i) % 12
            curr_a = a_start + (m_start - 1 + i) // 12
            
            # Formule Numérologique
            annee_perso = reduire(d + m + curr_a)
            vib_mois = reduire(annee_perso + (curr_m_idx + 1))
            
            # Gestion des versions (v1, v2, v3)
            compteur_vibrations[vib_mois] = compteur_vibrations.get(vib_mois, 0) + 1
            v_key = f"v{min(compteur_vibrations[vib_mois], 3)}"

            # Affichage
            with st.expander(f"✨ {mois_noms[curr_m_idx]} {curr_a} | Vibration {vib_mois}"):
                if vib_mois in DATA_TEXTES:
                    t = DATA_TEXTES[vib_mois][v_key]
                    st.write(f"**💼 Pro :** {t['pro']}")
                    st.write(f"**❤️ Cœur :** {t['coeur']}")
                    st.write(f"**💰 Flux :** {t['argent']}")
                    st.write(f"**🌿 Énergie :** {t['bienetre']}")
                else:
                    st.info(f"Texte pour la vibration {vib_mois} en cours de rédaction.")

        st.info(CONCLUSION)
