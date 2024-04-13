import sys
from gpt4all import GPT4All
import speech_recognition as sr

if sys.platform != 'darwin':
    import pyttsx3
    engine = pyttsx3.init() 


model_name = 'ggml-model-gpt4all-falcon-q4_0.bin'
# model = GPT4All(model_name, allow_download=True) ==> run this to download language model at first.
model_path = r'C:\Users\jonib\.cache\gpt4all'
model = GPT4All(model_name, model_path, allow_download=False)

voices = engine.getProperty('voices') 
mic = sr.Microphone()
recognizer = sr.Recognizer()

transcribing = False
mic_muted = True
wake_word = "friday"

def recognize_speech():
    global mic_muted
    global wake_word
    with mic as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source)

                transcription = recognizer.recognize_google(audio)

                if not mic_muted:
                    print('You: ' + transcription)
                    output = model.generate(transcription, max_tokens=200)
                    print('GPT4All: ', output)
                    speak(output)

                if wake_word in transcription.lower():
                    start_transcription()
                elif "mute" in transcription.lower() or "stop talking" in transcription.lower():
                    stop_transcription()
                elif "go to sleep" in transcription.lower():
                    print("Application is going to sleep.")
                    sys.exit()
                

            except sr.UnknownValueError:
                print("Sorry, I could not understand what you said.")

            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

def speak(text):
    global mic_muted

    if sys.platform == 'darwin':
        ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,?!-_$:+-/ ")
        clean_text = ''.join(c for c in text if c in ALLOWED_CHARS)
        system(f"say '{clean_text}'")
    else:
        engine.setProperty('rate', 160)
        engine.setProperty('volume', 0.9)
        engine.setProperty('voice', voices[1].id)

        if not mic_muted:
            turn_off_microphone()
            engine.say(text)
            engine.runAndWait()
            turn_on_microphone()

def turn_on_microphone():
    global mic_muted
    mic_muted = False

def turn_off_microphone():
    global mic_muted
    mic_muted = True

def start_transcription():
    global transcribing
    transcribing = True
    turn_on_microphone()
    
    print("Listening...")
    speak("Hi... I am listening.")

def stop_transcription():
    global transcribing
    transcribing = False
    turn_off_microphone()

    print("Microphone is on mute!")

def main():
    recognize_speech()

if __name__ == "__main__":
    main()
