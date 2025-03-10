# AssistantIA_01

## Description

AssistantIA_01 est un projet Python visant à développer un assistant intelligent capable d'interagir avec l'utilisateur pour répondre à des questions, exécuter des tâches automatisées et fournir diverses informations utiles. Il fonctionne uniquement en utilisant et en lui fournissant des documents pdf. Il ne sera pas capâble de vous répondre si
aucun document ne lui ai fournit. Si vous posez des questions d'où la réponse n'est pas disponible dans le document il ne pourra pas vous répondre.

Vous aurez besoin de votre propré clé API de OpenAI pour le faire fonctionner.

Je tiens à préciser que ce projet est un projet éducatif que j'ai suivi.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/KillianPiccerelle/AssistantIA_01.git
   ```

2. Accédez au répertoire du projet :

   ```bash
   cd AssistantIA_01
   ```

3. Créez un environnement virtuel et activez-le :

   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows, utilisez 'env\Scripts\activate'
   ```

4. Installez les dépendances requises (si un fichier `requirements.txt` est disponible) :
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Copiez le fichier `.env.copy` en `.env` :
   ```bash
   cp .env.copy .env
   ```
2. Modifiez le fichier `.env` pour y insérer vos propres configurations (API keys, chemins, etc.).

## Utilisation

Pour exécuter l'assistant, lancez la commande suivante :

```bash
python AssistantIA.py
```

L'assistant pourra alors interagir avec vous en fonction des configurations définies.

## Licence

Ce projet est sous licence [MIT](LICENSE).

## Auteurs

- **Killian Piccerelle** - Auteur principal

## Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur le dépôt GitHub ou à contacter l'auteur directement.

---

Merci d'utiliser AssistantIA_01 ! 🚀
