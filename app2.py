import streamlit as st
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="Numérologie Pro", page_icon="✨", layout="centered")
# --- DESIGN & ESTHÉTIQUE ---
# --- DESIGN ÉPURÉ & LUMINEUX ---
# --- DESIGN ÉQUILIBRÉ (SÉCURISÉ & LISIBLE) ---
# --- DESIGN COSMIQUE : BLEU NUIT, VIOLET & OR ---
# --- DESIGN BLEU ROYAL & OR ÉTINCELANT ---
# --- DESIGN SAPHIR, AMÉTHYSTE & OR ---
# --- DESIGN NUIT ÉTOILÉE : LISIBILITÉ MAXIMALE ---
# --- DESIGN FINAL : LISIBILITÉ TOTALE & CADRE OR ---
# --- DESIGN FINAL : CONTRASTE ABSOLU ---
# --- DESIGN FINAL : FORCE L'OPACITÉ BLANCHE ---
# --- DESIGN FINAL : LISIBILITÉ TOTALE (TABLEAUX + INTRO/CONCLU) ---
st.markdown("""
    <style>
    /* 1. LE FOND GLOBAL */
    .stApp {
        background: linear-gradient(135deg, #051937 0%, #1a1c4b 100%) !important;
        background-attachment: fixed;
    }

    /* 2. LE TITRE OR */
    h1 {
        color: #D4AF37 !important;
        text-align: center;
        text-transform: uppercase;
        font-weight: bold;
    }

    /* 3. FORCE LE FOND BLANC OPAQUE SUR LE TABLEAU (EXPANDER) */
    div[data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 2px solid #D4AF37 !important;
        border-radius: 10px !important;
        margin-bottom: 15px !important;
    }
    div[data-testid="stExpanderDetails"] {
        background-color: #ffffff !important;
    }

    /* 4. FORCE LE TEXTE EN NOIR PUR DANS L'EXPANDER */
    div[data-testid="stExpander"] p, 
    div[data-testid="stExpander"] span, 
    div[data-testid="stExpander"] h4 {
        color: #000000 !important;
    }

    /* 5. FIX POUR L'INTRO ET LA CONCLUSION (PLUS DE BLEU SUR BLEU) */
    /* On cible les blocs st.info et st.success */
    .stAlert {
        background-color: rgba(255, 255, 255, 0.1) !important; /* Fond très léger pour voir le dégradé derrière */
        border: 1px solid #D4AF37 !important;
        border-radius: 10px !important;
    }
    
    /* On force le texte de l'intro et conclu en BLANC ou OR */
    .stAlert p, .stAlert div {
        color: #ffffff !important; /* Texte Blanc Pur */
        font-size: 1.1rem !important;
        font-style: italic;
    }

    /* 6. STYLE DES TITRES DE RUBRIQUES (PRO, COEUR...) DANS LE TABLEAU */
    h4 {
        color: #1a1c4b !important;
        border-bottom: 2px solid #D4AF37 !important;
        margin-top: 15px !important;
        font-weight: bold !important;
    }

    /* 7. LABELS DU FORMULAIRE (Prénom, Nom...) en OR */
    label {
        color: #D4AF37 !important;
        font-weight: bold !important;
    }

    /* 8. LE BOUTON OR */
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
def reduire(n):
    while n > 9:
        n = sum(int(digit) for digit in str(n))
    return n

INTRO = "Le thème numérologique des 12 mois glissants est une boussole vibratoire qui vous permet d'anticiper les énergies dominantes. Chaque mois possède sa propre fréquence, influençant vos décisions et votre état d'esprit."
CONCLUSION = "Que ces vibrations vous guident vers votre plus bel accomplissement et vous apportent la clarté nécessaire à votre épanouissement."

# --- BASE DE DONNÉES INTÉGRALE (TEXTES LONGS ET QUANTITATIFS) ---
DATA_VIBRATIONS = {
    1: [
        {
            "pro": "L'aube d'un cycle nouveau se lève sur votre Œuvre, marquant le début d'une ère où votre volonté individuelle devient le moteur principal de votre réussite. Cette vibration de primauté vous exhorte à l'initiative pure et à la sortie de votre zone de confort habituelle. Ne soyez point dans l'attente d'une validation extérieure, car l'univers favorise en ce moment les pionniers et ceux qui osent briser les codes établis. C'est le temps de l'affirmation, de l'indépendance et du commandement naturel. Forgez vos projets avec la force de celui qui trace son propre sillage dans une terre encore vierge d'idées.",
            "coeur": "Un souffle de renouveau anime votre sphère affective, invitant à une forme de conquête de soi avant même de chercher la fusion avec l'autre. Cette énergie active peut bousculer les habitudes ronronnantes pour laisser place à une passion plus authentique et plus directe. Pour les âmes liées, c'est un élan de fraîcheur qui demande de redéfinir les bases du couple ; pour les cœurs libres, une rencontre impromptue pourrait naître de votre propre rayonnement et de cette nouvelle assurance que vous dégagez. Ne craignez pas d'exprimer vos désirs les plus profonds avec clarté.",
            "argent": "Les flux de l'abondance répondent favorablement à votre audace et à votre capacité à prendre des risques calculés ce mois-ci. C'est le moment idéal pour semer les graines de la prospérité future par des décisions tranchées et des investissements qui reflètent votre vision à long terme. La stagnation est votre seule ennemie financière ; l'argent doit circuler pour nourrir vos ambitions nouvelles. Investissez en vous-même, dans vos formations ou dans des outils qui augmentent votre autonomie.",
            "bienetre": "Votre vitalité est à son zénith, vous offrant une réserve d'énergie physique et mentale capable de soutenir vos projets les plus lourds. Cependant, cette puissance brute nécessite un exutoire sain pour ne pas se transformer en une tension nerveuse ou en impatience destructrice. Canalisez cette ardeur par une discipline physique régulière, idéalement des exercices qui demandent force et concentration. Préservez la clarté de votre esprit en vous accordant des moments de silence total."
        },
        {
            "pro": "Ce second souffle en vibration 1 vient confirmer vos premières intuitions de leader. L'heure n'est plus à l'hésitation mais à la consolidation de votre position de pionnier. Vous devez maintenant structurer votre élan initial pour qu'il devienne une force durable. Les obstacles qui se dressent ne sont que des tests pour mesurer votre détermination. Affinez votre stratégie, déléguez les tâches secondaires et concentrez votre feu sacré sur l'objectif principal. Votre capacité à décider sans douter sera votre meilleur atout.",
            "coeur": "La dynamique amoureuse exige aujourd'hui que vous preniez une place plus affirmée. Si vous avez tendance à vous effacer, cette vibration vous pousse à exprimer vos besoins avec une honnêteté radicale. Pour les célibataires, votre magnétisme est décuplé par votre confiance en vous ; ne cherchez pas l'amour, laissez-le être attiré par votre force intérieure. En couple, c'est le moment de proposer de nouveaux projets, de voyager ou de changer de cadre de vie pour insuffler une énergie de conquête partagée.",
            "argent": "L'expansion financière se poursuit, mais elle demande désormais une gestion plus stratégique de vos ressources. Ne vous contentez pas de gagner, cherchez à optimiser. C'est une période faste pour renégocier des contrats ou pour lancer une activité secondaire basée sur un talent personnel. Votre intuition financière est aiguisée : écoutez ce petit instinct qui vous dit quand foncer. L'argent est ici un outil de liberté ; utilisez-le pour briser les derniers verrous qui entravent votre autonomie matérielle.",
            "bienetre": "Le dynamisme reste fort, mais il doit s'accompagner d'une meilleure gestion de votre sommeil et de vos rythmes biologiques. Vous avez tendance à vouloir tout faire en même temps, ce qui peut créer une fatigue invisible. Apprenez l'art de la déconnexion technologique pour reposer votre système nerveux. Un retour à des activités manuelles ou à la nature sera salvateur. Votre corps est votre véhicule de réussite ; traitez-le avec la rigueur d'un athlète de haut niveau."
        }
    ],
    2: [
        {
            "pro": "L'heure est à l'Alliance stratégique et à l'exercice subtil de la diplomatie. La force brutale et les décisions solitaires doivent céder le pas à la finesse du discernement et à l'écoute active des besoins de vos partenaires. Vos succès ce mois-ci naîtront de votre capacité unique à unir les contraires et à percevoir les opportunités cachées dans les murmures entre les mots. Cultivez la patience de l'agriculteur, car les fruits les plus savoureux mûrissent toujours dans l'ombre des collaborations fertiles.",
            "coeur": "Une vibration de douceur et de réceptivité enveloppe vos échanges affectifs. Les liens les plus forts se tissent désormais dans la confidence, le partage des silences et une écoute profonde des émotions de l'autre. C'est un temps idéal pour l'harmonie, le pardon sincère et la fusion des âmes qui cherchent un port paisible. Laissez votre intuition guider vos pas vers ceux qui résonnent véritablement avec la fréquence de votre cœur, sans chercher à forcer le destin. La tendresse est votre meilleure alliée.",
            "argent": "La prospérité ce mois-ci dépend étroitement de votre équilibre intérieur et de votre capacité à collaborer. Évitez les mouvements financiers brusques, les investissements impulsifs ou les spéculations solitaires qui pourraient déstabiliser vos acquis. Les gains les plus solides se trouvent dans les associations réfléchies, les contrats de confiance et la gestion sage des ressources partagées. C'est un moment favorable pour conclure des accords basés sur le bénéfice mutuel. L'argent est ici le résultat d'une entente.",
            "bienetre": "Votre sensibilité est actuellement votre boussole la plus précieuse, mais elle vous rend également très perméable aux ambiances et aux énergies environnantes. Protégez votre paix intérieure comme un trésor rare, recherchez la proximité purificatrice de l'eau et écoutez les besoins changeants de votre corps avec une bienveillance maternelle. Évitez les lieux bruyants ou les personnalités toxiques qui pourraient drainer votre vitalité. Des activités comme le yoga vous permettront de maintenir cet équilibre."
        },
        {
            "pro": "La collaboration s'approfondit et demande une écoute plus nuancée. Il ne s'agit plus seulement de s'accorder en surface, mais de comprendre les non-dits de vos associés pour anticiper les tensions futures. Votre force réside dans votre capacité à être le liant indispensable d'un projet commun. Soyez le médiateur discret mais efficace qui fluidifie les rouages complexes de votre environnement professionnel. C'est par la souplesse et non par la force que vous obtiendrez les meilleurs compromis.",
            "coeur": "L'amour demande aujourd'hui une attention particulière aux détails émotionnels et aux petits gestes de soutien. On dépasse le simple accord pour toucher à une compréhension instinctive de l'autre. C'est un temps de pacification où les anciens conflits s'effacent devant une volonté commune de sérénité. Pour les célibataires, une rencontre basée sur une complicité intellectuelle et spirituelle profonde est favorisée par cette vibration de douceur. L'amour est une danse à deux, harmonieuse.",
            "argent": "Un accord financier passé pourrait être réévalué à votre avantage grâce à votre tact et votre sens de la négociation. C'est le moment de stabiliser vos acquis plutôt que de chercher l'expansion agressive. La richesse vient ici de la fidélité à vos engagements et de la qualité de votre réseau relationnel. Soyez attentif aux clauses des contrats et aux conseils avisés de vos partenaires de confiance. La précision administrative est votre alliée ce mois-ci.",
            "bienetre": "Votre système nerveux est sollicité par votre empathie naturelle, ce qui demande des moments de retrait total pour vous recentrer. Le repos n'est pas un luxe, c'est une nécessité absolue de régénération. Privilégiez une alimentation équilibrée et des soins doux comme l'aromathérapie ou la réflexologie. Votre santé physique est le reflet exact de votre climat émotionnel ; traitez vos peurs avec douceur pour laisser votre vitalité s'exprimer pleinement."
        }
    ],
    3: [
        {
            "pro": "L'éclat de la création illumine votre chemin professionnel, transformant chaque défi en une opportunité de briller par votre ingéniosité. Votre parole devient une force de persuasion redoutable et vos idées originales agissent comme des phares dans la nuit pour vos collaborateurs. C'est le mois idéal pour l'expression de vos talents, pour les contacts féconds et pour un rayonnement social sans précédent. Osez paraître sur le devant de la scène et partager vos visions les plus audacieuses, car le monde est enfin prêt à les recevoir.",
            "coeur": "La joie de vivre et une légèreté bienvenue s'invitent à votre table, dissipant les nuages de la mélancolie ou du sérieux excessif. Les échanges affectifs sont teintés d'un humour complice et d'une séduction naturelle qui attirent à vous les regards et les attentions. C'est une période faste pour les nouvelles rencontres, les célébrations entre amis et l'épanouissement des plaisirs sensoriels de l'existence. Laissez votre cœur s'exprimer avec spontanéité, sans peur du jugement ou du qu'en-dira-t-on.",
            "argent": "Une chance subtile mais réelle accompagne vos finances ce mois-ci, souvent déclenchée par votre réseau relationnel ou votre créativité débordante. La fluidité monétaire est favorisée par votre capacité à communiquer sur vos projets et à susciter l'intérêt de nouveaux partenaires. L'abondance peut venir par des voies inattendues, souvent liées à votre charisme ou à un talent que vous aviez jusqu'ici sous-estimé. N'ayez pas peur de mettre en avant vos services ou vos produits ; votre enthousiasme est contagieux.",
            "bienetre": "Votre moral est actuellement votre meilleur remède, agissant comme un bouclier naturel contre la fatigue et le stress. Cultivez l'enthousiasme, entourez-vous de personnes positives et stimulez votre esprit par des activités créatives ou artistiques. Veillez toutefois à ne point disperser votre précieuse essence vitale dans des futilités ou une agitation sociale excessive. Un sommeil régulier et de qualité soutiendra votre pétillance naturelle et préservera l'éclat de votre peau."
        },
        {
            "pro": "Votre communication professionnelle franchit une nouvelle étape de clarté et d'impact. On vient vers vous pour votre capacité à simplifier les concepts complexes et à motiver les troupes avec brio. Votre rayonnement attire des propositions stimulantes qui demandent une réponse rapide et enthousiaste. C'est le moment de peaufiner votre image de marque et de faire valoir vos succès passés avec une assurance élégante. Le succès sourit à ceux qui savent raconter une histoire inspirante autour de leur travail.",
            "coeur": "La complicité intellectuelle est au cœur de vos relations ce mois-ci. Vous avez besoin de partager des rires, des idées et des découvertes avec ceux que vous aimez. La communication est fluide et permet de lever les derniers tabous ou malentendus. Pour les cœurs solitaires, une amitié pourrait évoluer vers quelque chose de plus tendre grâce à un dialogue particulièrement inspiré et sincère. L'amour est une fête de l'esprit avant d'être une affaire de cœur.",
            "argent": "Les opportunités de gains sont liées à vos talents d'expression ou à des projets de groupe particulièrement dynamiques. C'est un mois favorable pour investir dans des domaines liés aux loisirs, aux médias ou à l'art de vivre. Votre flair vous pousse vers des dépenses liées au plaisir et à la sociabilité ; veillez simplement à garder un équilibre raisonnable pour ne pas compromettre vos projets à long terme. L'argent doit servir à embellir votre vie et celle de vos proches.",
            "bienetre": "Vous débordez d'énergie créatrice, ce qui stimule naturellement votre système immunitaire et votre joie de vivre. Pour garder cet élan, évitez les personnalités moroses ou les environnements ternes qui pompent votre vitalité. Le chant, la danse ou toute forme d'expression corporelle sera une thérapie puissante pour évacuer les micro-tensions accumulées. Votre corps exprime votre état de joie ; maintenez cette fréquence par des plaisirs simples et réguliers."
        }
    ],
    4: [
        {
            "pro": "L'heure est à l'Édification patiente et rigoureuse de vos ambitions les plus chères. Les rênes du destin demandent en ce moment une main ferme, une discipline de fer et un sens aigu de l'organisation pratique. C'est le temps de la structure, de l'ordre intérieur et du labeur patient qui ne cherche point la lumière immédiate. Construisez brique après brique, sans jamais chercher le raccourci facile, car seules les fondations que vous coulez aujourd'hui résisteront aux tempêtes futures. Votre fiabilité devient votre plus grand atout professionnel.",
            "coeur": "La sécurité émotionnelle et la loyauté indéfectible sont les piliers centraux de ce mois de construction affective. On ne cherche point l'aventure éphémère ou les passions dévastatrices, mais l'ancrage durable dans la réalité du quotidien partagé. C'est le moment idéal pour prouver votre attachement sincère par des actes concrets, une présence rassurante et une écoute qui ne faiblit jamais. Pour les couples, c'est le temps des projets immobiliers ou familiaux solides ; l'amour se prouve ici par la durée et la stabilité.",
            "argent": "La prospérité ce mois-ci ne doit rien au hasard, elle naît directement de votre rigueur et de votre sens de l'économie. Établissez vos comptes avec une précision chirurgicale, prévoyez l'imprévisible et investissez prioritairement dans le durable et le concret. La terre, l'immobilier ou les valeurs refuges sont des alliées sûres sous cette vibration de stabilité retrouvée. Évitez toute forme de spéculation hasardeuse qui pourrait compromettre vos efforts passés. Votre richesse se bâtit sur la prudence.",
            "bienetre": "Votre corps demande aujourd'hui du respect, de la régularité et une structure claire dans votre hygiène de vie. Honorez votre temple physique par une discipline sans faille, en privilégiant une alimentation saine et des horaires de repos fixes. Surveillez particulièrement vos articulations, votre dos et votre ossature ; ne portez point de charges trop lourdes, qu'elles soient réelles ou symboliques. Des exercices de renforcement musculaire ou de la marche régulière en terrain stable vous feront du bien."
        },
        {
            "pro": "La persévérance méthodique porte enfin ses fruits et vous commencez à voir les résultats tangibles de votre organisation sans faille. Votre fiabilité est remarquée par vos supérieurs ou vos pairs, vous positionnant comme une référence de stabilité dans un monde en mouvement. Ne relâchez pas l'effort de méthode, car c'est dans la répétition des bonnes pratiques que vous sécurisez votre avenir professionnel. Un dossier complexe ou une situation administrative délicate pourrait trouver sa résolution définitive.",
            "coeur": "L'amour se stabilise dans une routine rassurante qui permet d'approfondir la confiance mutuelle au-delà des mots. C'est en honorant vos promesses et en étant présent dans les moments ordinaires que vous renforcez vos liens les plus précieux. Pour les célibataires, la patience est de mise : ne précipitez rien, laissez le temps faire le tri entre l'éphémère et le solide. La loyauté devient votre critère de sélection numéro un, car vous aspirez à une union qui a du sens et du poids.",
            "argent": "Un investissement à long terme commence à montrer des signes de rentabilité rassurants. Continuez à épargner avec la même constance, car votre sécurité financière future dépend directement de votre autodiscipline actuelle. C'est un mois idéal pour régulariser des situations administratives, des assurances ou des dossiers bancaires restés en suspens. La rigueur dans vos paiements et vos factures vous apportera une tranquillité d'esprit inestimable pour aborder les cycles suivants.",
            "bienetre": "Le besoin d'ancrage est fort ce mois-ci. Travaillez votre respiration ventrale et votre contact physique avec la nature ou la matière. Des massages profonds ou des soins ostéopathiques pourraient vous aider à libérer les tensions accumulées dans votre structure dorsale. Votre endurance est excellente, mais elle nécessite un entretien régulier pour ne pas s'user prématurément. La santé est ici une question de prévention, de régularité et de respect des limites naturelles.",
        }
    ],
    5: [
        {
            "pro": "Un vent puissant de Mutation souffle sur votre vie professionnelle, balayant les certitudes pour laisser place à l'imprévu créateur. Les chaînes de la routine et de la stagnation se brisent enfin pour vous offrir l'aventure, les voyages ou de nouvelles méthodes de travail révolutionnaires. Soyez tel le voyageur prêt à saisir chaque opportunité au vol, car le mouvement perpétuel est en ce moment votre seule constante bénéfique. Votre capacité d'adaptation et votre agilité mentale seront vos plus grandes forces.",
            "coeur": "L'énergie du désir, de la curiosité et de la liberté individuelle s'intensifie brusquement dans votre sphère sentimentale. C'est un temps idéal pour explorer de nouveaux horizons affectifs, pour rompre avec la monotonie des habitudes et pour redécouvrir avec émerveillement le plaisir de l'imprévu à deux. Laissez-vous surprendre par l'inconnu, osez des expériences qui sortent de votre cadre habituel et libérez-vous des carcans qui étouffaient votre spontanéité. L'amour est une exploration.",
            "argent": "Les flux financiers sont rapides, vifs et parfois instables, demandant une attention de chaque instant et une grande souplesse de réaction. L'argent circule avec une vélocité étonnante ce mois-ci ; il peut entrer en abondance par des voies nouvelles mais peut aussi repartir rapidement pour financer vos soifs de liberté ou de changement. Gardez une main agile sur la bourse tout en restant ouvert aux opportunités d'investissement audacieuses dans les nouvelles technologies.",
            "bienetre": "Une vitalité bouillonnante et une soif d'expérience vous animent, vous poussant à explorer vos limites physiques et mentales. Vous avez un besoin impérieux d'air, d'espace, de nouveauté et de stimuli sensoriels variés pour vous sentir pleinement vivant. Prenez garde toutefois aux excès de toutes sortes et à l'impulsivité qui pourraient fragiliser votre équilibre nerveux à la longue. La respiration profonde et les sports de plein air seront vos meilleurs alliés pour canaliser cette énergie."
        },
        {
            "pro": "Cette phase de changement professionnel demande une grande vivacité d'esprit et une capacité à pivoter rapidement. Vous pourriez être sollicité pour des projets transversaux ou des déplacements imprévus qui enrichiront considérablement votre carnet d'adresses. Ne craignez pas l'instabilité passagère, elle est le signe que vous êtes en train de franchir une étape de croissance majeure. Votre curiosité est votre moteur, laissez-la vous guider vers des domaines encore inexplorés.",
            "coeur": "La communication est le moteur de votre vie sentimentale ce mois-ci. Vous avez besoin d'échanges vifs, de débats passionnés et d'une forme de liberté qui ne vous étouffe pas. C'est un temps de rencontres variées pour les célibataires et de renouveau du dialogue pour les couples. N'ayez pas peur d'exprimer votre besoin d'indépendance ; s'il est bien formulé, il ne fera que renforcer la qualité de votre lien en y apportant une dimension de respect mutuel et de fraîcheur.",
            "argent": "L'argent est pour vous un moyen d'expérimentation ce mois-ci. Vous pourriez être tenté par des achats impulsifs liés à la technologie ou au voyage. Si votre budget le permet, accordez-vous ces plaisirs, mais gardez un œil sur la tendance générale pour ne pas finir le mois dans le flou. Des opportunités de gains rapides peuvent se présenter via des contacts informels ou des idées de génie nées d'une discussion impromptue. Soyez réactif et restez mobile.",
            "bienetre": "Votre système nerveux est électrique et demande une alternance entre action intense et relaxation profonde. Pour éviter le surmenage intellectuel, accordez-vous des pauses régulières loin des écrans. Le voyage, même court, agit sur vous comme une véritable thérapie de régénération mentale. Changez de décor, changez de routine, et laissez votre corps s'adapter à de nouveaux environnements. La souplesse, tant physique que mentale, est le gage de votre santé.",
        }
    ],
    6: [
        {
            "pro": "L'Harmonie relationnelle et le sens de la Responsabilité partagée sont vos maîtres-mots absolus pour ce mois de construction collective. On attend de vous la justesse d'un juge, la patience d'un diplomate et la bienveillance inspirante d'un mentor pour votre équipe ou vos collaborateurs. C'est le moment idéal pour embellir concrètement votre cadre de travail, apaiser les tensions latentes et assumer pleinement votre rôle de pilier au sein de votre communauté professionnelle. Votre succès est collectif.",
            "coeur": "Le foyer est désormais votre véritable sanctuaire et l'amour la boussole qui oriente chacun de vos choix de vie importants. Cette vibration chaleureuse favorise l'engagement profond, la création d'un cocon protecteur et le soin méticuleux porté aux êtres qui vous sont chers. C'est un temps idéal pour le mariage, l'agrandissement de la famille, une installation commune ou une réconciliation durable. Laissez votre cœur s'exprimer à travers la tendresse et le dévouement.",
            "argent": "L'équilibre financier se trouve ce mois-ci dans la gestion judicieuse des besoins familiaux et dans l'investissement porté sur votre confort personnel et celui des vôtres. Vos décisions monétaires doivent viser avant tout l'amélioration de la qualité de vie et l'embellissement de votre habitat. La générosité équilibrée attire paradoxalement à son tour l'abondance dans votre sphère de vie. C'est un temps favorable pour les investissements immobiliers familiaux ou les assurances.",
            "bienetre": "Le corps et l'esprit réclament aujourd'hui une dose massive de beauté, de douceur et d'harmonie sensorielle pour fonctionner au mieux. Entourez-vous de couleurs apaisantes, écoutez des musiques qui élèvent votre âme et prenez soin de votre équilibre hormonal par des méthodes naturelles. La paix émotionnelle est le gage absolu de votre santé physique ce mois-ci ; évitez les conflits qui drainent votre énergie vitale. Soyez doux avec vous-même, comme vous l'êtes avec les autres."
        },
        {
            "pro": "Votre rôle de stabilisateur professionnel s'accentue. Vous êtes celui vers qui l'on se tourne pour obtenir un avis juste ou pour résoudre un conflit délicat entre collègues. Cette responsabilité, bien qu'exigeante, assoit votre autorité morale au sein de l'entreprise. Prenez soin de ne pas vous laisser envahir par les problèmes des autres au détriment de vos propres tâches, mais continuez à cultiver cet esprit d'entraide qui fait votre force et votre réputation d'excellence.",
            "coeur": "L'harmonie familiale demande un investissement conscient de votre temps et de votre énergie. C'est une période idéale pour organiser des moments de retrouvailles, pour embellir votre décoration intérieure ou pour prendre soin de parents ou d'enfants. Votre besoin d'être utile à ceux que vous aimez est comblé par des retours de gratitude touchants. En couple, l'engagement se renforce par des projets concrets qui sécurisent votre avenir commun. La fidélité est votre socle.",
            "argent": "La gestion de votre budget est axée sur la prévoyance et le bien-être domestique. Vous pourriez décider d'engager des dépenses pour améliorer votre cadre de vie ou pour soutenir un projet lié à un membre de la famille. Ces investissements sont bénéfiques car ils renforcent votre sentiment de sécurité et de confort. Veillez cependant à ne pas trop porter le fardeau financier des autres ; l'équilibre réside dans le partage équitable des responsabilités au sein du groupe.",
            "bienetre": "Votre santé est étroitement liée à votre environnement immédiat. Un cadre de vie propre, ordonné et esthétique est indispensable à votre équilibre psychique. Prenez soin de votre peau, de votre alimentation et accordez-vous des bains relaxants ou des soins de beauté qui renforcent votre estime de soi. La pratique du jardinage ou de l'art floral peut être une excellente thérapie pour canaliser votre besoin de créer de la beauté. Cultivez votre jardin intérieur avec amour.",
        }
    ],
    7: [
        {
            "pro": "Le temps semble s'arrêter ce mois-ci pour laisser place à la Connaissance profonde et à la réflexion stratégique de haut vol. Détachez-vous de l'agitation superficielle du monde professionnel pour parfaire vos savoirs et affiner votre vision à long terme. La victoire appartient à celui qui sait voir ce que les autres ignorent par manque de recul. Votre esprit est votre arme la plus tranchante ce mois-ci ; utilisez-le pour analyser, comprendre et planifier vos prochains mouvements avec une précision chirurgicale.",
            "coeur": "Une certaine distance émotionnelle ou physique est temporairement nécessaire pour mieux comprendre la véritable nature de vos sentiments les plus profonds. C'est un temps de solitude choisie et féconde, ou de partage intellectuel intense avec un partenaire capable de comprendre vos silences. Le silence est le terreau sacré où germent actuellement les unions les plus solides. L'amour est ici un mystère sacré qui demande de la patience et une grande honnêteté intellectuelle envers soi-même.",
            "argent": "La gestion de l'argent demande ce mois-ci une grande retenue et une analyse froide des opportunités. Observez les marchés, étudiez les chiffres, mais ne vous hâtez point de conclure des transactions sous l'influence de l'émotion ou de la pression extérieure. Un secret financier ou une information confidentielle pourrait être révélée à votre avantage si vous restez attentif et discret. La richesse vient ici de l'esprit et de la prudence. Évitez les dépenses impulsives ou de prestige.",
            "bienetre": "Le repos de l'esprit et la protection de votre système nerveux sont vos priorités absolues sous cette vibration de sagesse. Méditez, lisez, et n'hésitez point à vous retirer du tumulte social dès que vous en ressentez le besoin impérieux. Votre mental est sollicité par vos réflexions intenses ; accordez-lui le calme et le sommeil profond qu'il réclame pour se régénérer. La proximité de la nature sauvage, des forêts ou des lieux de recueillement sera votre meilleure source de vitalité.",
        },
        {
            "pro": "Votre expertise est sollicitée sur des points techniques ou stratégiques pointus. C'est une période de perfectionnement où vous pourriez envisager une formation de haut niveau ou une recherche approfondie sur un sujet qui vous passionne. Votre crédibilité professionnelle augmente à mesure que vous démontrez votre maîtrise et votre recul sur les événements. Ne cherchez pas à briller par l'agitation, mais par la pertinence de vos analyses froides et documentées. Le savoir est votre pouvoir.",
            "coeur": "La qualité de la relation prime sur la quantité de moments passés ensemble. Vous aspirez à des échanges qui ont du sens, à des discussions philosophiques ou à une quête spirituelle partagée. C'est un mois de grande lucidité sur vos besoins affectifs réels. Si vous êtes seul, cette période de célibat est vécue comme une opportunité de croissance personnelle majeure. En couple, c'est le moment de se retrouver sur l'essentiel, loin des bruits du monde, pour sceller une complicité d'âme.",
            "argent": "La prudence financière se transforme en une stratégie d'investissement réfléchie. Vous pourriez découvrir des opportunités cachées dans des domaines liés à la recherche, à l'enseignement ou aux technologies de pointe. C'est un mois pour apprendre à gérer vos avoirs de manière plus autonome et moins dépendante des fluctuations extérieures. Prenez le temps de lire les petits caractères des contrats bancaires ; votre vigilance vous évitera des frais inutiles ou des erreurs administratives.",
            "bienetre": "Le besoin de calme et de solitude devient une nécessité physiologique pour votre équilibre. Accordez-vous des cures de silence ou des retraites spirituelles si possible. Votre corps a besoin de se décharger des tensions électromagnétiques et du stress urbain. La pratique de la méditation de pleine conscience ou du yoga nidra vous aidera à réguler votre sommeil et à apaiser votre mental bouillonnant. Écoutez votre intuition, elle est particulièrement affûtée ce mois-ci pour vous guider vers la guérison.",
        }
    ],
    8: [
        {
            "pro": "La Puissance et l'Accomplissement concret se manifestent avec une force irrésistible ce mois-ci. C'est le mois de la récolte : vous obtenez enfin ce que vous avez semé avec tant d'effort. Affirmez votre ambition, tranchez les nœuds gordiens et assumez pleinement votre autorité naturelle. Le succès matériel vous tend les bras si vous agissez avec une intégrité absolue et un sens aigu de la justice. Vous êtes le chef d'orchestre de votre réussite, ne craignez pas de diriger avec fermeté.",
            "coeur": "Les sentiments sont vécus avec une intensité volcanique, mêlant passion, magnétisme et désir de contrôle. C'est un temps idéal pour vivre des émotions fortes et pour utiliser votre charisme naturel afin de séduire ou de reconquérir. Veillez toutefois à ce que cette puissance ne devienne pas un besoin de domination étouffant pour l'autre. L'amour est ici une force de transformation puissante qui demande à être canalisée par le respect mutuel et une volonté de bâtir un empire affectif solide.",
            "argent": "Les flux financiers sont à leur paroxysme, offrant des opportunités de gains massifs ou de restructurations d'envergure. C'est le moment idéal pour négocier des contrats importants, pour investir de manière offensive ou pour régulariser des dettes anciennes. L'argent est pour vous une énergie de puissance que vous devez apprendre à maîtriser sans peur mais avec discernement. Votre flair pour les affaires est à son comble, vous permettant de débusquer la rentabilité là où d'autres échouent.",
            "bienetre": "Votre énergie vitale est colossale, mais elle peut s'avérer brutale pour votre organisme si elle n'est pas canalisée. Surveillez votre tension artérielle et le stress lié à la quête incessante de réussite. Apprenez à relâcher chaque muscle après l'effort et accordez-vous des plages de décompression totale. La pratique d'un sport intense ou de compétition vous aidera à évacuer le trop-plein d'adrénaline et à maintenir votre corps dans un état de performance optimale et saine.",
        },
        {
            "pro": "L'heure est à la gestion de votre pouvoir et à l'exercice de votre influence. Vous êtes en position de force pour imposer vos conditions ou pour obtenir une promotion méritée. C'est un mois où votre sens de la stratégie matérielle fait merveille. Veillez cependant à rester juste dans vos rapports de force ; la vraie puissance ne se prouve pas par l'écrasement, mais par la capacité à emmener les autres vers un succès commun. Votre leadership est scruté, soyez un modèle de détermination intègre.",
            "coeur": "La passion se transforme en une volonté de construire quelque chose de durable et d'imposant à deux. C'est le moment des engagements sérieux qui impliquent une dimension matérielle ou sociale (mariage, achat commun, projets de carrière croisés). Vous avez besoin d'un partenaire qui soit à la hauteur de vos ambitions et qui partage votre soif de réussite. La sensualité est puissante et agit comme un ciment qui renforce votre complicité dans les moments de lutte extérieure. Soyez généreux dans votre force.",
            "argent": "Une rentrée d'argent significative ou un retour sur investissement vient valider vos choix passés. C'est un mois faste pour les transactions immobilières, les héritages ou les litiges financiers qui trouvent enfin une issue favorable. Gérez cette abondance avec la sagesse d'un empereur : réinvestissez une part dans votre croissance future et utilisez le reste pour asseoir votre sécurité. L'argent appelle l'argent, à condition d'être géré avec une main de fer dans un gant de velours.",
            "bienetre": "Votre résistance physique est exceptionnelle, vous permettant de faire face à des charges de travail importantes sans faiblir. Cependant, veillez à ne pas ignorer les signaux d'alerte de votre corps par simple orgueil de force. Le foie et le système digestif peuvent être sollicités par les excès liés à votre rythme de vie intense. Une cure de détox ou un régime alimentaire plus sobre vous aidera à maintenir votre clarté mentale et votre puissance physique. La maîtrise de soi est la clé de votre santé.",
        }
    ],
    9: [
        {
            "pro": "L'heure est à l'Achèvement de vos projets et à l'Ouverture sur de vastes horizons mondiaux. Un cycle majeur de neuf ans ou de neuf mois se termine, vous demandant de clore les dossiers en suspens et de faire un bilan honnête de vos succès et échecs. Votre rayonnement dépasse désormais vos frontières habituelles pour toucher un public plus large. C'est le temps de la transmission, de l'enseignement et de la préparation à une renaissance prochaine. La fin d'une étape est la promesse d'une ascension.",
            "coeur": "L'amour se fait universel et compassionnel, vous poussant à donner un sens plus vaste à vos relations personnelles. C'est un mois idéal pour les grands voyages intérieurs, les réconciliations ultimes et un lâcher-prise salutaire sur les blessures du passé. Laissez votre cœur s'ouvrir à l'inconnu et à l'altruisme ; c'est dans le don désintéressé que vous trouverez votre plus grande satisfaction émotionnelle. Une page se tourne pour laisser place à une dimension plus spirituelle de l'union.",
            "argent": "L'abondance vient par des voies détournées, des récompenses pour vos efforts passés ou des opportunités liées à l'étranger et à l'humanitaire. Ne retenez pas les ressources avec avarice ; laissez-les circuler, car c'est ainsi que vous purifiez votre karma financier. C'est un temps pour régler vos derniers comptes matériels, solder vos dettes et préparer le terrain vierge du prochain cycle qui commence. L'argent est ici une récompense pour votre intégrité passée et non un but en soi.",
            "bienetre": "Un besoin de purification totale du corps et de l'esprit se fait sentir de manière impérieuse. Nettoyez votre organisme par une alimentation légère et libérez votre mental des rancœurs ou des attachements inutiles. L'écoute de votre intuition et de vos rêves vous apportera les clés de votre régénération future. Votre santé dépend de votre capacité à lâcher ce qui est mort pour laisser la place au flux de la vie nouvelle. Accordez-vous du temps pour la rêverie et la méditation.",
        },
        {
            "pro": "Vous êtes dans une phase de transition où vous préparez déjà mentalement le terrain pour vos futures aventures. C'est le moment idéal pour déléguer vos responsabilités actuelles, pour former vos successeurs et pour clore avec élégance vos engagements en cours. Votre expérience est votre plus grand trésor ; n'hésitez pas à la partager généreusement. Vous recevez la reconnaissance pour l'ensemble de votre œuvre, ce qui vous donne la force de vous projeter vers de nouveaux sommets encore plus élevés.",
            "coeur": "Une grande lucidité s'installe dans votre vie amoureuse. Vous comprenez enfin le sens des épreuves passées et vous vous sentez prêt à vivre une relation basée sur une liberté totale et une confiance absolue. C'est un mois de bilan affectif où vous décidez de ne garder que l'essentiel. Pour les célibataires, une rencontre avec une personne d'une culture différente ou ayant un vécu riche pourrait transformer votre vision du couple. L'amour est ici un voyage sans fin vers l'autre et vers soi-même.",
            "argent": "Les finances passent au second plan derrière vos aspirations spirituelles ou idéologiques. Pourtant, c'est souvent à ce moment que les ressources arrivent le plus facilement, comme par magie. Utilisez cet argent pour des causes qui vous tiennent à cœur ou pour financer des projets de voyage et d'étude. La générosité est votre meilleure stratégie financière ce mois-ci ; plus vous donnez avec le cœur, plus l'univers semble s'empresser de combler vos besoins. Préparez-vous à une nouvelle ère d'abondance.",
            "bienetre": "Votre corps exprime un besoin de légèreté et de fluidité. Privilégiez les activités comme la natation, le yoga ou la danse libre. L'air pur et les grands espaces sont indispensables pour recharger vos batteries après un long cycle d'efforts. Vous êtes en train de muer, au sens propre comme au sens figuré ; soyez bienveillant avec votre fatigue passagère, elle est le signe de cette transformation interne profonde. La sérénité est à portée de main si vous acceptez de laisser partir l'ancien.",
        }
    ]
}

# --- AUTHENTIFICATION ---
if 'auth' not in st.session_state: st.session_state['auth'] = False
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
    # --- FORMULAIRE ---
    st.title("✨ Vos 12 Prochains Mois")
    with st.form("numerologie"):
        c1, c2 = st.columns(2)
        prenom = c1.text_input("Prénom")
        nom = c1.text_input("Nom de famille")
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
        historique_vibrations = {}

        for i in range(12):
            idx_m = (m_start - 1 + i) % 12
            an_m = a_start + (m_start - 1 + i) // 12
            ap = reduire(dnais.day + dnais.month + an_m)
            vib = reduire(ap + (idx_m + 1))
            
            # Anti-redondance (Vibration A/B)
            if vib not in historique_vibrations:
                historique_vibrations[vib] = 0
                variante = 0
            else:
                historique_vibrations[vib] += 1
                variante = historique_vibrations[vib] % 2
            
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
