import pyaudio
import speech_recognition as sr
import cleverbotfreeapi
import os

def find_default_audio_devices():
    audio = pyaudio.PyAudio()
    input_device_index = None
    output_device_index = None

    for i in range(audio.get_device_count()):
        info = audio.get_device_info_by_index(i)
        if info['maxInputChannels'] > 0 and input_device_index is None:
            input_device_index = i
        if info['maxOutputChannels'] > 0 and output_device_index is None:
            output_device_index = i

    return input_device_index, output_device_index

def main():
    recognizer = sr.Recognizer()

    # Find default audio input and output devices
    microphone_device_index, speaker_device_index = find_default_audio_devices()

    if microphone_device_index is None:
        print("No microphone input device found.")
        return

    if speaker_device_index is None:
        print("No speaker output device found.")
        return

    while True:
        audio = None
        try:
            audio_input = input("Press Enter to start recording...")
            if audio_input == "":
                p = pyaudio.PyAudio()
                stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True,
                                input_device_index=microphone_device_index, frames_per_buffer=1024)
                print("Recording... (Press Enter to stop)")

                frames = []
                while True:
                    try:
                        audio_chunk = stream.read(1024)
                        frames.append(audio_chunk)
                    except KeyboardInterrupt:
                        print("Stopped recording.")
                        break

                stream.stop_stream()
                stream.close()
                p.terminate()

                audio = b''.join(frames)
        except KeyboardInterrupt:
            break

        if audio:
            try:
                inp = recognizer.recognize_google(audio)
                print("You >> " + inp)

                out = cleverbotfreeapi.cleverbot(inp, session="Deftera")
                print("Felicia >> " + out)

                os.system(f"termux-tts-speak -d {speaker_device_index} '{out}'")
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

if __name__ == "__main__":
    main()
