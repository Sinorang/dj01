from django.shortcuts import render, redirect
import googletrans
from django.contrib import messages
from gtts import gTTS
from random import sample

# Create your views here.
def make():
    l = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    st = ""
    for i in range(10):
        st += sample(l, 1)[0]
    return st

def index(request):
    b = request.GET.get("bf", "")
    
    context = {
        "dic" : googletrans.LANGUAGES,
        "fr" : "en",
        "to" : "ko"
    }

    if b:
        f = request.GET.get("fr", "")
        t = request.GET.get("to", "")
        tr = googletrans.Translator()
        result = tr.translate(b, src=f, dest=t)
        messages.info(request, "번역이 완료되었습니다")

        tts = gTTS(result.text, lang=t)
        filename = make()
        tts.save(f'media/tts/{filename}.mp3')

        context.update({
            "af" : result.text,
            "bf" : b,
            "fr" : f,
            "to" : t,
            "fn" : filename
        })

    return render(request, "trans/index.html", context)

def reset(request):
    return redirect('trans:index')