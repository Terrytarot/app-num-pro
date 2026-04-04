import streamlit as st
from datetime import datetime

# --- 1. CONFIGURATION & CAMOUFLAGE ---
st.set_page_config(page_title="Numérologie Pro", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    /* MASQUAGE TOTAL STREAMLIT */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display:none !important;}
    [data-testid="stDecoration"] {display:none !important;}
    [data-testid="stStatusWidget"] {display:none !important;}
    
    /* Cache le lien Streamlit en bas à droite */
    div[class*="viewerBadge_container"] {display:none !important;}
    div[class*="styles_viewerBadge"] {display:none !important;}
    a[href*="streamlit.io"] {display:none !important;}

    /* DESIGN BLEU NUIT & OR */
    .stApp {
        background: linear-gradient(135deg, #051937 0%, #1a1c4b 100%) !important;
        background-attachment: fixed;
    }
    h1, h2 {
        color: #D4AF37 !important;
        text-align: center;
        text-transform: uppercase;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    label { color: #D4AF37 !important; font-weight: bold !important; }
    .stButton>button {
        background: linear-gradient(90deg, #D4AF37, #FBF5B7) !important;
        color: #051937 !important;
        font-weight: bold !important;
        width: 100% !important;
        border-radius: 10px !important;
        height: 3.5em !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. AUTHENTIFICATION ---
if 'auth' not in st.session_state:
    st.session_state.auth = False

if not st.session_state.auth:
    st.title("ACCÈS RÉSERVÉ")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        email = st.text_input("Email professionnel")
        code = st.text_input("Code d'accès", type="password")
        if st.button("SE CONNECTER"):
            # REMPLACE PAR TES VRAIS ACCÈS ICI
            if email == "tfb13@wanadoo.fr" and code == "Barfle041390":
                st.session_state.auth = True
                st.rerun()
            else:
                st.error("Identifiants incorrects")
    st.stop()

# --- 3. DONNÉES ---
def reduire(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

# J'ai remis ici tout ce que tu m'as transmis
# --- 3. BASE DE DONNÉES INTÉGRALE (TEXTES LONGS) ---
DATA_VIBRATIONS = {
    1: [
        {
            "pro": "L'aube d'un cycle nouveau se lève sur votre Œuvre, marquant le début d'une ère où votre volonté individuelle devient le moteur principal de votre réussite. Cette vibration de primauté vous exhorte à l'initiative pure et à la sortie de votre zone de confort habituelle. Ne soyez point dans l'attente d'une validation extérieure, car l'univers favorise en ce moment les pionniers et ceux qui osent briser les codes établis. C'est le temps de l'affirmation, de l'indépendance et du commandement naturel. Forgez vos projets avec la force de celui qui trace son propre sillage dans une terre encore vierge d'idées.",
            "coeur": "Un souffle de renouveau anime votre sphère affective, invitant à une forme de conquête de soi avant même de chercher la fusion avec l'autre. Cette énergie active peut bousculer les habitudes ronronnantes pour laisser place à une passion plus authentique et plus directe. Pour les âmes liées, c'est un élan de fraîcheur qui demande de redéfinir les bases du couple ; pour les cœurs libres, une rencontre impromptue pourrait naître de votre propre rayonnement et de cette nouvelle assurance que vous dégagez. Ne craignez pas d'exprimer vos désirs les plus profonds avec clarté.",
            "argent": "Les flux de l'abondance répondent favorablement à votre audace et à votre capacité à prendre des risques calculés ce mois-ci. C'est le moment idéal pour semer les graines de la prospérité future par des décisions tranchées et des investissements qui reflètent votre vision à long terme. La stagnation est votre seule ennemie financière ; l'argent doit circuler pour nourrir vos ambitions nouvelles. Investissez en vous-même, dans vos formations ou dans des outils qui augmentent votre autonomie.",
            "bienetre": "Votre vitalité est à son zénith, vous offrant une réserve d'énergie physique et mentale capable de soutenir vos projets les plus lourds. Cependant, cette puissance brute nécessite un exutoire sain pour ne pas se transformer en une tension nerveuse ou en impatience destructrice. Canalisez cette ardeur par une discipline physique régulière, idéalement des exercices qui demandent force et concentration. Préservez la clarté de votre esprit en vous accordant des moments de silence total."
        }
    ],
    2: [
        {
            "pro": "L'heure est à l'Alliance stratégique et à l'exercice subtil de la diplomatie. La force brutale et les décisions solitaires doivent céder le pas à la finesse du discernement et à l'écoute active des besoins de vos partenaires. Vos succès ce mois-ci naîtront de votre capacité unique à unir les contraires et à percevoir les opportunités cachées dans les murmures entre les mots. Cultivez la patience de l'agriculteur, car les fruits les plus savoureux mûrissent toujours dans l'ombre des collaborations fertiles.",
            "coeur": "Une vibration de douceur et de réceptivité enveloppe vos échanges affectifs. Les liens les plus forts se tissent désormais dans la confidence, le partage des silences et une écoute profonde des émotions de l'autre. C'est un temps idéal pour l'harmonie, le pardon sincère et la fusion des âmes qui cherchent un port paisible. Laissez votre intuition guider vos pas vers ceux qui résonnent véritablement avec la fréquence de votre cœur, sans chercher à forcer le destin. La tendresse est votre meilleure alliée.",
            "argent": "La prospérité ce mois-ci dépend étroitement de votre équilibre intérieur et de votre capacité à collaborer. Évitez les mouvements financiers brusques, les investissements impulsifs ou les spéculations solitaires qui pourraient déstabiliser vos acquis. Les gains les plus solides se trouvent dans les associations réfléchies, les contrats de confiance et la gestion sage des ressources partagées. C'est un moment favorable pour conclure des accords basés sur le bénéfice mutuel. L'argent est ici le résultat d'une entente.",
            "bienetre": "Votre sensibilité est actuellement votre boussole la plus précieuse, mais elle vous rend également très perméable aux ambiances et aux énergies environnantes. Protégez votre paix intérieure comme un trésor rare, recherchez la proximité purificatrice de l'eau et écoutez les besoins changeants de votre corps avec une bienveillance maternelle. Évitez les lieux bruyants ou les personnalités toxiques qui pourraient drainer votre vitalité. Des activités comme le yoga vous permettront de maintenir cet équilibre."
        }
    ],
    3: [
        {
            "pro": "L'éclat de la création illumine votre chemin professionnel, transformant chaque défi en une opportunité de briller par votre ingéniosité. Votre parole devient une force de persuasion redoutable et vos idées originales agissent comme des phares dans la nuit pour vos collaborateurs. C'est le mois idéal pour l'expression de vos talents, pour les contacts féconds et pour un rayonnement social sans précédent. Osez paraître sur le devant de la scène et partager vos visions les plus audacieuses, car le monde est enfin prêt à les recevoir.",
            "coeur": "La joie de vivre et une légèreté bienvenue s'invitent à votre table, dissipant les nuages de la mélancolie ou du sérieux excessif. Les échanges affectifs sont teintés d'un humour complice et d'une séduction naturelle qui attirent à vous les regards et les attentions. C'est une période faste pour les nouvelles rencontres, les célébrations entre amis et l'épanouissement des plaisirs sensoriels de l'existence. Laissez votre cœur s'exprimer avec spontanéité, sans peur du jugement ou du qu'en-dira-t-on.",
            "argent": "Une chance subtile mais réelle accompagne vos finances ce mois-ci, souvent déclenchée par votre réseau relationnel ou votre créativité débordante. La fluidité monétaire est favorisée par votre capacité à communiquer sur vos projets et à susciter l'intérêt de nouveaux partenaires. L'abondance peut venir par des voies inattendues, souvent liées à votre charisme ou à un talent que vous aviez jusqu'ici sous-estimé. N'ayez pas peur de mettre en avant vos services ou vos produits ; votre enthousiasme est contagieux.",
            "bienetre": "Votre moral est actuellement votre meilleur remède, agissant comme un bouclier naturel contre la fatigue et le stress. Cultivez l'enthousiasme, entourez-vous de personnes positives et stimulez votre esprit par des activités créatives ou artistiques. Veillez toutefois à ne point disperser votre précieuse essence vitale dans des futilités ou une agitation sociale excessive. Un sommeil régulier et de qualité soutiendra votre pétillance naturelle et préservera l'éclat de votre peau."
        }
    ],
    4: [
        {
            "pro": "L'heure est à l'Édification patiente et rigoureuse de vos ambitions les plus chères. Les rênes du destin demandent en ce moment une main ferme, une discipline de fer et un sens aigu de l'organisation pratique. C'est le temps de la structure, de l'ordre intérieur et du labeur patient qui ne cherche point la lumière immédiate. Construisez brique après brique, sans jamais chercher le raccourci facile, car seules les fondations que vous coulez aujourd'hui résisteront aux tempêtes futures. Votre fiabilité devient votre plus grand atout professionnel.",
            "coeur": "La sécurité émotionnelle et la loyauté indéfectible sont les piliers centraux de ce mois de construction affective. On ne cherche point l'aventure éphémère ou les passions dévastatrices, mais l'ancrage durable dans la réalité du quotidien partagé. C'est le moment idéal pour prouver votre attachement sincère par des actes concrets, une présence rassurante et une écoute qui ne faiblit jamais. Pour les couples, c'est le temps des projets immobiliers ou familiaux solides ; l'amour se prouve ici par la durée et la stabilité.",
            "argent": "La prospérité ce mois-ci ne doit rien au hasard, elle naît directement de votre rigueur et de votre sens de l'économie. Établissez vos comptes avec une précision chirurgicale, prévoyez l'imprévisible et investissez prioritairement dans le durable et le concret. La terre, l'immobilier ou les valeurs refuges sont des alliées sûres sous cette vibration de stabilité retrouvée. Évitez toute forme de spéculation hasardeuse qui pourrait compromettre vos efforts passés. Votre richesse se bâtit sur la prudence.",
            "bienetre": "Votre corps demande aujourd'hui du respect, de la régularité et une structure claire dans votre hygiène de vie. Honorez votre temple physique par une discipline sans faille, en privilégiant une alimentation saine et des horaires de repos fixes. Surveillez particulièrement vos articulations, votre dos et votre ossature ; ne portez point de charges trop lourdes, qu'elles soient réelles ou symboliques. Des exercices de renforcement musculaire ou de la marche régulière en terrain stable vous feront du bien."
        }
    ],
    5: [
        {
            "pro": "Un vent puissant de Mutation souffle sur votre vie professionnelle, balayant les certitudes pour laisser place à l'imprévu créateur. Les chaînes de la routine et de la stagnation se brisent enfin pour vous offrir l'aventure, les voyages ou de nouvelles méthodes de travail révolutionnaires. Soyez tel le voyageur prêt à saisir chaque opportunité au vol, car le mouvement perpétuel est en ce moment votre seule constante bénéfique. Votre capacité d'adaptation et votre agilité mentale seront vos plus grandes forces.",
            "coeur": "L'énergie du désir, de la curiosité et de la liberté individuelle s'intensifie brusquement dans votre sphère sentimentale. C'est un temps idéal pour explorer de nouveaux horizons affectifs, pour rompre avec la monotonie des habitudes et pour redécouvrir avec émerveillement le plaisir de l'imprévu à deux. Laissez-vous surprendre par l'inconnu, osez des expériences qui sortent de votre cadre habituel et libérez-vous des carcans qui étouffaient votre spontanéité. L'amour est une exploration.",
            "argent": "Les flux financiers sont rapides, vifs et parfois instables, demandant une attention de chaque instant et une grande souplesse de réaction. L'argent circule avec une vélocité étonnante ce mois-ci ; il peut entrer en abondance par des voies nouvelles mais peut aussi repartir rapidement pour financer vos soifs de liberté ou de changement. Gardez une main agile sur la bourse tout en restant ouvert aux opportunités d'investissement audacieuses dans les nouvelles technologies.",
            "bienetre": "Une vitalité bouillonnante et une soif d'expérience vous animent, vous poussant à explorer vos limites physiques et mentales. Vous avez un besoin impérieux d'air, d'espace, de nouveauté et de stimuli sensoriels variés pour vous sentir pleinement vivant. Prenez garde toutefois aux excès de toutes sortes et à l'impulsivité qui pourraient fragiliser votre équilibre nerveux à la longue. La respiration profonde et les sports de plein air seront vos meilleurs alliés pour canaliser cette énergie."
        }
    ],
    6: [
        {
            "pro": "L'Harmonie relationnelle et le sens de la Responsabilité partagée sont vos maîtres-mots absolus pour ce mois de construction collective. On attend de vous la justesse d'un juge, la patience d'un diplomate et la bienveillance inspirante d'un mentor pour votre équipe ou vos collaborateurs. C'est le moment idéal pour embellir concrètement votre cadre de travail, apaiser les tensions latentes et assumer pleinement votre rôle de pilier au sein de votre communauté professionnelle. Votre succès est collectif.",
            "coeur": "Le foyer est désormais votre véritable sanctuaire et l'amour la boussole qui oriente chacun de vos choix de vie importants. Cette vibration chaleureuse favorise l'engagement profond, la création d'un cocon protecteur et le soin méticuleux porté aux êtres qui vous sont chers. C'est un temps idéal pour le mariage, l'agrandissement de la famille, une installation commune ou une réconciliation durable. Laissez votre cœur s'exprimer à travers la tendresse et le dévouement.",
            "argent": "L'équilibre financier se trouve ce mois-ci dans la gestion judicieuse des besoins familiaux et dans l'investissement porté sur votre confort personnel et celui des vôtres. Vos décisions monétaires doivent viser avant tout l'amélioration de la qualité de vie et l'embellissement de votre habitat. La générosité équilibrée attire paradoxalement à son tour l'abondance dans votre sphère de vie. C'est un temps favorable pour les investissements immobiliers familiaux ou les assurances.",
            "bienetre": "Le corps et l'esprit réclament aujourd'hui une dose massive de beauté, de douceur et d'harmonie sensorielle pour fonctionner au mieux. Entourez-vous de couleurs apaisantes, écoutez des musiques qui élèvent votre âme et prenez soin de votre équilibre hormonal par des méthodes naturelles. La paix émotionnelle est le gage absolu de votre santé physique ce mois-ci ; évitez les conflits qui drainent votre énergie vitale. Soyez doux avec vous-même, comme vous l'êtes avec les autres."
        }
    ],
    7: [
        {
            "pro": "Le temps semble s'arrêter ce mois-ci pour laisser place à la Connaissance profonde et à la réflexion stratégique de haut vol. Détachez-vous de l'agitation superficielle du monde professionnel pour parfaire vos savoirs et affiner votre vision à long terme. La victoire appartient à celui qui sait voir ce que les autres ignorent par manque de recul. Votre esprit est votre arme la plus tranchante ce mois-ci ; utilisez-le pour analyser, comprendre et planifier vos prochains mouvements avec une précision chirurgicale.",
            "coeur": "Une certaine distance émotionnelle ou physique est temporairement nécessaire pour mieux comprendre la véritable nature de vos sentiments les plus profonds. C'est un temps de solitude choisie et féconde, ou de partage intellectuel intense avec un partenaire capable de comprendre vos silences. Le silence est le terreau sacré où germent actuellement les unions les plus solides. L'amour est ici un mystère sacré qui demande de la patience et une grande honnêteté intellectuelle envers soi-même.",
            "argent": "La gestion de l'argent demande ce mois-ci une grande retenue et une analyse froide des opportunités. Observez les marchés, étudiez les chiffres, mais ne vous hâtez point de conclure des transactions sous l'influence de l'émotion ou de la pression extérieure. Un secret financier ou une information confidentielle pourrait être révélée à votre avantage si vous restez attentif et discret. La richesse vient ici de l'esprit et de la prudence. Évitez les dépenses impulsives ou de prestige.",
            "bienetre": "Le repos de l'esprit et la protection de votre système nerveux sont vos priorités absolues sous cette vibration de sagesse. Méditez, lisez, et n'hésitez point à vous retirer du tumulte social dès que vous en ressentez le besoin impérieux. Votre mental est sollicité par vos réflexions intenses ; accordez-lui le calme et le sommeil profond qu'il réclame pour se régénérer. La proximité de la nature sauvage, des forêts ou des lieux de recueillement sera votre meilleure source de vitalité."
        }
    ],
    8: [
        {
            "pro": "L'heure est à la récolte de vos efforts passés et à l'affirmation de votre autorité naturelle. La vibration 8 vous propulse dans une phase de réalisation concrète où votre sens des affaires et votre capacité à diriger sont vos meilleurs atouts. C'est le moment de viser haut, de négocier avec audace et de prendre la place qui vous revient de droit dans la hiérarchie professionnelle. Votre détermination est votre plus grande force.",
            "coeur": "Une passion intense et une exigence de vérité marquent vos relations ce mois-ci. Vous ne vous contentez plus de l'à-peu-près ou des faux-semblants. En couple, c'est le moment de construire des projets d'envergure, comme un investissement commun ; pour les cœurs libres, votre magnétisme est puissant et lié à votre réussite personnelle. L'amour se vit ici avec une force et une loyauté sans faille.",
            "argent": "Les flux financiers sont particulièrement puissants sous cette vibration de pouvoir. Elle favorise les gains importants, les retours sur investissement et la signature de contrats lucratifs. Cependant, elle demande une gestion rigoureuse et une vision à long terme. C'est le mois idéal pour régler les questions administratives ou juridiques en votre faveur. L'argent est ici le reflet de votre efficacité.",
            "bienetre": "Votre énergie est combative et votre résistance physique est à son maximum. Pour garder l'équilibre face à cette intensité, pratiquez des activités qui demandent de la maîtrise de soi, comme les arts martiaux ou le pilates. Attention toutefois à ne pas accumuler trop de tension dans le haut du corps ; apprenez à relâcher la pression pour préserver votre clarté mentale et votre sommeil."
        }
    ],
    9: [
        {
            "pro": "Vous arrivez au terme d'un cycle majeur, une période de bilan et d'épuration nécessaire avant le renouveau. Cette vibration vous invite à finaliser vos dossiers en cours plutôt qu'à lancer de nouvelles initiatives. Votre intuition est décuplée, vous permettant de percevoir les enjeux globaux de votre carrière avec un recul salvateur. Une ouverture vers l'enseignement, l'international ou des projets à vocation humaine est fortement favorisée ce mois-ci.",
            "coeur": "La vibration 9 apporte une grande compassion et une sensibilité exacerbée dans votre sphère affective. Vous aspirez à un idéal amoureux élevé et à une connexion d'âme profonde. C'est un temps de pardon, de compréhension mutuelle et parfois de détachement nécessaire pour laisser partir ce qui ne vous sert plus. Votre cœur s'ouvre à une dimension plus vaste, privilégiant la qualité émotionnelle et l'authenticité.",
            "argent": "La prudence et la fluidité sont vos guides financiers ce mois-ci. Ce n'est pas une période d'accumulation agressive, mais plutôt de circulation sage des ressources. Terminez vos remboursements, clôturez les vieux comptes et soyez généreux si vous le pouvez. L'argent doit être vu comme une énergie qui circule ; ce que vous libérez aujourd'hui avec sagesse créera l'espace nécessaire pour l'abondance du prochain cycle.",
            "bienetre": "Un grand besoin d'évasion et de ressourcement spirituel se fait sentir. Votre esprit a besoin de calme pour intégrer les leçons du cycle qui s'achève. La méditation, les séjours en bord de mer ou la lecture inspirante sont vos meilleurs alliés. Écoutez la fatigue émotionnelle qui peut survenir et accordez-vous de vrais moments de solitude choisie. Votre régénération passe par le silence et l'introspection."
        }
    ]
}
} # <-- CETTE ACCOLADE FERME LE DICTIONNAIRE

# --- 4. INTERFACE ---
st.title("🔮 NUMÉROLOGIE PRESTIGE")

# Utilisation d'un formulaire pour une validation stable
with st.form("mon_formulaire_prestige"):
    col_a, col_b = st.columns(2)
    with col_a:
        nom = st.text_input("Nom du client")
    with col_b:
        prenom = st.text_input("Prénom du client")
    
    date_naiss = st.date_input("Date de naissance", min_value=datetime(1940, 1, 1))
    
    # Le bouton de validation
    bouton_valider = st.form_submit_button("GÉNÉRER LE THÈME")

if bouton_valider:
    if nom and prenom:
        # 1. Calcul de la vibration (Ex: 14/05 -> 1+4+0+5 = 10 -> 1)
        chiffre_brut = date_naiss.day + date_naiss.month
        chiffre = reduire(chiffre_brut)
        
        st.success(f"Analyse vibratoire terminée pour {prenom} {nom}")
        
        # 2. Affichage des résultats dans l'Expander (Tableau Blanc)
        with st.expander(f"✨ VOTRE SYNTHÈSE : VIBRATION {chiffre}", expanded=True):
            # Rubrique PRO
            st.markdown("#### 💼 Vie Professionnelle")
            st.write(DATA_VIBRATIONS[chiffre][0]["pro"])
            
            # Rubrique COEUR
            st.markdown("#### ❤️ Vie Affective")
            st.write(DATA_VIBRATIONS[chiffre][0]["coeur"])
            
            # Rubrique ARGENT
            st.markdown("#### 💰 Finances & Abondance")
            st.write(DATA_VIBRATIONS[chiffre][0]["argent"])
            
            # Rubrique BIEN-ÊTRE
            st.markdown("#### 🌿 Énergie & Bien-être")
            st.write(DATA_VIBRATIONS[chiffre][0]["bienetre"])
            
    else:
        st.warning("⚠️ Veuillez saisir le nom et le prénom pour générer l'analyse.")
