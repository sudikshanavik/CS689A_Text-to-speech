from Utilities import tts

if __name__ == "__main__":
	text = input("Enter the text to be converted: ")
	

	for i in text:
		print(i)

	tts.text_to_speech(text, debug=True, use_pronunciation_dict=True)