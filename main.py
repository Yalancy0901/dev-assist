# main.py

from voice_ip import listen
from voice_op import speak
from command_handle import handle_command

def main():
    speak("Hola guysss! I am your voice assistant for development tasks.")
    
    while True:
        try:
            command = listen()
            if not command:
                speak("Sorry, I didn't catch that.")
                continue

            if "exit" in command or "quit" in command:
                speak("Bye! Thanks for using me Hehehee.")
                break

            response = handle_command(command)
            speak(response)

        except KeyboardInterrupt:
            speak("Assistant terminated.")
            break
        except Exception as e:
            speak(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
