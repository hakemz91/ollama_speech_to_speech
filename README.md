# ollama_speech_to_speech for Windows
Chatbot speech to speech using Ollama
### Requirements for this setup:
- ffmpeg installed (https://phoenixnap.com/kb/ffmpeg-windows)
- NVIDIA GPU (will prob work with only CPU too)
- microphone
- Install Ollama. Get it here: https://ollama.com/
- Anaconda installation. Get it here: https://docs.anaconda.com/free/anaconda/install/windows/

### How to install and setup:

1. git clone this repo to any folder in your PC: https://github.com/hakemz91/ollama_speech_to_speech.git
2. Create new anaconda environment and activate it using command below:
   conda create -n ollama_speech_to_speech python=3.10 -y
   then,
   conda activate ollama_speech_to_speech
4. cd to dir ollama_speech_to_speech
5. pip install -r requirements.txt
6. download https://nordnet.blob.core.windows.net/bilde/checkpoints.zip
7. extract checkpoints.zip to ollama_speech_to_speech folder
8. In talk3.py , change the path of joa.mp3 in line 247 to your path. Use forward slash.
9. run talk3.py

