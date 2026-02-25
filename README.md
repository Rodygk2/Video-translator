🎬 AI Video Translator

Transcrire, traduire et générer automatiquement des sous-titres à partir d’une vidéo.

Projet Python utilisant Whisper AI + FFmpeg + NLP pour transformer une vidéo en texte, traduction et sous-titres exploitables.

🚀 Démo du pipeline
Video
  │
  ▼
Audio Extraction (FFmpeg)
  │
  ▼
Speech To Text (Whisper)
  │
  ▼
Language Detection
  │
  ▼
Translation
  │
  ▼
Subtitle Generation (.srt)

🧰 Stack Technique
Technologie	Rôle
Python	Script principal
Whisper	Transcription vocale
FFmpeg	Extraction audio
Deep Translator	Traduction
SRT	Sous-titres
📂 Structure du projet
video-translator
│
├── videos
│   └── video.mp4
│
├── audio
│   └── audio.wav
│
├── outputs
│   ├── transcripts
│   │   └── transcript.txt
│   │
│   ├── translations
│   │   └── translation.txt
│   │
│   └── subtitles
│       └── subtitles.srt
│
├── src
│   ├── extract_audio.py
│   ├── speech_to_text.py
│   ├── translate_text.py
│   └── subtitle_generator.py
│
├── main.py
├── requirements.txt
└── README.md
⚙️ Installation

1️⃣ Cloner le projet
git clone https://github.com/username/video-translator.git
cd video-translator

2️⃣ Créer un environnement virtuel

Windows

python -m venv venv
venv\Scripts\activate

Mac / Linux

python3 -m venv venv
source venv/bin/activate

3️⃣ Installer les dépendances
pip install -r requirements.txt

Si tu n’as pas encore le fichier :

pip install openai-whisper
pip install deep-translator
pip install ffmpeg-python

Puis :

pip freeze > requirements.txt

4️⃣ Installer FFmpeg

Télécharger ici :

https://ffmpeg.org/download.html

Vérifier l'installation :

ffmpeg -version

▶️ Utilisation
Ajouter une vidéo
videos/video.mp4
Lancer le programme
python main.py

📄 Résultats

Après exécution :

outputs/

transcripts/
   transcript.txt

translations/
   translation.txt

subtitles/
   subtitles.srt
🧠 Fonctionnement détaillé
1. Extraction audio
src/extract_audio.py

Commande utilisée :

ffmpeg -i video.mp4 -vn audio.wav

Objectif :

isoler la piste audio

préparer la transcription

2. Speech to Text
src/speech_to_text.py

Utilise :

OpenAI Whisper

Permet :

transcription

détection automatique de langue

timestamps

Exemple résultat :

{
 "text": "...",
 "language": "fr",
 "segments": [...]
}
3. Traduction
src/translate_text.py

Traduction automatique vers :

Français

ou toute autre langue.

4. Génération des sous-titres
src/subtitle_generator.py

Utilise les timestamps Whisper.

Exemple :

1
00:00:01,000 --> 00:00:04,000
Bonjour tout le monde
🎥 Incruster les sous-titres dans la vidéo
ffmpeg -i videos/video.mp4 \
-vf subtitles=outputs/subtitles/subtitles.srt \
outputs/video_final.mp4
⭐ Fonctionnalités

✔ Extraction audio
✔ Transcription automatique
✔ Détection de langue
✔ Traduction
✔ Génération de sous-titres
✔ Pipeline automatisé

🔮 Améliorations futures

Interface Web

Upload de vidéos

Traduction multi-langues

Génération automatique de vidéos sous-titrées

API REST

Traitement en batch

Interface graphique

📊 Exemple d’utilisation réelle

Utilisable pour :

Créateurs de contenu

YouTube

Podcasts

Formation en ligne

Accessibilité

Traduction de conférences

👨‍💻 Auteur

Rodolphe Gbankou

Développeur Web
Bénin 🇧🇯

Compétences :

Python

Laravel

Django

Automatisation

IA appliquée

🤝 Contribution

Les contributions sont les bienvenues.

Fork

Branch

Commit

Pull Request

📜 Licence

Projet open-source sous licence MIT.
