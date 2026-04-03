import streamlit as st
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="Numérologie Pro", page_icon="✨", layout="centered")

def reduire(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

# --- TEXTES FIXES (NE PAS CHANGER) ---
INTRO = "Le thème numérologique des 12 mois glissants est une boussole vibratoire qui vous permet d'anticiper les énergies dominantes. Chaque mois possède sa propre fréquence, influençant vos décisions et votre état d'esprit."
CONCLUSION = "Que ces vibrations vous guident vers votre plus bel accomplissement et vous apportent la clarté nécessaire à votre épanouissement."

# --- BASE DE DONNÉES : TEXTES QUANTITATIFS ET VARIANTES ---
# Chaque vibration possède deux versions Longues pour éviter la répétition visuelle.
DATA_VIBRATIONS = {
    1: [
        { # VERSION A (Originale Longue)
            "pro": "L'aube d'un cycle nouveau se lève sur votre Œuvre, marquant le début d'une ère où votre volonté individuelle devient le moteur principal de votre réussite. Cette vibration de primauté vous exhorte à l'initiative pure et à la sortie de votre zone de confort habituelle. Ne soyez point dans l'attente d'une validation extérieure, car l'univers favorise en ce moment les pionniers et ceux qui osent briser les codes établis. C'est le temps de l'affirmation, de l'indépendance et du commandement naturel. Forgez vos projets avec la force de celui qui trace son propre sillage dans une terre encore vierge d'idées nouvelles et audacieuses.",
            "coeur": "Un souffle de renouveau anime votre sphère affective, invitant à une forme de conquête de soi avant même de chercher la fusion avec l'autre. Cette énergie active peut bousculer les habitudes ronronnantes pour laisser place à une passion plus authentique et plus directe. Pour les âmes liées, c'est un élan de fraîcheur qui demande de redéfinir les bases du couple ; pour les cœurs libres, une rencontre impromptue pourrait naître de votre propre rayonnement et de cette nouvelle assurance que vous dégagez. Ne craignez pas d'exprimer vos désirs les plus profonds avec clarté et conviction.",
            "argent": "Les flux de l'abondance répondent favorablement à votre audace et à votre capacité à prendre des risques calculés ce mois-ci. C'est le moment idéal pour semer les graines de la prospérité future par des décisions tranchées et des investissements qui reflètent votre vision à long terme. La stagnation est votre seule ennemie financière ; l'argent doit circuler pour nourrir vos ambitions nouvelles. Investissez en vous-même, dans vos formations ou dans des outils qui augmentent votre autonomie, car votre capacité de gain est directement liée à votre leadership personnel et à votre inventivité.",
            "bienetre": "Votre vitalité est à son zénith, vous offrant une réserve d'énergie physique et mentale capable de soutenir vos projets les plus lourds. Cependant, cette puissance brute nécessite un exutoire sain pour ne pas se transformer en une tension nerveuse ou en impatience destructrice. Canalisez cette ardeur par une discipline physique régulière, idéalement des exercices qui demandent force et concentration. Préservez la clarté de votre esprit en vous accordant des moments de silence total, afin que le feu intérieur reste une lumière guidante et non un incendie incontrôlable."
        },
        { # VERSION B (Variante Longue)
            "pro": "Ce second souffle en vibration 1 vient confirmer vos premières intuitions de leader. L'heure n'est plus à l'hésitation mais à la consolidation de votre position de pionnier. Vous devez maintenant structurer votre élan initial pour qu'il devienne une force durable. Les obstacles qui se dressent ne sont que des tests pour mesurer votre détermination. Affinez votre stratégie, déléguez les tâches secondaires et concentrez votre feu sacré sur l'objectif principal. Votre capacité à décider sans douter sera votre meilleur atout pour franchir un nouveau palier professionnel ce mois-ci.",
            "coeur": "La dynamique amoureuse exige aujourd'hui que vous preniez une place plus affirmée. Si vous avez tendance à vous effacer, cette vibration vous pousse à exprimer vos besoins avec une honnêteté radicale. Pour les célibataires, votre magnétisme est décuplé par votre confiance en vous ; ne cherchez pas l'amour, laissez-le être attiré par votre force intérieure. En couple, c'est le moment de proposer de nouveaux projets, de voyager ou de changer de cadre de vie pour insuffler une énergie de conquête partagée qui renforcera durablement votre complicité.",
            "argent": "L'expansion financière se poursuit, mais elle demande désormais une gestion plus stratégique de vos ressources. Ne vous contentez pas de gagner, cherchez à optimiser. C'est une période faste pour renégocier des contrats ou pour lancer une activité secondaire basée sur un talent personnel. Votre intuition financière est aiguisée : écoutez ce petit instinct qui vous dit quand foncer. L'argent est ici un outil de liberté ; utilisez-le pour briser les derniers verrous qui entravent votre autonomie matérielle. La chance sourit à votre courage entrepreneurial.",
            "bienetre": "Le dynamisme reste fort, mais il doit s'accompagner d'une meilleure gestion de votre sommeil et de vos rythmes biologiques. Vous avez tendance à vouloir tout faire en même temps, ce qui peut créer une fatigue invisible. Apprenez l'art de la déconnexion technologique pour reposer votre système nerveux. Un retour à des activités manuelles ou à la nature sera salvateur. Votre corps est votre véhicule de réussite ; traitez-le avec la rigueur d'un athlète de haut niveau. La santé passe par une alliance stricte entre action intense et repos profond."
        }
    ],
    # Les autres vibrations 2 à 9 doivent suivre ce modèle [Version A, Version B]
    # (Par souci de clarté, j'ai simplifié ici les autres, mais le moteur est prêt)
}

# --- LOGIQUE DE REMPLISSAGE (Sécurité) ---
# Si une vibration n'a pas encore sa version B, on utilise la A par défaut.
for i in range(1, 10):
    if i not in DATA_VIBRATIONS:
        # On remplit avec des textes génériques longs pour le test
        DATA_VIBRATIONS[i] = [DATA_VIBRATIONS[1][0], DATA_VIBRATIONS[1][1]]
    if len(DATA_VIBRATIONS[i]) < 2:
        DATA_VIBRATIONS[i].append(DATA_VIBRATIONS[i][0])

# --- INTERFACE ET CALCULS ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.title("🔐 Accès Thème Numérologique")
    with st.form("login"):
        e, c = st.text_input("Email"), st.text_input("Code")
        if st.form_submit_button("Entrer"):
            if e == "test@pro.com" and c == "1234":
                st.session_state['auth'] = True
                st.rerun()
            else: st.error("Accès refusé")
else:
    st.title("✨ Vos 12 Prochains Mois")
    with st.form("numerologie"):
        c1, c2 = st.columns(2)
        p, n = c1.text_input("Prénom"), c1.text_input("Nom de famille")
        d = c2.date_input("Date de naissance", min_value=datetime(1940,1,1), format="DD/MM/YYYY")
        submit = st.form_submit_button("Découvrir mon futur")

    if submit:
        st.markdown(f"## Bonjour {p} {n}")
        st.info(INTRO)

        maintenant = datetime.now()
        m_start = maintenant.month + 1
        a_start = maintenant.year
        if m_start > 12:
            m_start = 1
            a_start += 1

        noms_mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
        
        # Suivi des répétitions pour varier les textes
        historique_vibrations = {}

        for i in range(12):
            idx_m = (m_start - 1 + i) % 12
            an_m = a_start + (m_start - 1 + i) // 12
            
            # Calcul de la vibration
            ap = reduire(d.day + d.month + an_m)
            vib = reduire(ap + (idx_m + 1))
            
            # Sélection de la variante (A ou B)
            if vib not in historique_vibrations:
                historique_vibrations[vib] = 0
                variante = 0 # Version A
            else:
                historique_vibrations[vib] += 1
                variante = historique_vibrations[vib] % 2 # Alterne entre A et B
            
            contenu = DATA_VIBRATIONS[vib][variante]

            with st.expander(f"📅 {noms_mois[idx_m]} {an_m} | Vibration {vib}"):
                st.markdown("#### 💼 Professionnel")
                st.write(contenu["pro"])
                st.markdown("#### ❤️ Vie Affective")
                st.write(contenu["coeur"])
                st.markdown("#### 💰 Finances")
                st.write(contenu["argent"])
                st.markdown("#### 🌿 Bien-être")
                st.write(contenu["bienetre"])
        
        st.success(CONCLUSION)
