# ollama_speech_to_speech
Chatbot speech to speech using Ollama
### Requirements for this setup:
- ffmpeg installed (https://phoenixnap.com/kb/ffmpeg-windows)
- NVIDIA GPU (will prob work with only CPU too)
- microphone
- Install Ollama. Get it here: https://ollama.com/

### How to install and setup:

1. git clone this repo to any folder in your PC: https://github.com/hakemz91/ollama_speech_to_speech.git
2. cd dir ollama_speech_to_speech
3. pip install -r requirements.txt
4. download https://nordnet.blob.core.windows.net/bilde/checkpoints.zip
5. extract checkpoints.zip to ollama_speech_to_speech folder
8. In talk3.py , change the path of joa.mp3 in line 247 to your path. Use forward slash.
11. run talk3.py (low latency version)

