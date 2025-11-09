# TP1

## Partie 1:

1. Un Block contient une entête contenant le hash du block précédant (à l'exception du tout premier block qui contient comme entête des 0) et des méta-données comme le Nounce, le temps de création du block (timestamp), et pied qui contient le hash du block courant. Le 'body' du block contient les transactions enregistrés à limite de 7 transactions
2. Si on modifie un block ancien:
   - Le hash de la chain change
   - Une vérification de la validité de la chiane est lancé pour décider d'accepter ou de refuser les changements
   - Puisque le hash du block a changé est n'est plus conforme avec les block suivants, les modifications ne sont pas approuvé, sinon la chaine est cassé est la propriété d'immutabilité du BlockChaine
3. Le Bitcoin et l'Ethereum sont basés sur la même technologie de blockchain mais sont implémenté de manières différentes. Parmi les différences les plus pertinentes sont le nombre maximales de pièces de monnaies qui est limitée à 12 millions de BTC mais pas de limite strcite pour le ETH. Aussi l'algorithme de vérification et différents pour les
4. Un hash est une fonction non reversible qui passe dans un seul sens (à partie d'une information on peut générer un hash mais d'un hash on ne peut pas regénérer l'information). Le hash sert comme signature pour signier les blocs et les informations transactionneles du blockchain.

## Partie 2:

1. La modification de la transaction du bloc 1 engendre la modification de tous les blocs concurrant
2. Le hash du block 2 change puisque son entête contient le hash du block précédant et cette information est utilisé pour générer le hash du block 2. Par conséquent, le hash du block 2 (et block 3 aussi) change.
3. La fonction de Hash ici est SHA-256. C'est l'algorithme SHA qui digeste en sortie une chaine de longeur 256 bits
