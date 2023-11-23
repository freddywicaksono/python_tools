from gtts import gTTS 
from playsound import playsound

mytext = 'Selamat Belajar Python!'
language = 'id'
myobj = gTTS(text=mytext, lang=language, slow=False) 

myobj.save("selamat_datang.mp3") 
playsound("selamat_datang.mp3", True)
