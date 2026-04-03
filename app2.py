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

# --- TEXTES FIXES (NE PAS CHANGER) ---
INTRO = "Le thème numérologique des 12 mois glissants est une boussole vibratoire qui vous permet d'anticiper les énergies dominantes. Chaque mois possède sa propre fréquence, influençant vos décisions et votre état d'esprit."
CONCLUSION = "Que ces vibrations vous guident vers votre plus bel accomplissement et vous apportent la clarté nécessaire à votre épanouissement."

# --- BASE DE DONNÉES : TEXTES LONGS (QUANTITATIF) ---
DATA_TEXTES = {
    1: {
        "pro": "L'aube d'un cycle nouveau se lève sur votre Œuvre, marquant le début d'une ère où votre volonté individuelle devient le moteur principal de votre réussite. Cette vibration de primauté vous exhorte à l'initiative pure et à la sortie de votre zone de confort habituelle. Ne soyez point dans l'attente d'une validation extérieure, car l'univers favorise en ce moment les pionniers et ceux qui osent briser les codes établis. C'est le temps de l'affirmation, de l'indépendance et du commandement naturel. Forgez vos projets avec la force de celui qui trace son propre sillage dans une terre encore vierge d'idées.",
        "coeur": "Un souffle de renouveau anime votre sphère affective, invitant à une forme de conquête de soi avant même de chercher la fusion avec l'autre. Cette énergie active peut bousculer les habitudes ronronnantes pour laisser place à une passion plus authentique et plus directe. Pour les âmes liées, c'est un élan de fraîcheur qui demande de redéfinir les bases du couple ; pour les cœurs libres, une rencontre impromptue pourrait naître de votre propre rayonnement et de cette nouvelle assurance que vous dégagez. Ne craignez pas d'exprimer vos désirs les plus profonds avec clarté.",
        "argent": "Les flux de l'abondance répondent favorablement à votre audace et à votre capacité à prendre des risques calculés ce mois-ci. C'est le moment idéal pour semer les graines de la prospérité future par des décisions tranchées et des investissements qui reflètent votre vision à long terme. La stagnation est votre seule ennemie financière ; l'argent doit circuler pour nourrir vos ambitions nouvelles. Investissez en vous-même, dans vos formations ou dans des outils qui augmentent votre autonomie, car votre capacité de gain est directement liée à votre leadership personnel.",
        "bienetre": "Votre vitalité est à son zénith, vous offrant une réserve d'énergie physique et mentale capable de soutenir vos projets les plus lourds. Cependant, cette puissance brute nécessite un exutoire sain pour ne pas se transformer en une tension nerveuse ou en impatience destructrice. Canalisez cette ardeur par une discipline physique régulière, idéalement des exercices qui demandent force et concentration. Préservez la clarté de votre esprit en vous accordant des moments de silence total, afin que le feu intérieur reste une lumière et non un incendie incontrôlable."
    },
    2: {
        "pro": "L'heure est à l'Alliance stratégique et à l'exercice subtil de la diplomatie. La force brutale et les décisions solitaires doivent céder le pas à la finesse du discernement et à l'écoute active des besoins de vos partenaires. Vos succès ce mois-ci naîtront de votre capacité unique à unir les contraires et à percevoir les opportunités cachées dans les murmures entre les mots. Cultivez la patience de l'agriculteur, car les fruits les plus savoureux mûrissent toujours dans l'ombre des collaborations fertiles. Votre rôle est celui du médiateur, de celui qui fluidifie les échanges pour le bien commun.",
        "coeur": "Une vibration de douceur et de réceptivité enveloppe vos échanges affectifs. Les liens les plus forts se tissent désormais dans la confidence, le partage des silences et une écoute profonde des émotions de l'autre. C'est un temps idéal pour l'harmonie, le pardon sincère et la fusion des âmes qui cherchent un port paisible. Laissez votre intuition guider vos pas vers ceux qui résonnent véritablement avec la fréquence de votre cœur, sans chercher à forcer le destin. La tendresse est votre meilleure alliée pour ouvrir les portes qui semblaient closes ; laissez la vulnérabilité devenir votre force.",
        "argent": "La prospérité ce mois-ci dépend étroitement de votre équilibre intérieur et de votre capacité à collaborer. Évitez les mouvements financiers brusques, les investissements impulsifs ou les spéculations solitaires qui pourraient déstabiliser vos acquis. Les gains les plus solides se trouvent dans les associations réfléchies, les contrats de confiance et la gestion sage des ressources partagées. C'est un moment favorable pour demander conseil à des experts ou pour conclure des accords basés sur le bénéfice mutuel. L'argent est ici le résultat d'une entente harmonieuse avec le flux de la vie.",
        "bienetre": "Votre sensibilité est actuellement votre boussole la plus précieuse, mais elle vous rend également très perméable aux ambiances et aux énergies environnantes. Protégez votre paix intérieure comme un trésor rare, recherchez la proximité purificatrice de l'eau et écoutez les besoins changeants de votre corps avec une bienveillance maternelle. Évitez les lieux bruyants ou les personnalités toxiques qui pourraient drainer votre vitalité. Des activités comme le yoga, le tai-chi ou de simples promenades dans le calme vous permettront de maintenir cet équilibre délicat entre votre monde intérieur et extérieur."
    },
    3: {
        "pro": "L'éclat de la création illumine votre chemin professionnel, transformant chaque défi en une opportunité de briller par votre ingéniosité. Votre parole devient une force de persuasion redoutable et vos idées originales agissent comme des phares dans la nuit pour vos collaborateurs. C'est le mois idéal pour l'expression de vos talents, pour les contacts féconds et pour un rayonnement social sans précédent. Osez paraître sur le devant de la scène et partager vos visions les plus audacieuses, car le monde est enfin prêt à les recevoir avec enthousiasme. Votre charisme est votre meilleur outil de travail, utilisez-le avec panache.",
        "coeur": "La joie de vivre et une légèreté bienvenue s'invitent à votre table, dissipant les nuages de la mélancolie ou du sérieux excessif. Les échanges affectifs sont teintés d'un humour complice et d'une séduction naturelle qui attirent à vous les regards et les attentions. C'est une période faste pour les nouvelles rencontres, les célébrations entre amis et l'épanouissement des plaisirs sensoriels de l'existence. Laissez votre cœur s'exprimer avec spontanéité, sans peur du jugement ou du qu'en-dira-t-on. L'amour se vit ici comme un jeu délicieux, une danse légère qui réenchante votre quotidien et vos liens existants.",
        "argent": "Une chance subtile mais réelle accompagne vos finances ce mois-ci, souvent déclenchée par votre réseau relationnel ou votre créativité débordante. La fluidité monétaire est favorisée par votre capacité à communiquer sur vos projets et à susciter l'intérêt de nouveaux partenaires. L'abondance peut venir par des voies inattendues, souvent liées à votre charisme ou à un talent que vous aviez jusqu'ici sous-estimé. N'ayez pas peur de mettre en avant vos services ou vos produits ; votre enthousiasme est contagieux et attire les investisseurs. C'est un temps pour la circulation joyeuse de l'argent et pour quelques plaisirs mérités.",
        "bienetre": "Votre moral est actuellement votre meilleur remède, agissant comme un bouclier naturel contre la fatigue et le stress. Cultivez l'enthousiasme, entourez-vous de personnes positives et stimulez votre esprit par des activités créatives ou artistiques. Veillez toutefois à ne point disperser votre précieuse essence vitale dans des futilités ou une agitation sociale excessive qui finirait par vous vider de votre substance. Un sommeil régulier et de qualité soutiendra votre pétillance naturelle et préservera l'éclat de votre peau et de vos yeux. La joie est une nourriture spirituelle dont votre corps a un besoin impérieux."
    },
    4: {
        "pro": "L'heure est à l'Édification patiente et rigoureuse de vos ambitions les plus chères. Les rênes du destin demandent en ce moment une main ferme, une discipline de fer et un sens aigu de l'organisation pratique. C'est le temps de la structure, de l'ordre intérieur et du labeur patient qui ne cherche point la lumière immédiate. Construisez brique après brique, sans jamais chercher le raccourci facile, car seules les fondations que vous coulez aujourd'hui résisteront aux tempêtes futures. Votre fiabilité devient votre plus grand atout professionnel, attirant la confiance de ceux qui comptent vraiment dans votre milieu.",
        "coeur": "La sécurité émotionnelle et la loyauté indéfectible sont les piliers centraux de ce mois de construction affective. On ne cherche point l'aventure éphémère ou les passions dévastatrices, mais l'ancrage durable dans la réalité du quotidien partagé. C'est le moment idéal pour prouver votre attachement sincère par des actes concrets, une présence rassurante et une écoute qui ne faiblit jamais. Pour les couples, c'est le temps des projets immobiliers ou familiaux solides ; pour les célibataires, c'est l'exigence de trouver un partenaire qui partage vos valeurs de stabilité et de sérieux. L'amour se prouve ici par la durée.",
        "argent": "La prospérité ce mois-ci ne doit rien au hasard, elle naît directement de votre rigueur et de votre sens de l'économie. Établissez vos comptes avec une précision chirurgicale, prévoyez l'imprévisible et investissez prioritairement dans le durable et le concret. La terre, l'immobilier ou les valeurs refuges sont des alliées sûres sous cette vibration de stabilité retrouvée. Évitez toute forme de spéculation hasardeuse qui pourrait compromettre vos efforts passés. Votre richesse se bâtit sur la prudence et sur une gestion de bon père de famille, garantissant une tranquillité d'esprit indispensable pour vos projets futurs.",
        "bienetre": "Votre corps demande aujourd'hui du respect, de la régularité et une structure claire dans votre hygiène de vie. Honorez votre temple physique par une discipline sans faille, en privilégiant une alimentation saine et des horaires de repos fixes. Surveillez particulièrement vos articulations, votre dos et votre ossature ; ne portez point de charges trop lourdes, qu'elles soient réelles ou symboliques. Des exercices de renforcement musculaire ou de la marche régulière en terrain stable vous feront le plus grand bien. La santé est ici le résultat d'un équilibre entre l'effort physique maîtrisé et une discipline mentale rigoureuse."
    },
    5: {
        "pro": "Un vent puissant de Mutation souffle sur votre vie professionnelle, balayant les certitudes pour laisser place à l'imprévu créateur. Les chaînes de la routine et de la stagnation se brisent enfin pour vous offrir l'aventure, les voyages ou de nouvelles méthodes de travail révolutionnaires. Soyez tel le voyageur prêt à saisir chaque opportunité au vol, car le mouvement perpétuel est en ce moment votre seule constante bénéfique. Votre capacité d'adaptation et votre agilité mentale seront vos plus grandes forces pour naviguer dans ce chaos fertile. Ne craignez pas de changer de cap si le vent tourne ; l'univers favorise votre audace.",
        "coeur": "L'énergie du désir, de la curiosité et de la liberté individuelle s'intensifie brusquement dans votre sphère sentimentale. C'est un temps idéal pour explorer de nouveaux horizons affectifs, pour rompre avec la monotonie des habitudes et pour redécouvrir avec émerveillement le plaisir de l'imprévu à deux. Laissez-vous surprendre par l'inconnu, osez des expériences qui sortent de votre cadre habituel et libérez-vous des carcans qui étouffaient votre spontanéité. L'amour se vit ici comme une exploration passionnante, un voyage sans carte où seule l'intensité du moment présent compte vraiment. Soyez prêt pour l'aventure.",
        "argent": "Les flux financiers sont rapides, vifs et parfois instables, demandant une attention de chaque instant et une grande souplesse de réaction. L'argent circule avec une vélocité étonnante ce mois-ci ; il peut entrer en abondance par des voies nouvelles mais peut aussi repartir rapidement pour financer vos soifs de liberté ou de changement. Gardez une main agile sur la bourse tout en restant ouvert aux opportunités d'investissement audacieuses dans les nouvelles technologies ou les domaines innovants. C'est un temps pour le mouvement monétaire, pour oser des transactions rapides et pour faire fructifier votre sens inné de l'opportunisme sain.",
        "bienetre": "Une vitalité bouillonnante et une soif d'expérience vous animent, vous poussant à explorer vos limites physiques et mentales. Vous avez un besoin impérieux d'air, d'espace, de nouveauté et de stimuli sensoriels variés pour vous sentir pleinement vivant. Prenez garde toutefois aux excès de toutes sortes et à l'impulsivité qui pourraient fragiliser votre équilibre nerveux à la longue. La respiration profonde, les sports de plein air ou les voyages de découverte seront vos meilleurs alliés pour canaliser cette énergie de changement sans vous épuiser. Votre corps a besoin de se sentir libre de ses mouvements pour rester en pleine santé."
    },
    6: {
        "pro": "L'Harmonie relationnelle et le sens de la Responsabilité partagée sont vos maîtres-mots absolus pour ce mois de construction collective. On attend de vous la justesse d'un juge, la patience d'un diplomate et la bienveillance inspirante d'un mentor pour votre équipe ou vos collaborateurs. C'est le moment idéal pour embellir concrètement votre cadre de travail, apaiser les tensions latentes et assumer pleinement votre rôle de pilier au sein de votre communauté professionnelle. Votre succès n'est plus un exploit solitaire, mais la conséquence directe de l'équilibre que vous savez instaurer autour de vous. La reconnaissance viendra de votre intégrité sans faille.",
        "coeur": "Le foyer est désormais votre véritable sanctuaire et l'amour la boussole qui oriente chacun de vos choix de vie importants. Cette vibration chaleureuse favorise l'engagement profond, la création d'un cocon protecteur et le soin méticuleux porté aux êtres qui vous sont chers. C'est un temps idéal pour le mariage, l'agrandissement de la famille, une installation commune ou une réconciliation durable après des périodes de trouble. Laissez votre cœur s'exprimer à travers la tendresse, le dévouement et la volonté de créer une beauté durable dans vos relations. L'amour se vit ici comme un art de l'harmonie quotidienne, un don de soi qui nourrit l'âme.",
        "argent": "L'équilibre financier se trouve ce mois-ci dans la gestion judicieuse des besoins familiaux et dans l'investissement porté sur votre confort personnel et celui des vôtres. Vos décisions monétaires doivent viser avant tout l'amélioration de la qualité de vie, l'embellissement de votre habitat ou la sécurisation de l'avenir de vos proches. La générosité équilibrée — savoir donner sans vous appauvrir — attire paradoxalement à son tour l'abondance dans votre sphère de vie. C'est un temps favorable pour les investissements immobiliers familiaux, les assurances prévoyantes et tout ce qui renforce le sentiment de sécurité matérielle au sein du foyer. La richesse sert ici la paix.",
        "bienetre": "Le corps et l'esprit réclament aujourd'hui une dose massive de beauté, de douceur et d'harmonie sensorielle pour fonctionner au mieux. Entourez-vous de couleurs apaisantes, écoutez des musiques qui élèvent votre soul et prenez soin de votre équilibre hormonal et circulatoire par des méthodes naturelles et douces. La paix émotionnelle est le gage absolu de votre santé physique ce mois-ci ; évitez les conflits qui drainent votre énergie vitale. Des soins esthétiques, des massages relaxants ou la pratique du jardinage vous permettront de vous reconnecter à la terre tout en cultivant votre propre jardin intérieur. Soyez doux avec vous-même."
    },
    7: {
        "pro": "Le temps semble s'arrêter ce mois-ci pour laisser place à la Connaissance profonde et à la réflexion stratégique de haut vol. Détachez-vous de l'agitation superficielle du monde professionnel pour parfaire vos savoirs et affiner votre vision à long terme. La victoire appartient à celui qui sait voir ce que les autres ignorent par manque de recul. Votre esprit est votre arme la plus tranchante.",
        "coeur": "Une certaine distance émotionnelle ou physique est temporairement nécessaire pour mieux comprendre la véritable nature de vos sentiments. C'est un temps de solitude choisie et féconde, ou de partage intellectuel intense. Le silence est le terreau sacré où germent actuellement les unions les plus profondes. L'amour est un mystère qui demande de la patience.",
        "argent": "La gestion de l'argent demande ce mois-ci une grande retenue et une analyse froide des opportunités. Observez les marchés, mais ne vous hâtez point de conclure des transactions sous l'influence de l'émotion. Un secret financier ou une information confidentielle pourrait être révélé à votre avantage. La richesse vient ici de l'esprit et de la prudence.",
        "bienetre": "Le repos de l'esprit et la protection de votre système nerveux sont vos priorités absolues. Méditez, lisez, et n'hésitez point à vous retirer du tumulte social dès que vous en ressentez le besoin. Votre système nerveux est sollicité par vos réflexions intenses ; accordez-lui le calme et le sommeil profond qu'il réclame pour se régénérer."
    },
    8: {
        "pro": "La Puissance et l'Accomplissement concret se manifestent avec force. C'est le mois de la récolte : vous obtenez ce que vous avez semé. Affirmez votre ambition, tranchez les nœuds gordiens et assumez votre autorité. Le succès matériel massif vous tend les bras si vous agissez avec intégrité. Vous êtes le chef d'orchestre de votre réussite.",
        "coeur": "Les sentiments sont vécus avec une intensité volcanique. C'est un temps idéal pour vivre des émotions fortes et utiliser votre magnétisme. Veillez toutefois à ce que cette passion ne devienne pas un besoin de contrôle. L'amour est ici une force de transformation puissante qui demande à être canalisée par le respect mutuel.",
        "argent": "Les flux financiers sont à leur paroxysme. C'est le moment idéal pour négocier des contrats d'envergure ou restructurer vos avoirs de manière offensive. L'argent est pour vous une énergie de puissance. Votre flair pour les affaires est à son comble, vous permettant de débusquer la rentabilité là où les autres voient des risques.",
        "bienetre": "Votre énergie vitale est colossale, mais elle peut être brutale pour votre organisme. Surveillez votre tension et le stress lié à la quête de réussite. Apprenez à relâcher chaque muscle après l'effort et accordez-vous des plages de décompression totale. La pratique d'un sport intense vous aidera à évacuer le trop-plein d'adrénaline."
    },
    9: {
        "pro": "L'heure est à l'Achèvement de vos projets et à l'Ouverture sur le monde. Un cycle majeur se termine, vous demandant de clore les dossiers en suspens. Votre rayonnement dépasse vos frontières habituelles pour toucher un public vaste. C'est le temps de la transmission. La fin d'une étape est la promesse d'une ascension future.",
        "coeur": "L'amour se fait universel et compassionnel, vous poussant à donner un sens plus vaste à vos relations. C'est un mois idéal pour les grands voyages intérieurs et un lâcher-prise sur les blessures du passé. Laissez votre cœur s'ouvrir à l'inconnu ; c'est dans le don désintéressé que vous trouverez votre plus grande satisfaction.",
        "argent": "L'abondance vient par des voies détournées ou des opportunités liées à l'étranger. Ne retenez pas les ressources avec avarice ; laissez-les circuler, car c'est ainsi que la nouvelle richesse se prépare. C'est un temps pour régler vos derniers comptes matériels et préparer le terrain vierge du prochain cycle. L'argent est une récompense.",
        "bienetre": "Un besoin de purification totale du corps et de l'esprit se fait sentir. Nettoyez votre organisme et libérez votre mental des rancœurs anciennes. L'écoute de votre intuition vous apportera les clés de votre régénération. Votre santé dépend de votre capacité à lâcher ce qui est mort pour laisser la place au flux nouveau."
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
        # Format français (DD/MM/YYYY)
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
            
            # CALCULS
            ap = reduire(dnais.day + dnais.month + an_actuelle)
            vib = reduire(ap + (idx_mois + 1))
            
            # AFFICHAGE
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
