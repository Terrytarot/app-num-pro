import streamlit as st
from datetime import datetime

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Numérologie Pro", page_icon="✨", layout="centered")

# --- FONCTION DE CALCUL ---
def reduire(n):
    """Réduit un nombre à un chiffre (1-9)."""
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

# --- TEXTES D'INTRODUCTION ET CONCLUSION ---
INTRO = "Le thème numérologique des 12 mois glissants est une boussole vibratoire qui vous permet d'anticiper les énergies dominantes. Chaque mois possède sa propre fréquence, influençant vos décisions et votre état d'esprit."
CONCLUSION = "Que ces vibrations vous guident vers votre plus bel accomplissement et vous apportent la clarté nécessaire à votre épanouissement."

# --- BASE DE DONNÉES UNIQUE ---
DATA_TEXTES = {
    1: {
        "pro": "L'aube d'un cycle nouveau se lève sur votre Œuvre, marquant le début d'une ère où votre volonté individuelle devient le moteur principal de votre réussite. Cette vibration de primauté vous exhorte à l'initiative pure et à la sortie de votre zone de confort habituelle.",
        "coeur": "Un souffle de renouveau anime votre sphère affective, invitant à une forme de conquête de soi avant même de chercher la fusion avec l'autre. Cette énergie active peut bousculer les habitudes ronronnantes pour laisser place à une passion plus authentique.",
        "argent": "Les flux de l'abondance répondent favorablement à votre audace et à votre capacité à prendre des risques calculés ce mois-ci. C'est le moment idéal pour semer les graines de la prospérité future par des décisions tranchées.",
        "bienetre": "Votre vitalité est à son zénith, vous offrant une réserve d'énergie physique et mentale capable de soutenir vos projets les plus lourds. Cependant, cette puissance brute nécessite un exutoire sain pour ne pas se transformer en tension."
    },
    2: {
        "pro": "L'heure est à l'Alliance stratégique et à l'exercice subtil de la diplomatie. La force brutale et les décisions solitaires doivent céder le pas à la finesse du discernement et à l'écoute active des besoins de vos partenaires.",
        "coeur": "Une vibration de douceur et de réceptivité enveloppe vos échanges affectifs. Les liens les plus forts se tissent désormais dans la confidence, le partage des silences et une écoute profonde des émotions de l'autre.",
        "argent": "La prospérité ce mois-ci dépend étroitement de votre équilibre intérieur et de votre capacité à collaborer. Évitez les mouvements financiers brusques ou les spéculations solitaires qui pourraient déstabiliser vos acquis.",
        "bienetre": "Votre sensibilité est actuellement votre boussole la plus précieuse, mais elle vous rend également très perméable aux ambiances environnantes. Protégez votre paix intérieure comme un trésor rare."
    },
    3: {
        "pro": "L'éclat de la création illumine votre chemin professionnel, transformant chaque défi en une opportunité de briller par votre ingéniosité. Votre parole devient une force de persuasion redoutable ce mois-ci.",
        "coeur": "La joie de vivre et une légèreté bienvenue s'invitent à votre table, dissipant les nuages de la mélancolie. Les échanges affectifs sont teintés d'un humour complice et d'une séduction naturelle.",
        "argent": "Une chance subtile mais réelle accompagne vos finances ce mois-ci, souvent déclenchée par votre réseau relationnel ou votre créativité débordante. L'abondance peut venir par des voies inattendues.",
        "bienetre": "Votre moral est actuellement votre meilleur remède, agissant comme un bouclier naturel contre la fatigue et le stress. Cultivez l'enthousiasme et entourez-vous de personnes positives."
    },
    4: {
        "pro": "L'heure est à l'Édification patiente et rigoureuse de vos ambitions les plus chères. Les rênes du destin demandent en ce moment une main ferme, une discipline de fer et un sens aigu de l'organisation.",
        "coeur": "La sécurité émotionnelle et la loyauté indéfectible sont les piliers centraux de ce mois de construction affective. C'est le moment idéal pour prouver votre attachement par des actes concrets.",
        "argent": "La prospérité ce mois-ci ne doit rien au hasard, elle naît directement de votre rigueur et de votre sens de l'économie. Établissez vos comptes avec une précision chirurgicale.",
        "bienetre": "Votre corps demande aujourd'hui du respect, de la régularité et une structure claire dans votre hygiène de vie. Honorez votre temple physique par une discipline sans faille."
    },
    5: {
        "pro": "Un vent puissant de Mutation souffle sur votre vie professionnelle, balayant les certitudes pour laisser place à l'imprévu créateur. Les chaînes de la routine se brisent enfin pour vous offrir l'aventure.",
        "coeur": "L'énergie du désir, de la curiosité et de la liberté individuelle s'intensifie brusquement. C'est un temps idéal pour explorer de nouveaux horizons affectifs et rompre avec la monotonie.",
        "argent": "Les flux financiers sont rapides, vifs et parfois instables, demandant une attention de chaque instant. L'argent circule avec une vélocité étonnante ce mois-ci.",
        "bienetre": "Une vitalité bouillonnante et une soif d'expérience vous animent, vous poussant à explorer vos limites physiques. Vous avez un besoin impérieux d'air et d'espace."
    },
    6: {
        "pro": "L'Harmonie relationnelle et le sens de la Responsabilité partagée sont vos maîtres-mots. On attend de vous la justesse d'un juge et la bienveillance inspirante d'un mentor pour votre équipe.",
        "coeur": "Le foyer est désormais votre véritable sanctuaire et l'amour la boussole qui oriente vos choix. Cette vibration favorise l'engagement profond et la création d'un cocon protecteur.",
        "argent": "L'équilibre financier se trouve dans la gestion judicieuse des besoins familiaux et dans l'investissement porté sur votre confort personnel. La richesse sert ici la paix du foyer.",
        "bienetre": "Le corps et l'esprit réclament aujourd'hui une dose massive de beauté et d'harmonie sensorielle. Entourez-vous de couleurs apaisantes et écoutez des musiques qui élèvent votre âme."
    },
    7: {
        "pro": "Le temps semble s'arrêter pour laisser place à la Connaissance profonde et à la réflexion stratégique. Détachez-vous de l'agitation superficielle pour affiner votre vision à long terme.",
        "coeur": "Une certaine distance émotionnelle est temporairement nécessaire pour mieux comprendre la nature de vos sentiments. C'est un temps de solitude choisie et féconde.",
        "argent": "La gestion de l'argent demande ce mois-ci une grande retenue et une analyse froide des opportunités. Observez les marchés, mais ne vous hâtez point de conclure des transactions.",
        "bienetre": "Le repos de l'esprit et la protection de votre système nerveux sont vos priorités absolues. Méditez, lisez et retirez-vous du tumulte social dès que le besoin s'en fait sentir."
    },
    8: {
        "pro": "La Puissance et l'Accomplissement concret se manifestent avec force. C'est le mois de la récolte : vous obtenez ce que vous avez semé. Affirmez votre ambition et assumez votre autorité.",
        "coeur": "Les sentiments sont vécus avec une intensité volcanique. C'est un temps idéal pour vivre des émotions fortes, mais veillez à ce que cette passion ne devienne pas un besoin de contrôle.",
        "argent": "Les flux financiers sont à leur paroxysme. C'est le moment idéal pour négocier des contrats d'envergure. Votre flair pour les affaires est à son comble ce mois-ci.",
        "bienetre": "Votre énergie vitale est colossale, mais elle peut être brutale pour votre organisme. Apprenez à relâcher chaque muscle après l'effort et accordez-vous des plages de décompression."
    },
    9: {
        "pro": "L'heure est à l'Achèvement de vos projets et à l'Ouverture sur le monde. Un cycle majeur se termine, vous demandant de clore les dossiers en suspens. C'est le temps de la transmission.",
        "coeur": "L'amour se fait universel et compassionnel, vous poussant à donner un sens plus vaste à vos relations. C'est un mois idéal pour le lâcher-prise sur les blessures du passé.",
        "argent": "L'abondance vient par des voies détournées ou des opportunités liées à l'étranger. Ne retenez pas les ressources avec avarice ; laissez-les circuler pour préparer le prochain cycle.",
        "bienetre": "Un besoin de purification totale du corps et de l'esprit se fait sentir. Nettoyez votre organisme et libérez votre mental des rancœurs anciennes pour accueillir le renouveau."
    }
}

# --- AUTHENTIFICATION ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.title("🔐 Accès Thème Numérologique")
    with st.form("login"):
        e = st.text_input("Email")
        c = st.text_input("Code")
        if st.form_submit_button("Entrer"):
            if e == "test@pro.com" and c == "1234":
                st.session_state['auth'] = True
                st.rerun()
            else: st.error("Accès refusé")
else:
    # --- FORMULAIRE ---
    st.title("✨ Vos 12 Prochains Mois")
    with st.form("numerologie"):
        c1, c2 = st.columns(2)
        prenom = c1.text_input("Prénom")
        nom = c1.text_input("Nom de famille")
        # Format français (DD/MM/YYYY) activé ici
        dnais = c2.date_input("Date de naissance", min_value=datetime(1940,1,1), format="DD/MM/YYYY")
        submit = st.form_submit_button("Découvrir mon futur")

    if submit:
        st.markdown(f"## Bonjour {prenom} {nom}")
        st.info(INTRO)

        maintenant = datetime.now()
        m_start = maintenant.month + 1
        a_start = maintenant.year
        if m_start > 12:
            m_start = 1
            a_start += 1

        noms_mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

        for i in range(12):
            idx_mois = (m_start - 1 + i) % 12
            an_actuelle = a_start + (m_start - 1 + i) // 12
            
            ap = reduire(dnais.day + dnais.month + an_actuelle)
            vib = reduire(ap + (idx_mois + 1))
            
            with st.expander(f"📅 {noms_mois[idx_mois]} {an_actuelle} | Vibration {vib}"):
                textes = DATA_TEXTES[vib]
                st.markdown("#### 💼 Professionnel")
                st.write(textes["pro"])
                st.markdown("#### ❤️ Vie Affective")
                st.write(textes["coeur"])
                st.markdown("#### 💰 Finances")
                st.write(textes["argent"])
                st.markdown("#### 🌿 Bien-être")
                st.write(textes["bienetre"])
        
        st.success(CONCLUSION)
