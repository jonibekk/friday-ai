# Friday AI
This is a 100% offline AI Voice Assistant. Completely open source and privacy friendly. Use any language model on GPT4ALL. 

## Setup
1. Install all dependencies from `requirements.txt` file
2. Install `ffmpeg`:
   On Windows: `choco install ffmpeg`
   On MacOS: `brew install ffmpeg`
   on Linux: `sudo apt update && sudo apt install ffmpeg`

   If you are on MacOS, you need to install `portaudio` library: Run `brew install portaudio` 
3. And finally run `python3 main.py`

I highly advise you to use Deepgram or alternative Text-To-Speech services for more human-like natural voices.

## Improvements to think about adding to yours
Give a system prompt. These open source models perform far better when you send a system prompt as specified in the GPT4ALL documentation: https://docs.gpt4all.io/gpt4all_python.html#introspection
