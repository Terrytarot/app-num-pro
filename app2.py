import streamlit as st
from datetime import datetime

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Numérologie Pro", page_icon="✨", layout="centered")

# --- FONCTION DE CALCUL ---
def reduire(n):
    """Réduit un nombre à un chiffre (1-9) sauf maîtres nombres 11, 22, 33"""
    while n > 9 and n not in [11, 22, 33]:
        n = sum(int(digit) for digit in str(n))
    return n

# --- TEXTES FIXES ---
INTRO = """Le thème numérologique des 12 mois glissants est une boussole vibratoire qui vous permet d'anticiper les énergies dominantes..."""
CONCLUSION = """Que ces vibrations vous guident vers votre plus bel accomplissement..."""

# --- BASE DE DONNÉES DES TEXTES ---
DATA_TEXTES = {
    1: {
        "v1": {
            "pro": """L'aube d'un cycle nouveau se lève sur votre Œuvre, marquant le début d'une ère où votre volonté individuelle devient le moteur principal de votre réussite. Cette vibration de primauté vous exhorte à l'initiative pure et à la sortie de votre zone de confort habituelle. Ne soyez point dans l'attente d'une validation extérieure, car l'univers favorise en ce moment les pionniers et ceux qui osent briser les codes établis. C'est le temps de l'affirmation, de l'indépendance et du commandement naturel. Forgez vos projets avec la force de celui qui trace son propre sillage dans une terre encore vierge d'idées.""",
            "coeur": """Un souffle de renouveau anime votre sphère affective, invitant à une forme de conquête de soi avant même de chercher la fusion avec l'autre. Cette énergie active peut bousculer les habitudes ronronnantes pour laisser place à une passion plus authentique et plus directe. Pour les âmes liées, c'est un élan de fraîcheur qui demande de redéfinir les bases du couple ; pour les cœurs libres, une rencontre impromptue pourrait naître de votre propre rayonnement et de cette nouvelle assurance que vous dégagez. Ne craignez pas d'exprimer vos désirs les plus profonds avec clarté.""",
            "argent": """Les flux de l'abondance répondent favorablement à votre audace et à votre capacité à prendre des risques calculés ce mois-ci. C'est le moment idéal pour semer les graines de la prospérité future par des décisions tranchées et des investissements qui reflètent votre vision à long terme. La stagnation est votre seule ennemie financière ; l'argent doit circuler pour nourrir vos ambitions nouvelles. Investissez en vous-même, dans vos formations ou dans des outils qui augmentent votre autonomie, car votre capacité de gain est directement liée à votre leadership personnel.""",
            "bienetre": """Votre vitalité est à son zénith, vous offrant une réserve d'énergie physique et mentale capable de soutenir vos projets les plus lourds. Cependant, cette puissance brute nécessite un exutoire sain pour ne pas se transformer en une tension nerveuse ou en impatience destructrice. Canalisez cette ardeur par une discipline physique régulière, idéalement des exercices qui demandent force et concentration. Préservez la clarté de votre esprit en vous accordant des moments de silence total, afin que le feu intérieur reste une lumière et non un incendie incontrôlable."""
        },
        "v2": {
            "pro": """Le rappel de la Vibration 1 vous invite à consolider le trône que vous avez commencé à bâtir lors de votre première impulsion. Consolidez vos acquis avec la force tranquille du souverain.""",
            "coeur": """L'indépendance acquise lors de la première phase doit maintenant trouver son point d'équilibre dans le partage sans perdre votre identité propre.""",
            "argent": """La récolte de vos premières initiatives se précise et demande une gestion de plus en plus fine pour assurer la pérennité de vos projets.""",
            "bienetre": """Apprenez à maîtriser votre feu intérieur avec la précision d'un artisan, en équilibrant action intense et repos régénérateur."""
        },
        "v3": {
            "pro": """Cette troisième occurrence de l'Unité signe votre avènement définitif en tant que maître absolu de votre destin. Votre vision est claire et votre action est pure.""",
            "coeur": """L'amour de soi et l'amour de l'autre fusionnent enfin en une identité émotionnelle solide et sereine, libre de toute dépendance.""",
            "argent": """La maîtrise des flux financiers est désormais totale et intuitive, vous permettant d'agir avec une liberté souveraine.""",
            "bienetre": """Une harmonie souveraine s'installe dans chaque cellule de votre être, témoignant de votre alignement parfait avec l'univers."""
        }
    },
    2: {
        "v1": {
            "pro": """L'heure est à l'Alliance stratégique et à l'exercice subtil de la diplomatie. La force brutale et les décisions solitaires doivent céder le pas à la finesse du discernement et à l'écoute active des besoins de vos partenaires. Vos succès ce mois-ci naîtront de votre capacité unique à unir les contraires et à percevoir les opportunités cachées dans les murmures entre les mots. Cultivez la patience de l'agriculteur, car les fruits les plus savoureux mûrissent toujours dans l'ombre des collaborations fertiles.""",
            "coeur": """Une vibration de douceur et de réceptivité enveloppe vos échanges affectifs. Les liens les plus forts se tissent désormais dans la confidence, le partage des silences et une écoute profonde des émotions de l'autre. C'est un temps idéal pour l'harmonie, le pardon sincère et la fusion des âmes qui cherchent un port paisible.""",
            "argent": """La prospérité ce mois-ci dépend étroitement de votre équilibre intérieur et de votre capacité à collaborer. Évitez les mouvements financiers brusques, les investissements impulsifs ou les spéculations solitaires qui pourraient déstabiliser vos acquis. Les gains les plus solides se trouvent dans les associations réfléchies.""",
            "bienetre": """Votre sensibilité est actuellement votre boussole la plus précieuse, mais elle vous rend également très perméable aux ambiances et aux énergies environnantes. Protégez votre paix intérieure comme un trésor rare, recherchez la proximité purificatrice de l'eau."""
        },
        "v2": {
            "pro": """Le retour de la dualité dans votre ciel professionnel vous demande d'approfondir l'art délicat du compromis sans vous perdre.""",
            "coeur": """L'écoute devient une seconde nature, vous permettant de percevoir les besoins non-dits de ceux que vous aimez avec une clarté nouvelle.""",
            "argent": """La prudence et la gestion partagée portent enfin leurs fruits, stabilisant vos flux financiers sur le long terme.""",
            "bienetre": """Attention à ne point porter indéfiniment le fardeau émotionnel d'autrui au détriment de votre propre équilibre vital."""
        },
        "v3": {
            "pro": """L'apothéose de la coopération se manifeste dans votre vie professionnelle, créant une synergie où 1+1 égale bien plus que 2.""",
            "coeur": """La fusion est enfin accomplie à un niveau vibratoire supérieur, où le "nous" transcende les ego individuels dans une paix totale.""",
            "argent": """L'abondance vient désormais de la gratitude et du partage équitable, créant un cercle vertueux de richesse partagée.""",
            "bienetre": """L'équilibre parfait entre vos polarités Yin et Yang est désormais atteint, vous offrant une sérénité inébranlable face au monde."""
        }
    },
    3: {
        "v1": {
            "pro": """L'éclat de la création illumine votre chemin professionnel, transformant chaque défi en une opportunité de briller par votre ingéniosité. Votre parole devient une force de persuasion redoutable.""",
            "coeur": """La joie de vivre et une légèreté bienvenue s'invitent à votre table, dissipant les nuages de la mélancolie ou du sérieux excessif. Les échanges affectifs sont teintés d'un humour complice.""",
            "argent": """Une chance subtile mais réelle accompagne vos finances ce mois-ci, souvent déclenchée par votre réseau relationnel ou votre créativité débordante.""",
            "bienetre": """Votre moral est actuellement votre meilleur remède, agissant comme un bouclier naturel contre la fatigue et le stress. Cultivez l'enthousiasme."""
        },
        "v2": {
            "pro": """Le retour de la vibration 3 vous invite à opérer une transition majeure vers la transmission de votre savoir créatif.""",
            "coeur": """La légèreté des débuts laisse place à une joie plus profonde et ancrée, basée sur une connaissance mutuelle joyeuse et pétillante.""",
            "argent": """Gérez vos succès financiers récents avec davantage de discernement pour transformer l'opportunité en richesse durable.""",
            "bienetre": """Il est temps de canaliser votre nervosité créatrice pour préserver votre paix intérieure face aux sollicitations du monde."""
        },
        "v3": {
            "pro": """Votre génie créatif atteint désormais sa pleine maturité et une reconnaissance indiscutable dans votre domaine de prédilection.""",
            "coeur": """L'amour est désormais vécu comme une fête permanente de l'esprit et du cœur, où chaque jour est une célébration de la vie.""",
            "argent": """La prospérité fleurit désormais naturellement grâce à votre renommée et à la qualité inégalée de votre expression personnelle.""",
            "bienetre": """Une vitalité radieuse et communicative émane de chaque pore de votre peau, signe d'une santé totale et rayonnante."""
        }
    },
    4: {
        "v1": {
            "pro": """L'heure est à l'Édification patiente et rigoureuse de vos ambitions les plus chères. Les rênes du destin demandent en ce moment une main ferme, une discipline de fer.""",
            "coeur": """La sécurité émotionnelle et la loyauté indéfectible sont les piliers centraux de ce mois de construction affective. On ne cherche point l'aventure éphémère.""",
            "argent": """La prospérité ce mois-ci ne doit rien au hasard, elle naît directement de votre rigueur et de votre sens de l'économie. Établissez vos comptes avec précision.""",
            "bienetre": """Votre corps demande aujourd'hui du respect, de la régularité et une structure claire dans votre hygiène de vie. Honorez votre temple physique."""
        },
        "v2": {
            "pro": """Le retour du bâtisseur dans votre cycle vous demande de vérifier avec minutie la solidité de ce que vous avez érigé jusqu'ici.""",
            "coeur": """L'engagement sentimental se confirme et s'approfondit sous le poids des responsabilités partagées assumées avec joie.""",
            "argent": """La patience et le travail acharné finissent par payer de manière concrète, apportant des résultats tangibles à vos finances.""",
            "bienetre": """Attention à ne point tomber dans une certaine rigidité, tant physique que mentale, qui pourrait finir par vous fragiliser."""
        },
        "v3": {
            "pro": """Vous atteignez désormais le rang de Maître d'Œuvre, celui qui n'a plus besoin de manipuler chaque pierre pour que l'édifice monte.""",
            "coeur": """La fondation affective sur laquelle vous avez travaillé est désormais éternelle et indestructible aux yeux de tous.""",
            "argent": """La richesse est désormais sécurisée et vous passez définitivement de l'accumulation anxieuse à la gestion sereine d'un patrimoine.""",
            "bienetre": """Une robustesse exceptionnelle et une vitalité de roc vous habitent désormais, témoignant de votre victoire sur les aléas de la vie."""
        }
    },
    5: {
        "v1": {
            "pro": """Un vent puissant de Mutation souffle sur votre vie professionnelle, balayant les certitudes pour laisser place à l'imprévu créateur. Les chaînes de la routine se brisent.""",
            "coeur": """L'énergie du désir, de la curiosité et de la liberté individuelle s'intensifie brusquement dans votre sphère sentimentale. C'est un temps idéal pour explorer.""",
            "argent": """Les flux financiers sont rapides, vifs et parfois instables, demandant une attention de chaque instant et une grande souplesse de réaction.""",
            "bienetre": """Une vitalité bouillonnante et une soif d'expérience vous animent, vous poussant à explorer vos limites physiques et mentales. Vous avez besoin d'air."""
        },
        "v2": {
            "pro": """Le retour du mouvement perpétuel dans votre carrière ne vous surprend plus ; cette fois, vous ne subissez plus le changement, vous le dirigez avec brio.""",
            "coeur": """La liberté ne signifie plus pour vous l'errance ou l'instabilité, mais le choix conscient de la nouveauté perpétuelle.""",
            "argent": """La ruse, l'agilité mentale et un sens aigu de la négociation servent admirablement vos finances lors de cette seconde phase.""",
            "bienetre": """Il est crucial ce mois-ci de calmer l'orage intérieur avant qu'il ne se transforme en un stress chronique handicapant."""
        },
        "v3": {
            "pro": """C'est l'heure de la libération professionnelle totale et de l'avènement de votre propre méthode révolutionnaire. Vous avez intégré le changement.""",
            "coeur": """Le cœur n'a désormais plus de frontières ni de peurs, vous vivez une liberté sentimentale magnifique où la confiance a remplacé le contrôle.""",
            "argent": """L'argent vient désormais vers vous par le mouvement pur, la créativité sans entraves et votre capacité à connecter des mondes différents.""",
            "bienetre": """Une jeunesse extraordinaire du corps et de l'esprit se manifeste en vous, comme si le mouvement vous avait immunisé contre le vieillissement."""
        }
    },
    6: {
        "v1": {
            "pro": """L'Harmonie relationnelle et le sens de la Responsabilité partagée sont vos maîtres-mots absolus. On attend de vous la justesse d'un juge.""",
            "coeur": """Le foyer est désormais votre véritable sanctuaire et l'amour la boussole qui oriente chacun de vos choix de vie importants.""",
            "argent": """L'équilibre financier se trouve ce mois-ci dans la gestion judicieuse des besoins familiaux et dans l'amélioration du confort personnel.""",
            "bienetre": """Le corps et l'esprit réclament aujourd'hui une dose massive de beauté, de douceur et d'harmonie sensorielle. Entourez-vous de calme."""
        },
        "v2": {
            "pro": """L'exigence du service envers autrui s'accentue dans votre vie professionnelle, faisant de vous la figure centrale du groupe.""",
            "coeur": """L'amour se fait aujourd'hui sacrifice joyeux et don de soi, dans la joie profonde de voir l'autre s'épanouir.""",
            "argent": """Les fruits de votre loyauté passée et de votre sérieux sont enfin là, apportant une stabilité financière qui vous permet de souffler.""",
            "bienetre": """Attention à ne point vous oublier totalement dans le soin constant porté aux autres. Apprenez à dire non avec douceur."""
        },
        "v3": {
            "pro": """Vous incarnez désormais la Sagesse du Conseil au sein de votre environnement professionnel, devenant une figure d'inspiration.""",
            "coeur": """Vous accédez à l'expérience du Grand Amour, celui qui ne demande rien et qui offre tout dans une plénitude affective irradiante.""",
            "argent": """L'abondance de confort et la paix matérielle totale caractérisent votre situation financière en cette phase de maîtrise.""",
            "bienetre": """Une santé basée sur l'équilibre parfait et une connaissance intuitive de votre corps vous procurent un sentiment de jeunesse durable."""
        }
    },
    7: {
        "v1": {
            "pro": """Le temps semble s'arrêter ce mois-ci pour laisser place à la Connaissance profonde et à la réflexion stratégique de haut vol. Détachez-vous de l'agitation.""",
            "coeur": """Une certaine distance émotionnelle ou physique est temporairement nécessaire pour mieux comprendre la véritable nature de vos sentiments.""",
            "argent": """La gestion de l'argent demande ce mois-ci une grande retenue et une analyse froide des opportunités. Observez les marchés sans hâte.""",
            "bienetre": """Le repos de l'esprit et la protection de votre système nerveux sont vos priorités absolues. Méditez et cherchez le calme."""
        },
        "v2": {
            "pro": """Votre intuition devient un outil de travail redoutable : vous voyez ce que les autres ne perçoivent pas encore. Travaillez dans le calme.""",
            "coeur": """La connexion d'âme à âme est privilégiée : vous vivez des moments de grâce et de compréhension mutuelle sans paroles.""",
            "argent": """Des opportunités inattendues surgissent grâce à votre intuition. Soyez attentif aux signes et aux rencontres fortuites.""",
            "bienetre": """Une harmonie profonde s'installe entre votre mental et votre corps. Vous ressentez une paix intérieure qui se reflète sur votre vitalité."""
        },
        "v3": {
            "pro": """Vous accédez à la Sagesse Visionnaire : votre vision professionnelle dépasse largement le cadre habituel. Vous devenez un guide recherché.""",
            "coeur": """L'amour est vécu comme une Communion Sacrée, une fusion des esprits et des cœurs. Vous atteignez un niveau de compassion naturelle.""",
            "argent": """L'Abondance Consciente se manifeste : vos besoins sont comblés car vous agissez en accord total avec les lois universelles.""",
            "bienetre": """Une conscience corporelle totale et une maîtrise de vos énergies vitales caractérisent votre état actuel. Vous incarnez le sage."""
        }
    },
    8: {
        "v1": {
            "pro": """La Puissance et l'Accomplissement concret se manifestent avec force. C'est le mois de la récolte : vous obtenez ce que vous avez semé.""",
            "coeur": """Les sentiments sont vécus avec une intensité volcanique. C'est un temps idéal pour vivre des émotions fortes et utiliser votre magnétisme.""",
            "argent": """Les flux financiers sont à leur paroxysme. C'est le moment idéal pour négocier des contrats d'envergure ou restructurer vos avoirs.""",
            "bienetre": """Votre énergie vitale est colossale, mais elle peut être brutale pour votre organisme. Surveillez votre tension et le stress."""
        },
        "v2": {
            "pro": """La maîtrise subtile du pouvoir est votre défi : vous ne cherchez plus à prouver votre force par l'agitation. Votre influence grandit naturellement.""",
            "coeur": """La passion se mue en un pouvoir protecteur au service de votre bonheur commun. Vous bâtissez un destin grandiose avec ceux que vous aimez.""",
            "argent": """La fortune sourit aux audacieux qui savent rester justes. Votre flair pour les investissements rentables est devenu infaillible.""",
            "bienetre": """Votre temple corporel doit suivre le rythme de votre esprit de conquête, ce qui demande une discipline athlétique."""
        },
        "v3": {
            "pro": """Vous atteignez l'Apothéose du Succès : vous êtes au sommet de votre montagne professionnelle. Votre autorité est naturelle.""",
            "coeur": """Un amour impérial couronne votre existence, transformant votre foyer en une dynastie de cœur. La puissance du lien protège les vôtres.""",
            "argent": """La Fortune Souveraine caractérise votre situation : l'argent coule vers vous sans effort car vous êtes un pôle d'attraction.""",
            "bienetre": """Une invulnérabilité physique apparente caractérise votre état de bien-être actuel. Vous avez forgé un temple de résistance."""
        }
    },
    9: {
        "v1": {
            "pro": """L'heure est à l'Achèvement de vos projets et à l'Ouverture sur le monde. Un cycle majeur se termine, vous demandant de clore les dossiers.""",
            "coeur": """L'amour se fait universel et compassionnel, vous poussant à donner un sens plus vaste à vos relations. Lâchez-prise sur le passé.""",
            "argent": """L'abondance vient par des voies détournées ou des opportunités liées à l'étranger. Ne retenez pas les ressources avec avarice.""",
            "bienetre": """Un besoin de purification totale du corps et de l'esprit se fait sentir. Nettoyez votre organisme et libérez votre mental."""
        },
        "v2": {
            "pro": """La boucle est bouclée et vous avez tiré les leçons des expériences passées. Ce mois agit comme une passerelle vers votre futur.""",
            "coeur": """Le pardon absolu libère enfin votre cœur de ses dernières chaînes. Les liens inutiles se dissolvent sans douleur.""",
            "argent": """Le bilan financier est positif si vous avez agi avec humanité. La chance est présente de manière subtile, liée au collectif.""",
            "bienetre": """Une paix inaltérable s'installe dans chaque fibre de votre être. Votre santé sereine ne dépend plus des circonstances extérieures."""
        },
        "v3": {
            "pro": """Vous atteignez l'Inspiration Mondiale : vos projets prennent une dimension altruiste qui touche le plus grand nombre.""",
            "coeur": """L'Amour Inconditionnel est votre réalité, faisant accéder à un état de grâce affective. Votre cœur est un océan de paix.""",
            "argent": """L'Héritage Spirituel et financier se manifeste : vos finances se stabilisent par des retours de fortune liés à votre générosité.""",
            "bienetre": """Une Transmutation Physique totale s'opère, vous faisant vous sentir léger et libéré de la pesanteur. Votre corps est purifié."""
        }
    }
}

# --- GESTION DE LA CONNEXION ---
if 'authentifie' not in st.session_state:
    st.session_state['authentifie'] = False

def check_login(email, code):
    # Identifiants de test - À modifier selon tes besoins
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
    st.sidebar.button("Se déconnecter", on_click=lambda: st.session_state.update({"authentifie": False}))
    st.title("✨ Vos Vibrations Mensuelles")
    
    with st.form("infos"):
        col1, col2 = st.columns(2)
        prenom = col1.text_input("Prénom")
        nom = col1.text_input("Nom")
        date_n = col2.date_input("Date de Naissance", min_value=datetime(1940, 1, 1))
        annee_cible = col2.number_input("Année du rapport", min_value=2024, max_value=2030, value=datetime.now().year)
        submit = st.form_submit_button("Générer mon rapport")

    if submit:
   if submit:
        st.markdown(f"### Rapport pour {prenom} {nom}")
        st.write(INTRO)
        
        # 1. On définit le point de départ : le mois prochain
        maintenant = datetime.now()
        mois_depart = maintenant.month + 1
        annee_depart = maintenant.year
        
        # Si on est en décembre, le mois prochain est janvier de l'année suivante
        if mois_depart > 12:
            mois_depart = 1
            annee_depart += 1

        mois_noms = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
        compteur_vib = {}

        # 2. On boucle 12 fois pour avoir exactement 12 mois glissants
        for i in range(12):
            # Calcul du mois et de l'année en cours de boucle
            m_actuel_idx = (mois_depart - 1 + i) % 12  # Index de 0 à 11
            annee_actuelle = annee_depart + (mois_depart - 1 + i) // 12
            
            # --- CALCUL NUMÉROLOGIQUE ---
            # Année Personnelle = Jour + Mois + Année en cours
            ap = reduire(date_n.day + date_n.month + annee_actuelle)
            # Mois Personnel = Année Personnelle + Mois en cours
            vib_mois = reduire(ap + (m_actuel_idx + 1))
            
            # Gestion des versions v1, v2, v3
            compteur_vib[vib_mois] = compteur_vib.get(vib_mois, 0) + 1
            v_key = f"v{min(compteur_vib[vib_mois], 3)}"
            
            # 3. Affichage de l'onglet
            with st.expander(f"✨ {mois_noms[m_actuel_idx]} {annee_actuelle} | Vibration {vib_mois}"):
                if vib_mois in DATA_TEXTES:
                    txt = DATA_TEXTES[vib_mois][v_key]
                    st.write(f"**💼 Professionnel :** {txt['pro']}")
                    st.write(f"**❤️ Cœur :** {txt['coeur']}")
                    st.write(f"**💰 Argent :** {txt['argent']}")
                    st.write(f"**🌿 Bien-être :** {txt['bienetre']}")
                else:
                    st.error(f"Texte manquant pour la vibration {vib_mois}")
        
        st.info(CONCLUSION)
