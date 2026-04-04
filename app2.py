import streamlit as st
from datetime import datetime

# --- 1. CONFIGURATION & DESIGN (INCHANGÉ) ---
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

# --- 2. AUTHENTIFICATION (FORÇAGE NOIR NET) ---
if 'auth' not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    # Ce bloc CSS local force le titre h1 en noir et enlève l'ombre portée
    st.markdown("""
        <style>
            .auth-title {
                color: #000000 !important;
                text-shadow: none !important;
                font-weight: bold !important;
                text-align: center !important;
                font-size: 3rem !important;
                margin-bottom: 30px !important;
                display: block !important;
            }
        </style>
        <h1 class="auth-title">ACCÈS RÉSERVÉ</h1>
    """, unsafe_allow_html=True)
    
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
# --- 3. FONCTIONS DE CALCUL (AJOUT DU MODULE LETTRES) ---
def reduire(n):
    while n > 9: n = sum(int(digit) for digit in str(n))
    return n

def calculer_expression(nom_complet):
    # Table de Pythagore : A=1, B=2... I=9, J=1...
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

# --- BASE DATA_VIBRATIONS (VOS TEXTES LONGS A, B, C) ---
# [Le dictionnaire DATA_VIBRATIONS 1 à 9 reste ici identique à votre version précédente]
DATA_VIBRATIONS = {
    1: {
        "A": {"pro": "L'aube d'un cycle nouveau se lève sur votre Œuvre, marquant le début d'une ère où votre volonté individuelle devient le moteur principal de votre réussite. Cette vibration de primauté vous exhorte à l'initiative pure et à la sortie de votre zone de confort habituelle. Ne soyez point dans l'attente d'une validation extérieure, car l'univers favorise en ce moment les pionniers et ceux qui osent briser les codes établis. C'est le temps de l'affirmation, de l'indépendance et du commandement naturel. Forgez vos projets avec la force de celui qui trace son propre sillage dans une terre encore vierge d'idées.", "coeur": "Un souffle de renouveau anime votre sphère affective, invitant à une forme de conquête de soi avant même de chercher la fusion avec l'autre. Cette énergie active peut bousculer les habitudes ronronnantes pour laisser place à une passion plus authentique et plus directe. Pour les âmes liées, c'est un élan de fraîcheur qui demande de redéfinir les bases du couple ; pour les cœurs libres, une rencontre impromptue pourrait naître de votre propre rayonnement et de cette nouvelle assurance que vous dégagez.", "argent": "Les flux de l'abondance répondent favorablement à votre audace et à votre capacité à prendre des risques calculés ce mois-ci. C'est le moment idéal pour semer les graines de la prospérité future par des décisions tranchées et des investissements qui reflètent votre vision à long terme. La stagnation est votre seule ennemie financière ; l'argent doit circuler pour nourrir vos ambitions nouvelles. Investissez en vous-même, dans vos formations ou dans des outils qui augmentent votre autonomie.", "bienetre": "Votre vitalité est à son zénith, vous offrant une réserve d'énergie physique et mentale capable de soutenir vos projets les plus lourds. Cependant, cette puissance brute nécessite un exutoire sain pour ne pas se transformer en une tension nerveuse ou en impatience destructrice. Canalisez cette ardeur par une discipline physique régulière, idéalement des exercices qui demandent force et concentration."},
        "B": {"pro": "L'élan créateur initié précédemment demande une structuration plus audacieuse. Ce mois-ci, votre capacité à innover est décuplée par une expérience déjà acquise. Devenez celui qui impose le rythme des affaires par une vision claire et une exécution sans faille. Les opportunités se multiplient pour ceux qui osent.", "coeur": "L'indépendance affective acquise devient votre plus bel atout de séduction. Dans le couple, vous insufflez une dynamique de projets nouveaux qui brise la routine. C'est un temps de conquête réciproque où chacun respecte l'espace de l'autre tout en vibrant à l'unisson.", "argent": "La prospérité est liée à votre capacité d'auto-détermination. Ce n'est pas le moment de déléguer vos choix financiers. Une opportunité d'investissement dans un projet avant-gardiste se présente ; étudiez-la avec le sérieux d'un bâtisseur prêt à transformer le plomb en or.", "bienetre": "Une vitalité débordante vous anime. Pour canaliser ce surplus d'energy sans créer de tensions nerveuses, privilégiez des activités de haute intensité. Votre corps est en phase de reconstruction active, demandant une nutrition de haute qualité."},
        "C": {"pro": "L'aboutissement de votre positionnement. Vous atteignez une forme de maîtrise où chaque décision semble fluide et évidente. Votre autorité est désormais reconnue par vos pairs comme une évidence naturelle, vous permettant de diriger des projets d'une envergure jusque-là inégalée.", "coeur": "Une maturité affective exceptionnelle s'installe. Vous avez compris que l'amour ne demande pas le sacrifice de soi, mais l'épanouissement mutuel. La relation devient un espace de soutien inconditionnel où le dialogue et la passion cohabitent en parfaite harmonie.", "argent": "Consolidation de vos flux financiers. Les décisions prises au début du cycle portent leurs fruits les plus mûrs. Vous avez établi une base de sécurité qui permet désormais des investissements prestigieux et une gestion sereine de votre patrimoine.", "bienetre": "Équilibre parfait entre force et sérénité. Votre corps a intégré les nouveaux rythmes de ce cycle. Vous ressentez une puissance tranquille qui vous rend invulnérable aux agitations extérieures. La méditation et le travail postural soutiennent votre rayonnement."}
    },
    2: {
        "A": {"pro": "L'heure est à l'Alliance stratégique et à l'exercice subtil de la diplomatie. La force brutale et les décisions solitaires doivent céder le pas à la finesse du discernement et à l'écoute active des besoins de vos partenaires. Vos succès ce mois-ci naîtront de votre capacité unique à unir les contraires et à percevoir les opportunités cachées dans les murmures entre les mots. Cultivez la patience de l'agriculteur, car les fruits les plus savoureux mûrissent toujours dans l'ombre des collaborations fertiles.", "coeur": "Une vibration de douceur et de réceptivité enveloppe vos échanges affectifs. Les liens les plus forts se tissent désormais dans la confidence, le partage des silences et une écoute profonde des émotions de l'autre. C'est un temps idéal pour l'harmonie, le pardon sincère et la fusion des âmes qui cherchent un port paisible. Laissez votre intuition guider vos pas vers ceux qui résonnent véritablement avec la fréquence de votre cœur.", "argent": "La prospérité ce mois-ci dépend étroitement de votre équilibre intérieur et de votre capacité à collaborer. Évitez les mouvements financiers brusques ou les investissements impulsifs. Les gains les plus solides se trouvent dans les associations réfléchies, les contrats de confiance et la gestion sage des ressources partagées. C'est un moment favorable pour conclure des accords basés sur le bénéfice mutuel.", "bienetre": "Votre sensibilité est actuellement votre boussole la plus précieuse, mais elle vous rend également très perméable aux ambiances. Protégez votre paix intérieure, recherchez la proximité purificatrice de l'eau et écoutez les besoins changeants de votre corps avec une bienveillance maternelle. Évitez les lieux bruyants qui pourraient drainer votre vitalité."},
        "B": {"pro": "La collaboration devient votre plus grand levier de croissance. En sachant déléguer et en favorisant le travail d'équipe, vous atteignez des objectifs inaccessibles en solitaire. La patience et l'écoute deviennent vos armes les plus redoutables pour dénouer des négociations complexes.", "coeur": "L'harmonie règne au sein du foyer. C'est un mois idéal pour les réconciliations ou pour approfondir la complicité intellectuelle et spirituelle avec l'être aimé. La fusion est douce, naturelle, et basée sur une confiance mutuelle retrouvée après les remous passés.", "argent": "Recherchez le conseil d'experts ou de partenaires de confiance avant toute transaction majeure. Les gains se font à travers des contrats signés dans un esprit de partage et d'équilibre. La fluidité monétaire est sereine et suit le rythme de vos alliances.", "bienetre": "Besoin de calme et de soins doux pour votre système nerveux. Privilégiez les massages, la relaxation ou la proximité de l'eau pour équilibrer vos fluides corporels. Votre santé dépend de votre capacité à lâcher prise sur les tensions extérieures."},
        "C": {"pro": "Le tact et la médiation résolvent les derniers blocages structurels de vos projets. Votre capacité à unir les talents autour d'un objectif commun fait de vous un partenaire indispensable. Vous récoltez les fruits de votre diplomatie par des contrats pérennes.", "coeur": "Une union sacrée se dessine. La paix affective est votre socle de sérénité. Vous vivez une période de grâce où la compréhension mutuelle dépasse les mots, créant un environnement de sécurité et de tendresse absolue pour vous et vos proches.", "argent": "Flux monétaires régulés par des accords écrits et sécurisants. Votre prudence passée vous permet aujourd'hui de jouir d'une stabilité matérielle confortable. La richesse est le fruit d'une gestion partagée et d'une vision équilibrée du profit.", "bienetre": "Harmonie émotionnelle totale. Votre corps se régénère dans le calme. Vous avez appris à écouter les signaux faibles de votre organisme, vous permettant de maintenir une vitalité constante et apaisée, loin du tumulte des cycles précédents."}
    },
    3: {
        "A": {"pro": "L'éclat de la création illumine votre chemin professionnel, transformant chaque défi en une opportunité de briller par votre ingéniosité. Votre parole devient une force de persuasion redoutable et vos idées originales agissent comme des phares dans la nuit pour vos collaborateurs. C'est le mois idéal pour l'expression de vos talents, pour les contacts féconds et pour un rayonnement social sans précédent. Osez paraître sur le devant de la scène.", "coeur": "La joie de vivre et une légèreté bienvenue s'invitent à votre table, dissipant les nuages de la mélancolie. Les échanges affectifs sont teintés d'un humour complice et d'une séduction naturelle qui attirent à vous les regards. C'est une période faste pour les nouvelles rencontres, les célébrations entre amis et l'épanouissement des plaisirs sensoriels de l'existence.", "argent": "Une chance subtile mais réelle accompagne vos finances ce mois-ci, souvent déclenchée par votre réseau relationnel ou votre créativité débordante. La fluidité monétaire est favorisée par votre capacité à communiquer sur vos projets. L'abondance peut venir par des voies inattendues, souvent liées à votre charisme ou à un talent sous-estimé.", "bienetre": "Votre moral est actuellement votre meilleur remède, agissant comme un bouclier naturel contre la fatigue. Cultivez l'enthousiasme, entourez-vous de personnes positives et stimulez votre esprit par des activités créatives ou artistiques. Veillez toutefois à ne point disperser votre précieuse essence vitale dans une agitation excessive."},
        "B": {"pro": "Communication et rayonnement sont les piliers de votre mois. Votre capacité à vulgariser des concepts complexes fait de vous une figure incontournable de votre milieu. Les projets de groupe sont extrêmement favorisés par votre verve et votre enthousiasme contagieux.", "coeur": "Expression libre des sentiments. Vous osez dire votre amour avec une verve poétique qui touche au cœur. Le plaisir social et les sorties enrichissent votre vie affective, apportant un vent de fraîcheur nécessaire dans votre quotidien amoureux.", "argent": "Favorise les activités liées au commerce, aux médias ou aux arts. Les rentrées d'argent sont liées à votre image de marque et à votre popularité croissante. Votre réseau social devient votre plus grande réserve de valeur et de réussite.", "bienetre": "Vitalité pétillante et humeur radieuse. Vous avez besoin de contacts humains pour vous recharger énergétiquement. Veillez simplement à ne pas trop disperser votre parole pour garder votre ancrage et éviter une fatigue nerveuse en fin de mois."},
        "C": {"pro": "Le rayonnement professionnel atteint son apogée créative. Vous devenez une source d'inspiration pour vos pairs, capable de transformer n'importe quel concept abstrait en une réussite commerciale concrète et éclatante par la simple force de votre charisme.", "coeur": "Échanges pétillants et rencontres stimulantes. L'amour est une fête de l'esprit. Vous vivez des moments de complicité rare où la joie est le moteur principal, permettant de surmonter les anciens blocages par le rire et la légèreté partagée.", "argent": "Prospérité fluide et opportunités multiples. L'argent arrive par le biais de vos connexions les plus créatives. Votre audace sociale paye enfin, ouvrant des portes vers des financements ou des contrats prestigieux que vous n'osiez imaginer.", "bienetre": "Équilibre trouvé dans l'expression totale de soi. Votre corps exulte de joie et votre énergie est stable. Vous rayonnez d'une santé qui vient de l'intérieur, portée par une satisfaction personnelle profonde et une clarté mentale exemplaire."}
    },
    4: {
        "A": {"pro": "L'heure est à l'Édification patiente et rigoureuse de vos ambitions les plus chères. Les rênes du destin demandent en ce moment une main ferme, une discipline de fer et un sens aigu de l'organisation pratique. C'est le temps de la structure, de l'ordre intérieur et du labeur patient qui ne cherche point la lumière immédiate. Construisez brique après brique, sans jamais chercher le raccourci facile.", "coeur": "La sécurité émotionnelle et la loyauté indéfectible sont les piliers centraux de ce mois de construction affective. On ne cherche point l'aventure éphémère, mais l'ancrage durable dans la réalité du quotidien partagé. C'est le moment idéal pour prouver votre attachement sincère par des actes concrets, une présence rassurante et une écoute qui ne faiblit jamais.", "argent": "La prospérité ce mois-ci ne doit rien au hasard, elle naît directement de votre rigueur et de votre sens de l'économie. Établissez vos comptes avec une précision chirurgicale, prévoyez l'imprévisible et investissez prioritairement dans le durable et le concret. La terre, l'immobilier ou les valeurs refuges sont des alliées sûres.", "bienetre": "Votre corps demande aujourd'hui du respect, de la régularité et une structure claire dans votre hygiène de vie. Honorez votre temple physique par une discipline sans faille, en privilégiant une alimentation saine et des horaires de repos fixes. Surveillez particulièrement vos articulations et votre dos."},
        "B": {"pro": "La persévérance porte ses fruits les plus concrets. Vos fondations sont désormais prêtes à supporter des structures plus hautes et plus ambitieuses. Votre sérieux inspire une confiance totale à vos clients, stabilisant votre position sur le long terme.", "coeur": "L'ancrage amoureux est total. Vous bâtissez un sanctuaire inviolable pour votre relation. On valorise la durée, la fidélité et la construction de projets matériels communs au sein du foyer, renforçant le sentiment de sécurité réciproque.", "argent": "Sécurisation des acquis financiers. Vos investissements passés commencent à montrer une solidité exemplaire, vous permettant d'envisager des placements à long terme encore plus sûrs. Votre épargne devient un socle inébranlable pour votre avenir.", "bienetre": "Force physique stable et endurance accrue. Votre corps répond parfaitement à la discipline imposée. La marche régulière et le contact avec la nature brute vous apportent la solidité mentale nécessaire pour maintenir vos efforts professionnels."},
        "C": {"pro": "La maîtrise technique et l'ordre vous permettent de franchir un palier de rentabilité décisif. Vous avez construit un système qui travaille désormais pour vous avec une régularité d'horloger, vous libérant du temps pour la stratégie.", "coeur": "Loyauté éprouvée et complicité bâtie sur le roc. L'amour est un édifice indestructible qui résiste à toutes les pressions extérieures. Vous savourez la tranquillité d'une relation où chaque promesse est tenue avec une honnêteté totale.", "argent": "Patrimoine consolidé et sécurité matérielle garantie. Chaque euro investi avec sagesse renforce votre indépendance future. Vous récoltez la paix d'esprit que vous avez patiemment semée par vos efforts constants d'organisation.", "bienetre": "Ancrage profond et équilibre physiologique. Votre corps est en parfaite harmonie avec vos cycles de travail. Vous ressentez une solidité interne qui vous protège des maladies saisonnières et des agitations émotionnelles passagères."}
    },
    5: {
        "A": {"pro": "Un vent puissant de Mutation souffle sur votre vie professionnelle, balayant les certitudes pour laisser place à l'imprévu créateur. Les chaînes de la routine se brisent enfin pour vous offrir l'aventure ou de nouvelles méthodes de travail révolutionnaires. Soyez tel le voyageur prêt à saisir chaque opportunité au vol. Votre capacité d'adaptation sera votre plus grande force.", "coeur": "L'énergie du désir, de la curiosité et de la liberté individuelle s'intensifie brusquement. C'est un temps idéal pour explorer de nouveaux horizons affectifs, pour rompre avec la monotonie et pour redécouvrir avec émerveillement le plaisir de l'imprévu à deux. Laissez-vous surprendre par l'inconnu, osez des expériences nouvelles.", "argent": "Les flux financiers sont rapides, vifs et parfois instables, demandant une attention de chaque instant. L'argent circule avec une vélocité étonnante ce mois-ci ; il peut entrer en abondance par des voies nouvelles mais peut aussi repartir rapidement pour financer vos soifs de liberté. Gardez une main agile sur la bourse.", "bienetre": "Une vitalité bouillonnante vous anime, vous poussant à explorer vos limites. Vous avez un besoin impérieux d'air, d'espace et de nouveauté pour vous sentir pleinement vivant. Prenez garde toutefois aux excès de toutes sortes qui pourraient fragiliser votre équilibre nerveux. La respiration profonde est essentielle."},
        "B": {"pro": "Nouveaux horizons et adaptabilité agile. Un déplacement ou une rencontre impromptue bouscule positivement votre trajectoire. Votre capacité à pivoter rapidement face aux imprévus devient votre avantage concurrentiel le plus précieux ce mois-ci.", "coeur": "Séduction magnétique et charme imprévisible. Vous attirez l'attention par votre esprit vif et votre soif de liberté. Pour les couples, c'est le moment d'un voyage improvisé ou d'une expérience inédite pour raviver la flamme de la découverte.", "argent": "Flux monétaires dynamiques liés au mouvement. Soyez prêt à réagir en un éclair face à une proposition inattendue. La mobilité de vos actifs et votre intuition financière vous permettent de réaliser des profits rapides et significatifs.", "bienetre": "Besoin impérieux de mouvement et de changement de décor. Votre corps réclame de la variété et des sensations fortes pour évacuer le stress accumulé. Le sport, les voyages éclairs ou les nouvelles activités physiques sont vos moteurs de santé."},
        "C": {"pro": "Maîtrise totale du changement. Vous dominez le chaos par votre agilité et votre sens inné du timing. Les mutations initiées précédemment deviennent des opportunités d'expansion fulgurantes pour votre carrière et votre notoriété.", "coeur": "L'amour se vit comme une aventure renouvelée. Chaque jour est une nouvelle étape riche en surprises et en découvertes mutuelles. Vous avez trouvé l'équilibre parfait entre votre besoin d'indépendance et la fusion émotionnelle.", "argent": "Rentabilité liée à l'innovation et à l'audace. Vos idées les plus originales s'avèrent être les plus lucratives. Vous récoltez les bénéfices de votre souplesse d'esprit par des rentrées d'argent aussi soudaines que gratifiantes.", "bienetre": "Dynamisme exceptionnel et sensation de légèreté. Votre énergie est un moteur puissant de transformation personnelle. Vous vous sentez capable de relever n'importe quel défi, porté par une vitalité qui semble inépuisable et conquérante."}
    },
    6: {
        "A": {"pro": "L'Harmonie relationnelle et le sens de la Responsabilité partagée sont vos maîtres-mots. On attend de vous la justesse d'un juge, la patience d'un diplomate et la bienveillance d'un mentor. C'est le moment idéal pour embellir votre cadre de travail, apaiser les tensions latentes et assumer pleinement votre rôle de pilier au sein de votre équipe.", "coeur": "Le foyer est désormais votre véritable sanctuaire. Cette vibration favorise l'engagement profond, la création d'un cocon protecteur et le soin porté aux êtres chers. C'est un temps idéal pour le mariage, l'agrandissement de la famille ou une réconciliation durable. Laissez votre cœur s'exprimer à travers la tendresse.", "argent": "L'équilibre financier se trouve dans la gestion judicieuse des besoins familiaux et dans l'investissement porté sur votre confort personnel. Vos décisions doivent viser avant tout l'amélioration de la qualité de vie et l'embellissement de votre habitat. La générosité équilibrée attire l'abondance.", "bienetre": "Le corps et l'esprit réclament aujourd'hui une dose massive de beauté et d'harmonie sensorielle. Entourez-vous de couleurs apaisantes, écoutez des musiques qui élèvent votre soul. La paix émotionnelle est le gage absolu de votre santé physique. Soyez doux avec vous-même."},
        "B": {"pro": "Médiation réussie et succès d'équipe. Votre rôle de conciliateur au sein de l'entreprise est crucial. Vous créez un environnement de travail où chacun se sent valorisé, augmentant ainsi la productivité globale par l'harmonie sociale.", "coeur": "Douceur de vivre et protection du clan. Votre foyer rayonne d'une paix contagieuse. C'est une période idéale pour renforcer les liens familiaux ou pour s'occuper de la décoration de votre intérieur, créant un véritable havre de paix.", "argent": "Dépenses réfléchies pour le bien-être durable. Vos finances servent à bâtir un avenir serein pour vos proches. Les investissements dans l'immobilier ou les assurances familiales sont extrêmement favorisés ce mois-ci par votre sens des responsabilités.", "bienetre": "Équilibre hormonal et digestif optimal. Soignez votre alimentation avec amour et privilégiez les moments de partage autour d'une belle table. La convivialité et la beauté de votre environnement sont vos meilleurs médicaments naturels."},
        "C": {"pro": "Médiation souveraine et influence bienveillante. Votre capacité à résoudre les conflits fait de vous une figure incontournable de votre milieu professionnel. Vous récoltez le respect et la loyauté de tous vos collaborateurs.", "coeur": "Amour inconditionnel et grâce affective. Vous vivez une période de communion rare où les besoins de l'autre passent avant les vôtres avec joie. La relation est fluide, dénuée de tensions, et centrée sur l'harmonie du nid familial.", "argent": "Flux monétaires stabilisés par une gestion exemplaire. L'argent n'est plus une source de stress mais un serviteur dévoué à votre confort de vie. Votre générosité passée vous revient sous forme d'une sécurité matérielle pérenne.", "bienetre": "Sérénité absolue et rayonnement sensoriel. Vous êtes en paix totale avec votre image et votre corps. Votre santé est excellente, portée par un mental apaisé et un environnement esthétique qui nourrit vos sens au quotidien."}
    },
    7: {
        "A": {"pro": "Le temps semble s'arrêter pour laisser place à la Connaissance profonde et à la réflexion stratégique. Détachez-vous de l'agitation superficielle pour parfaire vos savoirs et affiner votre vision. La victoire appartient à celui qui sait voir ce que les autres ignorent. Votre esprit est votre arme la plus tranchante ; utilisez-le pour analyser.", "coeur": "Une certaine distance émotionnelle est temporairement nécessaire pour mieux comprendre la véritable nature de vos sentiments. C'est un temps de solitude choisie et féconde, ou de partage intellectuel intense avec un partenaire capable de comprendre vos silences. Le silence est le terreau où germent les unions les plus solides.", "argent": "La gestion de l'argent demande une grande retenue et une analyse froide. Étudiez les chiffres, mais ne vous hâtez point de conclure des transactions sous l'influence de l'émotion. Un secret financier pourrait être révélé à votre avantage si vous restez attentif et discret. La richesse vient de l'esprit.", "bienetre": "Le repos de l'esprit est votre priorité absolue. Méditez, lisez, et n'hésitez point à vous retirer du tumulte social. Votre mental est sollicité par vos réflexions intenses ; accordez-lui le calme et le sommeil profond qu'il réclame pour se régénérer. La proximité de la nature sera votre source de vitalité."},
        "B": {"pro": "Expertise approfondie et sagesse stratégique. Vos analyses passées se transforment en décisions prophétiques. Vous agissez avec un temps d'avance car vous avez pris le temps de l'étude, vous plaçant au-dessus de la mêlée concurrentielle.", "coeur": "Mystère, profondeur et échanges spirituels. Vos relations atteignent une dimension sacrée où l'on communique par l'âme. Vous cherchez la vérité derrière les apparences, renforçant les liens avec ceux qui partagent votre quête de sens.", "argent": "Révélation financière et investissement de l'esprit. Une opportunité liée à la recherche ou à un domaine spécialisé se présente. Votre patience et votre discrétion vous permettent de réaliser une opération financière particulièrement judicieuse.", "bienetre": "Régénération par le silence et l'étude. Votre cerveau a besoin de pauses régulières sans écrans. La méditation transcendantale ou la lecture de textes philosophiques nourrit votre vitalité physique autant que votre sérénité mentale."},
        "C": {"pro": "Maîtrise intellectuelle et reconnaissance de votre savoir-faire. Vous devenez la référence dans votre domaine de spécialisation. Votre parole est écoutée comme celle d'un expert dont la vision stratégique est infaillible et respectée.", "coeur": "Union des esprits et paix intérieure partagée. La connexion intellectuelle est le moteur de votre bonheur amoureux. Vous vivez une période de grâce où le calme et la réflexion commune soudent votre relation plus que n'importe quelle passion éphémère.", "argent": "Prudence récompensée et gains intellectuels. Votre gestion sage vous met à l'abri des fluctuations du marché. Vous récoltez les bénéfices de votre clairvoyance passée, assurant une pérennité financière basée sur la connaissance plutôt que sur la chance.", "bienetre": "Paix mentale totale et harmonie spirituelle. Votre système nerveux est parfaitement apaisé, vous offrant une clarté de vue et une santé physique robuste. Vous avez atteint un état de détachement serein qui vous rend invincible face au stress."}
    },
    8: {
        "A": {"pro": "L'heure est à la récolte de vos efforts passés et à l'affirmation de votre autorité naturelle. La vibration 8 vous propulse dans une phase de réalisation concrète où votre sens des affaires et votre capacité à diriger sont vos meilleurs atouts. C'est le moment de viser haut, de négocier avec audace et de prendre la place qui vous revient de droit dans la hiérarchie professionnelle. Votre détermination est votre plus grande force.", "coeur": "Une passion intense et une exigence de vérité marquent vos relations ce mois-ci. Vous ne vous contentez plus de l'à-peu-près ou des faux-semblants. En couple, c'est le moment de construire des projets d'envergure, comme un investissement commun ; pour les cœurs libres, votre magnétisme est puissant et lié à votre réussite personnelle.", "argent": "Les flux financiers sont particulièrement puissants sous cette vibration de pouvoir. Elle favorise les gains importants, les retours sur investissement et la signature de contrats lucratifs. Cependant, elle demande une gestion rigoureuse et une vision à long terme. C'est le mois idéal pour régler les questions administratives ou juridiques.", "bienetre": "Votre énergie est combative et votre résistance physique est à son maximum. Pour garder l'équilibre face à cette intensité, pratiquez des activités qui demandent de la maîtrise de soi, comme les arts martiaux ou le pilates. Attention toutefois à ne pas accumuler trop de tension dans le haut du corps."},
        "B": {"pro": "Puissance de concrétisation et ambition affirmée. Vous dominez les enjeux matériels avec une aisance royale. Votre force de caractère et votre vision stratégique vous permettent de franchir des étapes décisives vers une réussite éclatante et durable.", "coeur": "Loyauté et puissance du lien amoureux. L'amour se vit avec une intensité royale, sans compromis. C'est le mois idéal pour officialiser une situation, prendre des responsabilités familiales de poids ou sceller une union par un engagement matériel fort.", "argent": "Maîtrise totale du destin financier. Vous savez faire fructifier chaque ressource que vous touchez. C'est le moment de viser des sommets, de réinvestir vos bénéfices et de négocier avec une autorité naturelle qui impose le respect de vos débiteurs.", "bienetre": "Vitalité conquérante mais nerveuse. Votre puissance doit être canalisée par un sport intense pour éviter de devenir une source d'agressivité. Surveillez votre tension artérielle et accordez-vous des moments de décompression totale pour durer."},
        "C": {"pro": "Souveraineté professionnelle et succès matériel retentissant. Votre autorité est désormais indiscutable et vos résultats parlent pour vous. Vous dirigez votre carrière vers des sommets de notoriété et de puissance, consolidant votre empire brique après brique.", "coeur": "Passion constructive et foyer puissant. Votre couple devient une force de frappe sociale. Ensemble, vous réalisez des objectifs de vie ambitieux, soudés par une volonté commune de réussite et une loyauté qui défie le temps et les obstacles.", "argent": "Expansion fulgurante de vos actifs et abondance royale. Vous attirez la richesse par votre simple présence et votre sens aiguisé de l'opportunité. La sécurité matérielle est totale, vous permettant de jouer dans la cour des grands avec sérénité.", "bienetre": "Régénération physique de haute performance. Votre corps répond à l'exigence de vos ambitions avec une résilience étonnante. Vous rayonnez d'une force tranquille qui impressionne votre entourage et témoigne d'une maîtrise de soi absolue."}
    },
    9: {
        "A": {"pro": "Vous arrivez au terme d'un cycle majeur, une période de bilan et d'épuration nécessaire avant le renouveau. Cette vibration vous invite à finaliser vos dossiers en cours plutôt qu'à lancer de nouvelles initiatives. Votre intuition est décuplée, vous permettant de percevoir les enjeux globaux avec un recul salvateur. Ouverture vers l'international favorisée.", "coeur": "La vibration 9 apporte une grande compassion et une sensibilité exacerbée. Vous aspirez à un idéal amoureux élevé et à une connexion d'âme profonde. C'est un temps de pardon, de compréhension mutuelle et parfois de détachement nécessaire pour laisser partir ce qui ne vous sert plus. Votre cœur s'ouvre à une dimension plus vaste.", "argent": "La prudence et la fluidité sont vos guides financiers ce mois-ci. Ce n'est pas une période d'accumulation agressive, mais plutôt de circulation sage. Terminez vos remboursements, clôturez les vieux comptes. L'argent doit être vu comme une énergie qui circule librement pour créer l'espace du nouveau cycle.", "bienetre": "Un grand besoin d'évasion et de ressourcement spirituel se fait sentir. Votre esprit a besoin de calme pour intégrer les leçons du cycle qui s'achève. La méditation, les voyages ou la lecture inspirante sont vos meilleurs alliés. Écoutez votre fatigue émotionnelle et accordez-vous des moments de solitude choisie."},
        "B": {"pro": "Sagesse finale, transmission et bilan glorieux. Vous bouclez vos projets avec la main d'un maître. C'est le mois idéal pour préparer le terrain du futur cycle tout en partageant votre savoir-faire avec ceux qui prendront la relève de vos dossiers terminés.", "coeur": "Amour universel, altruisme et communion d'âme. Votre cœur s'élargit aux dimensions du monde, apportant une paix profonde dans vos relations. Pour les couples, c'est une phase de compréhension mutuelle qui dépasse les anciens conflits de l'ego pour une fusion sacrée.", "argent": "Lâcher-prise financier et générosité éclairée. En réglant vos dettes morales ou matérielles, vous débloquez des situations stagnantes. L'argent arrive souvent de manière inattendue, comme une récompense pour votre parcours de vie et votre intégrité.", "bienetre": "Détoxination physique et mentale profonde. Libérez-vous des toxines et des pensées sombres. La lumière, les thérapies énergétiques et le silence contemplatif vous guérissent, préparant votre corps à la renaissance énergétique du mois prochain."},
        "C": {"pro": "Rayonnement international et achèvement prestigieux. Ce que vous avez semé durant les neuf dernières années arrive à une apothéose gratifiante. Vous êtes prêt à passer à une étape de vie totalement nouvelle, porté par une notoriété établie et respectée.", "coeur": "Élévation de l'âme et amour inconditionnel. Vous vivez des moments de communion rare qui transforment votre vision du couple. Vous savourez la paix d'une relation épurée de ses scories, centrée sur l'essentiel : la présence et la beauté du lien éternel.", "argent": "Sagesse monétaire et abondance fluide. Vous comprenez que la véritable richesse est celle qui sert vos idéaux. Vos besoins sont comblés par la loi de l'attraction, vous permettant de vivre ce mois de transition dans une sérénité matérielle absolue.", "bienetre": "Harmonie holistique et paix intérieure totale. Votre corps, votre âme et votre esprit s'alignent parfaitement. Vous ressentez une légèreté divine, comme si vous aviez enfin déposé tous les fardeaux du cycle passé pour accueillir la lumière du renouveau."}
    }
}

# =========================================================
# =========================================================
# --- 6. INTERFACE ET GÉNÉRATION (VERSION NETTOYÉE) ---
# =========================================================
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

            # --- 1. PROFIL D'EXPRESSION (GRIS CLAIR / TEXTE NOIR NET / SANS EMOJI) ---
            st.markdown(f"""
                <div style="
                    background-color: #f0f2f6; 
                    padding: 25px; 
                    border-radius: 10px; 
                    border: 1px solid #dcdcdc; 
                    margin-bottom: 20px; 
                    text-align: center;
                    box-shadow: none !important;
                ">
                    <h3 style="
                        color: #000000 !important; 
                        margin-bottom: 10px; 
                        text-shadow: none !important; 
                        font-weight: 800 !important; 
                        text-transform: uppercase;
                    ">
                        PROFIL D'EXPRESSION : NOMBRE {v_expression}
                    </h3>
                    <p style="
                        color: #000000 !important; 
                        font-size: 1.1em; 
                        font-style: italic; 
                        line-height: 1.5; 
                        text-shadow: none !important; 
                        margin: 0;
                    ">
                        "{PROFIL_NOM[v_expression]}"
                    </p>
                </div>
            """, unsafe_allow_html=True)

            # --- 2. ANNÉE PERSONNELLE (FOND BLANC / TEXTE NOIR / ADIEU LE BLEU) ---
            st.markdown(f"""
                <div style="
                    background-color: #ffffff; 
                    padding: 15px; 
                    border-radius: 8px; 
                    border: 2px solid #D4AF37; 
                    margin-bottom: 30px;
                    box-shadow: none !important;
                ">
                    <p style="
                        color: #000000 !important; 
                        font-size: 1.25em; 
                        margin: 0; 
                        text-align: center; 
                        font-weight: bold; 
                        text-shadow: none !important;
                    ">
                        VOTRE ANNÉE PERSONNELLE 2026 : VIBRATION {v_annee}
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            st.divider()

            # --- 3. BOUCLE 12 MOIS (UTILISE VOS TEXTES LONGS ORIGINAUX) ---
            m_start, y_start = 5, 2026
            occurrences = {}

            for i in range(12):
                curr_m = (m_start + i - 1) % 12 + 1
                curr_y = y_start + (m_start + i - 1) // 12
                v_mois = reduire(v_annee + curr_m)
                
                count = occurrences.get(v_mois, 0)
                variant_key = "A" if count == 0 else "B" if count == 1 else "C"
                occurrences[v_mois] = count + 1
                
                data = DATA_VIBRATIONS.get(v_mois, DATA_VIBRATIONS[1])
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
                    
        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")
    else:
        st.error("Veuillez remplir votre nom et votre prénom.")
