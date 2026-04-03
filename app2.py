import streamlit as st
from datetime import datetime

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Numérologie Pro", page_icon="✨", layout="centered")

# --- FONCTION DE CALCUL ---
def reduire(n):
    while n > 9:
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
            "pro": """L'heure est à l'Alliance stratégique et à l'exercice subtil de la diplomatie. La force brutale et les décisions solitaires doivent céder le pas à la finesse du discernement et à l'écoute active des besoins de vos partenaires. Vos succès ce mois-ci naîtront de votre capacité unique à unir les contraires et à percevoir les opportunités cachées dans les murmures entre les mots. Cultivez la patience de l'agriculteur, car les fruits les plus savoureux mûrissent toujours dans l'ombre des collaborations fertiles. Votre rôle est celui du médiateur, de celui qui fluidifie les échanges pour le bien commun.""",
            "coeur": """Une vibration de douceur et de réceptivité enveloppe vos échanges affectifs. Les liens les plus forts se tissent désormais dans la confidence, le partage des silences et une écoute profonde des émotions de l'autre. C'est un temps idéal pour l'harmonie, le pardon sincère et la fusion des âmes qui cherchent un port paisible. Laissez votre intuition guider vos pas vers ceux qui résonnent véritablement avec la fréquence de votre cœur, sans chercher à forcer le destin. La tendresse est votre meilleure alliée pour ouvrir les portes qui semblaient closes ; laissez la vulnérabilité devenir votre force.""",
            "argent": """La prospérité ce mois-ci dépend étroitement de votre équilibre intérieur et de votre capacité à collaborer. Évitez les mouvements financiers brusques, les investissements impulsifs ou les spéculations solitaires qui pourraient déstabiliser vos acquis. Les gains les plus solides se trouvent dans les associations réfléchies, les contrats de confiance et la gestion sage des ressources partagées. C'est un moment favorable pour demander conseil à des experts ou pour conclure des accords basés sur le bénéfice mutuel. L'argent est ici le résultat d'une entente harmonieuse avec le flux de la vie.""",
            "bienetre": """Votre sensibilité est actuellement votre boussole la plus précieuse, mais elle vous rend également très perméable aux ambiances et aux énergies environnantes. Protégez votre paix intérieure comme un trésor rare, recherchez la proximité purificatrice de l'eau et écoutez les besoins changeants de votre corps avec une bienveillance maternelle. Évitez les lieux bruyants ou les personnalités toxiques qui pourraient drainer votre vitalité. Des activités comme le yoga, le tai-chi ou de simples promenades dans le calme vous permettront de maintenir cet équilibre délicat entre votre monde intérieur et extérieur."""
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
            "pro": """L'éclat de la création illumine votre chemin professionnel, transformant chaque défi en une opportunité de briller par votre ingéniosité. Votre parole devient une force de persuasion redoutable et vos idées originales agissent comme des phares dans la nuit pour vos collaborateurs. C'est le mois idéal pour l'expression de vos talents, pour les contacts féconds et pour un rayonnement social sans précédent. Osez paraître sur le devant de la scène et partager vos visions les plus audacieuses, car le monde est enfin prêt à les recevoir avec enthousiasme. Votre charisme est votre meilleur outil de travail, utilisez-le avec panache.""",
            "coeur": """La joie de vivre et une légèreté bienvenue s'invitent à votre table, dissipant les nuages de la mélancolie ou du sérieux excessif. Les échanges affectifs sont teintés d'un humour complice et d'une séduction naturelle qui attirent à vous les regards et les attentions. C'est une période faste pour les nouvelles rencontres, les célébrations entre amis et l'épanouissement des plaisirs sensoriels de l'existence. Laissez votre cœur s'exprimer avec spontanéité, sans peur du jugement ou du qu'en-dira-t-on. L'amour se vit ici comme un jeu délicieux, une danse légère qui réenchante votre quotidien et vos liens existants.""",
            "argent": """Une chance subtile mais réelle accompagne vos finances ce mois-ci, souvent déclenchée par votre réseau relationnel ou votre créativité débordante. La fluidité monétaire est favorisée par votre capacité à communiquer sur vos projets et à susciter l'intérêt de nouveaux partenaires. L'abondance peut venir par des voies inattendues, souvent liées à votre charisme ou à un talent que vous aviez jusqu'ici sous-estimé. N'ayez pas peur de mettre en avant vos services ou vos produits ; votre enthousiasme est contagieux et attire les investisseurs. C'est un temps pour la circulation joyeuse de l'argent et pour quelques plaisirs mérités.""",
            "bienetre": """Votre moral est actuellement votre meilleur remède, agissant comme un bouclier naturel contre la fatigue et le stress. Cultivez l'enthousiasme, entourez-vous de personnes positives et stimulez votre esprit par des activités créatives ou artistiques. Veillez toutefois à ne point disperser votre précieuse essence vitale dans des futilités ou une agitation sociale excessive qui finirait par vous vider de votre substance. Un sommeil régulier et de qualité soutiendra votre pétillance naturelle et préservera l'éclat de votre peau et de vos yeux. La joie est une nourriture spirituelle dont votre corps a un besoin impérieux."""
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
            "pro": """L'heure est à l'Édification patiente et rigoureuse de vos ambitions les plus chères. Les rênes du destin demandent en ce moment une main ferme, une discipline de fer et un sens aigu de l'organisation pratique. C'est le temps de la structure, de l'ordre intérieur et du labeur patient qui ne cherche point la lumière immédiate. Construisez brique après brique, sans jamais chercher le raccourci facile, car seules les fondations que vous coulez aujourd'hui résisteront aux tempêtes futures. Votre fiabilité devient votre plus grand atout professionnel, attirant la confiance de ceux qui comptent vraiment dans votre milieu.""",
            "coeur": """La sécurité émotionnelle et la loyauté indéfectible sont les piliers centraux de ce mois de construction affective. On ne cherche point l'aventure éphémère ou les passions dévastatrices, mais l'ancrage durable dans la réalité du quotidien partagé. C'est le moment idéal pour prouver votre attachement sincère par des actes concrets, une présence rassurante et une écoute qui ne faiblit jamais. Pour les couples, c'est le temps des projets immobiliers ou familiaux solides ; pour les célibataires, c'est l'exigence de trouver un partenaire qui partage vos valeurs de stabilité et de sérieux. L'amour se prouve ici par la durée.""",
            "argent": """La prospérité ce mois-ci ne doit rien au hasard, elle naît directement de votre rigueur et de votre sens de l'économie. Établissez vos comptes avec une précision chirurgicale, prévoyez l'imprévisible et investissez prioritairement dans le durable et le concret. La terre, l'immobilier ou les valeurs refuges sont des alliées sûres sous cette vibration de stabilité retrouvée. Évitez toute forme de spéculation hasardeuse qui pourrait compromettre vos efforts passés. Votre richesse se bâtit sur la prudence et sur une gestion de bon père de famille, garantissant une tranquillité d'esprit indispensable pour vos projets futurs.""",
            "bienetre": """Votre corps demande aujourd'hui du respect, de la régularité et une structure claire dans votre hygiène de vie. Honorez votre temple physique par une discipline sans faille, en privilégiant une alimentation saine et des horaires de repos fixes. Surveillez particulièrement vos articulations, votre dos et votre ossature ; ne portez point de charges trop lourdes, qu'elles soient réelles ou symboliques. Des exercices de renforcement musculaire ou de la marche régulière en terrain stable vous feront le plus grand bien. La santé est ici le résultat d'un équilibre entre l'effort physique maîtrisé et une discipline mentale rigoureuse."""
        },
        "v2": {
            "pro": """Le retour du bâtisseur dans votre cycle vous demande de vérifier avec minutie la solidité de ce que vous avez érigé jusqu'ici. C'est un mois consacré au perfectionnement technique, à la révision des procédures et à la finition soignée de vos projets en cours. Votre expertise devient votre bouclier le plus sûr face à la concurrence.""",
            "coeur": """L'engagement sentimental se confirme et s'approfondit sous le poids des responsabilités partagées assumées avec joie. Ce qui était auparavant une structure nécessaire devient désormais un véritable sanctuaire émotionnel où vous vous sentez protégé. Le foyer et la famille sont au centre de vos préoccupations.""",
            "argent": """La patience et le travail acharné finissent par payer de manière concrète, apportant des résultats tangibles à vos finances. Vos efforts passés commencent à se cristalliser en une sécurité matérielle plus confortable, vous permettant d'envisager des investissements de consolidation.""",
            "bienetre": """Apprenez à assouplir votre discipline quotidienne pour ne point briser votre propre résistance interne par un excès d'exigence envers vous-même."""
        },
        "v3": {
            "pro": """Vous atteignez désormais le rang de Maître d'Œuvre, celui qui n'a plus besoin de manipuler chaque pierre pour que l'édifice monte. La structure que vous avez bâtie avec tant de peine fonctionne désormais avec une efficacité qui vous permet de déléguer les détails opérationnels. Le succès est ici le couronnement d'une vie.""",
            "coeur": """La fondation affective sur laquelle vous avez travaillé est désormais éternelle et indestructible aux yeux de tous. Vos liens amoureux ou familiaux sont si ancrés dans la réalité et la confiance mutuelle qu'ils forment une base sacrée. C'est une période de grande paix domestique.""",
            "argent": """La richesse est désormais sécurisée et vous passez définitivement de l'accumulation anxieuse à la gestion sereine d'un patrimoine solide. Votre sécurité financière n'est plus un sujet d'inquiétude, mais le socle sur lequel repose votre sérénité d'esprit.""",
            "bienetre": """Une robustesse exceptionnelle et une vitalité de roc vous habitent désormais, témoignant de votre victoire sur les aléas de la vie. Votre corps est devenu un allié discipliné, endurant et parfaitement régulé, capable de soutenir vos projets les plus ambitieux sans faillir."""
        }
    },
    5: {
        "v1": {
            "pro": """Un vent puissant de Mutation souffle sur votre vie professionnelle, balayant les certitudes pour laisser place à l'imprévu créateur. Les chaînes de la routine et de la stagnation se brisent enfin pour vous offrir l'aventure, les voyages ou de nouvelles méthodes de travail révolutionnaires. Soyez tel le voyageur prêt à saisir chaque opportunité au vol, car le mouvement perpétuel est en ce moment votre seule constante bénéfique. Votre capacité d'adaptation et votre agilité mentale seront vos plus grandes forces pour naviguer dans ce chaos fertile. Ne craignez pas de changer de cap si le vent tourne ; l'univers favorise votre audace.""",
            "coeur": """L'énergie du désir, de la curiosité et de la liberté individuelle s'intensifie brusquement dans votre sphère sentimentale. C'est un temps idéal pour explorer de nouveaux horizons affectifs, pour rompre avec la monotonie des habitudes et pour redécouvrir avec émerveillement le plaisir de l'imprévu à deux. Laissez-vous surprendre par l'inconnu, osez des expériences qui sortent de votre cadre habituel et libérez-vous des carcans qui étouffaient votre spontanéité. L'amour se vit ici comme une exploration passionnante, un voyage sans carte où seule l'intensité du moment présent compte vraiment. Soyez prêt pour l'aventure.""",
            "argent": """Les flux financiers sont rapides, vifs et parfois instables, demandant une attention de chaque instant et une grande souplesse de réaction. L'argent circule avec une vélocité étonnante ce mois-ci ; il peut entrer en abondance par des voies nouvelles mais peut aussi repartir rapidement pour financer vos soifs de liberté ou de changement. Gardez une main agile sur la bourse tout en restant ouvert aux opportunités d'investissement audacieuses dans les nouvelles technologies ou les domaines innovants. C'est un temps pour le mouvement monétaire, pour oser des transactions rapides et pour faire fructifier votre sens inné de l'opportunisme sain.""",
            "bienetre": """Une vitalité bouillonnante et une soif d'expérience vous animent, vous poussant à explorer vos limites physiques et mentales. Vous avez un besoin impérieux d'air, d'espace, de nouveauté et de stimuli sensoriels variés pour vous sentir pleinement vivant. Prenez garde toutefois aux excès de toutes sortes et à l'impulsivité qui pourraient fragiliser votre équilibre nerveux à la longue. La respiration profonde, les sports de plein air ou les voyages de découverte seront vos meilleurs alliés pour canaliser cette énergie de changement sans vous épuiser. Votre corps a besoin de se sentir libre de ses mouvements pour rester en pleine santé."""
        },
        "v2": {
            "pro": """Le retour du mouvement perpétuel dans votre carrière ne vous surprend plus ; cette fois, vous ne subissez plus le changement, vous le dirigez avec brio. Votre expérience accumulée vous permet désormais de naviguer avec une aisance magistrale dans les eaux troubles de l'incertitude.""",
            "coeur": """La liberté ne signifie plus pour vous l'errance ou l'instabilité, mais le choix conscient de la nouveauté perpétuelle au sein même de vos engagements existants. Vous apprenez l'art difficile mais magnifique de renouveler vos liens affectifs sans avoir besoin de les briser.""",
            "argent": """La ruse, l'agilité mentale et un sens aigu de la négociation servent admirablement vos finances lors de cette seconde phase de mutation. Vous savez désormais anticiper les retournements de situation avant les autres, ce qui vous permet de sécuriser vos gains.""",
            "bienetre": """Il est crucial ce mois-ci de calmer l'orage intérieur avant qu'il ne se transforme en un stress chronique handicapant. La nervosité accumulée par tant de changements demande à être libérée par des activités de décharge dans de grands espaces naturels."""
        },
        "v3": {
            "pro": """C'est l'heure de la libération professionnelle totale et de l'avènement de votre propre méthode révolutionnaire. Vous avez si bien intégré le concept de changement qu'il est devenu une seconde nature, vous permettant d'agir avec une rapidité fulgurante que personne ne peut égaler.""",
            "coeur": """Le cœur n'a désormais plus de frontières ni de peurs, vous vivez une liberté sentimentale magnifique où la confiance mutuelle a définitivement remplacé la jalousie ou le besoin de contrôle. L'amour est devenu une exploration sans fin des potentiels de l'autre.""",
            "argent": """L'argent vient désormais vers vous par le mouvement pur, la créativité sans entraves et votre capacité à connecter des mondes différents. Vos voyages ou vos déplacements sont les catalyseurs directs de nouvelles richesses inattendues qui affluent.""",
            "bienetre": """Une jeunesse extraordinaire du corps et de l'esprit se manifeste en vous, comme si le mouvement permanent vous avait immunisé contre le vieillissement. Votre capacité d'adaptation physique est devenue prodigieuse, vous permettant de récupérer d'efforts intenses avec rapidité."""
        }
    },
    6: {
        "v1": {
            "pro": """L'Harmonie relationnelle et le sens de la Responsabilité partagée sont vos maîtres-mots absolus pour ce mois de construction collective. On attend de vous la justesse d'un juge, la patience d'un diplomate et la bienveillance inspirante d'un mentor pour votre équipe ou vos collaborateurs. C'est le moment idéal pour embellir concrètement votre cadre de travail, apaiser les tensions latentes et assumer pleinement votre rôle de pilier au sein de votre communauté professionnelle. Votre succès n'est plus un exploit solitaire, mais la conséquence directe de l'équilibre que vous savez instaurer autour de vous. La reconnaissance viendra de votre intégrité sans faille.""",
            "coeur": """Le foyer est désormais votre véritable sanctuaire et l'amour la boussole qui oriente chacun de vos choix de vie importants. Cette vibration chaleureuse favorise l'engagement profond, la création d'un cocon protecteur et le soin méticuleux porté aux êtres qui vous sont chers. C'est un temps idéal pour le mariage, l'agrandissement de la famille, une installation commune ou une réconciliation durable après des périodes de trouble. Laissez votre cœur s'exprimer à travers la tendresse, le dévouement et la volonté de créer une beauté durable dans vos relations. L'amour se vit ici comme un art de l'harmonie quotidienne, un don de soi qui nourrit l'âme.""",
            "argent": """L'équilibre financier se trouve ce mois-ci dans la gestion judicieuse des besoins familiaux et dans l'investissement porté sur votre confort personnel et celui des vôtres. Vos décisions monétaires doivent viser avant tout l'amélioration de la qualité de vie, l'embellissement de votre habitat ou la sécurisation de l'avenir de vos proches. La générosité équilibrée — savoir donner sans vous appauvrir — attire paradoxalement à son tour l'abondance dans votre sphère de vie. C'est un temps favorable pour les investissements immobiliers familiaux, les assurances prévoyantes et tout ce qui renforce le sentiment de sécurité matérielle au sein du foyer. La richesse sert ici la paix.""",
            "bienetre": """Le corps et l'esprit réclament aujourd'hui une dose massive de beauté, de douceur et d'harmonie sensorielle pour fonctionner au mieux. Entourez-vous de couleurs apaisantes, écoutez des musiques qui élèvent votre soul et prenez soin de votre équilibre hormonal et circulatoire par des méthodes naturelles et douces. La paix émotionnelle est le gage absolu de votre santé physique ce mois-ci ; évitez les conflits qui drainent votre énergie vitale. Des soins esthétiques, des massages relaxants ou la pratique du jardinage vous permettront de vous reconnecter à la terre tout en cultivant votre propre jardin intérieur. Soyez doux avec vous-même."""
        },
        "v2": {
            "pro": """L'exigence du service envers autrui s'accentue dans votre vie professionnelle, faisant de vous la figure centrale vers laquelle tout le monde se tourne. Votre sens inné du devoir est mis à l'épreuve par des sollicitations nombreuses, apportant une reconnaissance sans égal.""",
            "coeur": """L'amour se fait aujourd'hui sacrifice joyeux et don de soi, non par obligation, mais dans la joie profonde de voir l'autre s'épanouir. C'est une période de grande maturité affective où le lien se renforce par la traversée commune des responsabilités quotidiennes.""",
            "argent": """Les fruits de votre loyauté passée et de votre sérieux sont enfin là, apportant une stabilité financière qui vous permet de souffler un peu. La prospérité est désormais acquise si vous maintenez votre cap éthique et si vous ne cédez pas à des tentations douteuses.""",
            "bienetre": """Attention à ne point vous oublier totalement dans le soin constant porté aux autres, car votre réserve d'énergie vitale n'est point inépuisable. Apprenez l'art difficile de dire non avec douceur pour préserver l'harmonie de votre propre temple physique."""
        },
        "v3": {
            "pro": """Vous incarnez désormais la Sagesse du Conseil au sein de votre environnement professionnel, devenant une figure d'inspiration qui transcende les simples fonctions. Votre rôle dépasse désormais le cadre strictement technique pour devenir celui d'un architecte de l'harmonie humaine.""",
            "coeur": """Vous accédez à l'expérience du Grand Amour, celui qui ne demande rien et qui offre tout dans une plénitude affective qui irradie sur tout votre entourage. Votre foyer est devenu une perle de sérénité, un modèle d'équilibre que vos amis et votre famille prennent pour exemple.""",
            "argent": """L'abondance de confort et la paix matérielle totale caractérisent votre situation financière en cette phase de maîtrise. La richesse n'est plus pour vous un but en soi, mais le moyen naturel et fluide d'assurer la paix, la beauté et la sécurité autour de vous.""",
            "bienetre": """Une santé basée sur l'équilibre parfait et une connaissance intuitive de votre corps vous procurent un sentiment de jeunesse durable. Votre bien-être est devenu une émanation naturelle de votre paix intérieure, se traduisant par un teint radieux et une énergie constante."""
        }
    },
    7: {
        "v1": {
            "pro": """Le temps semble s'arrêter ce mois-ci pour laisser place à la Connaissance profonde et à la réflexion stratégique de haut vol. Détachez-vous de l'agitation superficielle du monde professionnel pour parfaire vos savoirs et affiner votre vision à long terme. La victoire appartient à celui qui sait voir ce que les autres ignorent par manque de recul. Votre esprit est votre arme la plus tranchante.""",
            "coeur": """Une certaine distance émotionnelle ou physique est temporairement nécessaire pour mieux comprendre la véritable nature de vos sentiments. C'est un temps de solitude choisie et féconde, ou de partage intellectuel intense. Le silence est le terreau sacré où germent actuellement les unions les plus profondes. L'amour est un mystère qui demande de la patience.""",
            "argent": """La gestion de l'argent demande ce mois-ci une grande retenue et une analyse froide des opportunités. Observez les marchés, mais ne vous hâtez point de conclure des transactions sous l'influence de l'émotion. Un secret financier ou une information confidentielle pourrait être révélé à votre avantage. La richesse vient ici de l'esprit et de la prudence.""",
            "bienetre": """Le repos de l'esprit et la protection de votre système nerveux sont vos priorités absolues. Méditez, lisez, et n'hésitez point à vous retirer du tumulte social dès que vous en ressentez le besoin. Votre système nerveux est sollicité par vos réflexions intenses ; accordez-lui le calme et le sommeil profond qu'il réclame pour se régénérer."""
        },
        "v2": {
            "pro": """Votre intuition devient un outil de travail redoutable : vous voyez ce que les autres ne perçoivent pas encore. C'est le mois des découvertes majeures et des solutions innovantes. Travaillez dans le calme. Votre autorité est celle de celui qui sait.""",
            "coeur": """La connexion d'âme à âme est privilégiée : vous vivez des moments de grâce et de compréhension mutuelle sans paroles. Votre sensibilité est à fleur de peau, vous rendant plus réceptif à la beauté des sentiments.""",
            "argent": """Des opportunités inattendues surgissent grâce à votre intuition. Soyez attentif aux signes et aux rencontres fortuites. Votre gestion est marquée par une vision à long terme qui rassure vos partenaires.""",
            "bienetre": """Une harmonie profonde s'installe entre votre mental et votre corps. Vous ressentez une paix intérieure qui se reflète sur votre vitalité physique. Votre sommeil est réparateur et riche en rêves inspirants."""
        },
        "v3": {
            "pro": """Vous accédez à la Sagesse Visionnaire : votre vision professionnelle dépasse largement le cadre habituel. Vous devenez un guide ou un consultant recherché pour votre clairvoyance. Vos projets sont portés par une dimension spirituelle forte.""",
            "coeur": """L'amour est vécu comme une Communion Sacrée, une fusion des esprits et des cœurs. Vous atteignez un niveau de compréhension où le pardon et la compassion sont naturels. Vous vivez une paix affective absolue.""",
            "argent": """L'Abondance Consciente se manifeste : vos besoins sont comblés car vous agissez en accord total avec les lois universelles. L'argent circule pour soutenir vos projets les plus nobles.""",
            "bienetre": """Une conscience corporelle totale et une maîtrise de vos énergies vitales caractérisent votre état actuel. Vous incarnez le sage dont la simple présence dégage du calme et de la sérénité."""
        }
    },
    8: {
        "v1": {
            "pro": """La Puissance et l'Accomplissement concret se manifestent avec force. C'est le mois de la récolte : vous obtenez ce que vous avez semé. Affirmez votre ambition, tranchez les nœuds gordiens et assumez votre autorité. Le succès matériel massif vous tend les bras si vous agissez avec intégrité. Vous êtes le chef d'orchestre de votre réussite.""",
            "coeur": """Les sentiments sont vécus avec une intensité volcanique. C'est un temps idéal pour vivre des émotions fortes et utiliser votre magnétisme. Veillez toutefois à ce que cette passion ne devienne pas un besoin de contrôle. L'amour est ici une force de transformation puissante qui demande à être canalisée par le respect mutuel.""",
            "argent": """Les flux financiers sont à leur paroxysme. C'est le moment idéal pour négocier des contrats d'envergure ou restructurer vos avoirs de manière offensive. L'argent est pour vous une énergie de puissance. Votre flair pour les affaires est à son comble, vous permettant de débusquer la rentabilité là où les autres voient des risques.""",
            "bienetre": """Votre énergie vitale est colossale, mais elle peut être brutale pour votre organisme. Surveillez votre tension et le stress lié à la quête de réussite. Apprenez à relâcher chaque muscle après l'effort et accordez-vous des plages de décompression totale. La pratique d'un sport intense vous aidera à évacuer le trop-plein d'adrénaline."""
        },
        "v2": {
            "pro": """La maîtrise subtile du pouvoir est votre défi : vous ne cherchez plus à prouver votre force par l'agitation. Votre influence grandit naturellement. On vous respecte pour votre capacité à trancher les situations avec une justice exemplaire. Votre stature de leader s'affirme par la justesse de vos actes et la solidité de vos résultats.""",
            "coeur": """La passion se mue en un pouvoir protecteur au service de votre bonheur commun. Vous bâtissez un destin grandiose avec ceux que vous aimez. C'est un temps pour les réalisations concrètes à deux : achats de biens ou projets audacieux. L'amour est devenu une alliance de pouvoir et une force de frappe émotionnelle constructive.""",
            "argent": """La fortune sourit aux audacieux qui savent rester justes. Votre flair pour les investissements rentables est devenu infaillible, vous permettant de consolider votre empire matériel. Votre parole vaut de l'or car on sait que vous tenez vos engagements. La richesse s'accumule naturellement.""",
            "bienetre": """Votre temple corporel doit suivre le rythme de votre esprit de conquête, ce qui demande une discipline athlétique. Ne négligez pas les signaux de fatigue sous prétexte de victoire immédiate. Accordez une importance capitale à votre alimentation. Des massages de récupération aideront à maintenir votre organisme au top."""
        },
        "v3": {
            "pro": """Vous atteignez l'Apothéose du Succès : vous êtes au sommet de votre montagne professionnelle. Votre autorité est naturelle et émane simplement de votre présence. On vient solliciter votre arbitrage ou bénéficier de votre protection. La victoire est totale car elle est assortie d'un respect universel.""",
            "coeur": """Un amour impérial couronne votre existence, transformant votre foyer en une dynastie de cœur. La puissance du lien forgé protège tous ceux que vous aimez. Vous vivez une phase où passion et stabilité créent une harmonie royale. Votre rayonnement attire la prospérité pour tout votre clan.""",
            "argent": """La Fortune Souveraine caractérise votre situation : l'argent coule vers vous sans effort car vous êtes un pôle d'attraction. Vous gérez désormais un héritage et une influence. Les flux financiers servent des projets qui dépassent votre personne.""",
            "bienetre": """Une invulnérabilité physique apparente caractérise votre état de bien-être actuel. Vous avez forgé un temple corporel d'une résistance exceptionnelle. Vous irradiez une puissance qui impose le calme. Votre santé est devenue une force de la nature."""
        }
    },
    9: {
        "v1": {
            "pro": """L'heure est à l'Achèvement de vos projets et à l'Ouverture sur le monde. Un cycle majeur se termine, vous demandant de clore les dossiers en suspens. Votre rayonnement dépasse vos frontières habituelles pour toucher un public vaste. C'est le temps de la transmission. La fin d'une étape est la promesse d'une ascension future.""",
            "coeur": """L'amour se fait universel et compassionnel, vous poussant à donner un sens plus vaste à vos relations. C'est un mois idéal pour les grands voyages intérieurs et un lâcher-prise sur les blessures du passé. Laissez votre cœur s'ouvrir à l'inconnu ; c'est dans le don désintéressé que vous trouverez votre plus grande satisfaction.""",
            "argent": """L'abondance vient par des voies détournées ou des opportunités liées à l'étranger. Ne retenez pas les ressources avec avarice ; laissez-les circuler, car c'est ainsi que la nouvelle richesse se prépare. C'est un temps pour régler vos derniers comptes matériels et préparer le terrain vierge du prochain cycle. L'argent est une récompense.""",
            "bienetre": """Un besoin de purification totale du corps et de l'esprit se fait sentir. Nettoyez votre organisme et libérez votre mental des rancœurs anciennes. L'écoute de votre intuition vous apportera les clés de votre régénération. Votre santé dépend de votre capacité à lâcher ce qui est mort pour laisser la place au flux nouveau."""
        },
        "v2": {
            "pro": """La boucle est bouclée et vous avez tiré les leçons des expériences passées. Ce mois agit comme une passerelle vers votre futur, vous demandant de partager votre expérience. Votre autorité est morale et spirituelle. C'est un temps pour le bilan, la gratitude et la préparation sereine de votre prochaine mutation. Vous finissez en beauté.""",
            "coeur": """Le pardon absolu libère enfin votre cœur de ses dernières chaînes. Les liens qui n'ont plus lieu d'être se dissolvent sans douleur, laissant la place à une clarté émotionnelle totale. Vos relations véritables atteignent une dimension de dévouement sublime. Vous vous sentez enfin complet et capable d'aimer sans attente.""",
            "argent": """Le bilan financier est positif si vous avez agi avec humanité. La chance est présente de manière subtile, liée à des projets à vocation collective. Réglez vos derniers comptes et préparez-vous à repartir sur des bases neuves. Vous vivez dans l'abondance du sage qui possède tout car il ne désire plus rien d'inutile.""",
            "bienetre": """Une paix inaltérable s'installe dans chaque fibre de votre être. Votre santé sereine ne dépend plus des circonstances extérieures. Utilisez ce temps pour méditer sur la beauté de votre parcours. La renaissance est imminente. Continuez à honorer ce temple avec une gratitude immense pour tout ce qu'il vous a offert."""
        },
        "v3": {
            "pro": """Vous atteignez l'Inspiration Mondiale : vos projets prennent une dimension altruiste qui touche le plus grand nombre. Vous travaillez désormais pour laisser un héritage de sagesse. Votre carrière se termine parée d'une aura de réussite éthique. Vous avez transmuté le travail en œuvre sacrée. Vous êtes devenu une source de lumière.""",
            "coeur": """L'Amour Inconditionnel est votre réalité, faisant accéder à un état de grâce affective. Vous n'avez plus besoin de réciprocité pour aimer, car votre cœur est un océan de paix inépuisable. Vos relations sont empreintes d'une poésie spirituelle magnifique. Vous vivez dans la gratitude absolue d'avoir aimé. Votre cœur est une porte ouverte.""",
            "argent": """L'Héritage Spirituel et financier se manifeste : vos finances se stabilisent par des retours de fortune liés à votre générosité passée. Vous ne manquez de rien pour entamer le nouveau cycle de vie. Vous avez appris que la véritable monnaie est celle de l'âme. Vous vivez dans l'opulence de l'esprit. Tout est accompli.""",
            "bienetre": """Une Transmutation Physique totale s'opère, vous faisant vous sentir léger et libéré de la pesanteur. Votre corps est purifié, prêt pour la nouvelle incarnation vibratoire qui vous attend. Une énergie sereine irrigue vos cellules pour les maintenir en joie. Offrez votre rayonnement à ceux qui vous entourent. Tout est prêt pour la lumière."""
        }
    }
}

# --- GESTION DE LA CONNEXION ---
if 'auth' not in st.session_state:
    st.session_state['auth'] = False

# --- INTERFACE ---
if not st.session_state['auth']:
    st.title("🔐 Espace Client")
    with st.form("login"):
        e = st.text_input("Email")
        c = st.text_input("Code", type="password")
        if st.form_submit_button("Valider"):
            if e == "test@pro.com" and c == "1234":
                st.session_state['auth'] = True
                st.rerun()
            else:
                st.error("Erreur")
else:
    st.title("✨ Votre Thème Numérologique")
    with st.form("infos"):
        c1, c2 = st.columns(2)
        prenom = c1.text_input("Prénom")
        nom = c1.text_input("Nom")
        dnais = c2.date_input("Naissance", min_value=datetime(1940, 1, 1))
        btn = st.form_submit_button("Générer")

    if btn:
        st.markdown(f"### Rapport pour {prenom} {nom}")
        st.write(INTRO)
        m_dep = datetime.now().month + 1
        a_dep = datetime.now().year
        if m_dep > 12: 
            m_dep = 1
            a_dep += 1
        
        noms = ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sept", "Oct", "Nov", "Déc"]
        compte = {}

        for i in range(12):
            idx = (m_dep - 1 + i) % 12
            an_c = a_dep + (m_dep - 1 + i) // 12
            vib = reduire(reduire(dnais.day + dnais.month + an_c) + (idx + 1))
            
            compte[vib] = compte.get(vib, 0) + 1
            vk = f"v{min(compte[vib], 3)}"
            
            with st.expander(f"📅 {noms[idx]} {an_c} | Vibration {vib}"):
                t = DATA_TEXTES[vib][vk]
                st.write(f"**Pro :** {t['pro']}")
                st.write(f"**Cœur :** {t['coeur']}")
                st.write(f"**Argent :** {t['argent']}")
                st.write(f"**Bien-être :** {t['bienetre']}")
        st.info(CONCLUSION)
