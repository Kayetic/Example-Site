import whisper

model = whisper.load_model("base")

result = model.transcribe("audio.mp3")
print(result["text"])


with open("transcription-polska.txt", "w") as f:
    f.write(result["text"])
    f.close()

# upload the transcription to your google drive
