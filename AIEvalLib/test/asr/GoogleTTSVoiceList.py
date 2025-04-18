# -*- coding: utf-8 -*-

from GlobalUtil import get_client_ai_voice_ggc


def list_voices():
    """Lists the available voices."""
    client = get_client_ai_voice_ggc()

    # Performs the list voices request
    voices = client.list_voices()

    print(f"len(voices.voices) : {len(voices.voices)} \n\n")

    for voice in voices.voices:
        # Display the voice's name. Example: tpc-vocoded
        print(f"Name: {voice.name}")

if __name__ == "__main__":
    list_voices()