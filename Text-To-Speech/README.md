Computational Linguistics for Indian Languages (CS689A)

**Text-To-Speech for Hindi Language**
This is a Concatenative Text-to-Speech system implemented in Python.

It is a part of course-work project for the course **Computational Linguistics for Indian Languages**

A concatenative text-to-speech system that creates an audio representation of text by pasting together a bunch of small audio files to form the whole of the output.

There are three steps, including:

***1. Text-to-words**: In this step, raw input text is tokenized into a list of words. This will also generally include converting numerical digits into their word equivalents (ex: turn "6" into "six").

***2. Words-to-phonemes**: In this step, the array of words is converted into phonemes. Phonemes are the individual sounds in a language. As Hindi has a pretty vast phonetic genre, the  hindi alphabetic pronunciation can vary change the pronunciation of the whole word. The system has already mapped the hindi phonetic sounds to their alphabets, so whenever the alphabet is detected, the system just maps to its audio file and return its number. The output is an list of numbers that each correspond to one of the 44 hindi phonemes.

***3. Phonemes-to-sounds**: Finally, each phoneme is paired with an audio file. This is the point where the actual audio is stitched together. It would also be in this step that the correct voice for the audio is selected, assuming multiple voices are supported.

**Dependencies**
This project relies on 
* Python 3x.
* re (for tokenization)
* wave and os (for stiching together the audio files)

**Installations**
Following are the steps to install the speech-synthesizer out:

1. Make sure that all dependencies are installed.
2. Navigate to the particular directory.
3. Run: `pip install -r requirements.txt`
4. Run the command `python3 SpeechSynthesis.py`
5. Will be prompted to input a message. Enter the text to be converted to speech.
6. The program will generate the output as a .wav file and end. Open speech.wav to  hear the result.


