from gtts import gTTS 

def text_to_speech(text, language='en', output_file='.\\temp\\output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)

if __name__ == '__main__':
    try:
        with open('.\\temp\\content.txt', 'r', encoding='utf-8') as f:
            text = f.read()
        text_to_speech(text, output_file='output.mp3')
    except FileNotFoundError:
        print("Error: Text file not found!")
    except Exception as e:
        print(f"An error occurred: {e}")
