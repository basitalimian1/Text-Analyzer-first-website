# I have created this file -- Basit ali
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # global params
    text = request. POST.get('analyze', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    upercase = request.POST.get('upercase', 'off')
    newline = request.POST.get('newlineremover', 'off')
    extra_space = request.POST.get('extra_space_remover', 'off')
    char_count = request.POST.get('count_char', 'off')
    orignal_text = text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ''

    # Removeing puncs
    if removepunc == 'on':
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {"porpuse": 'Remove punctuations', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)

    # Converting into upper case
    if upercase == 'on':
        analyzed = text.upper()
        params = {"porpuse": 'Remove punctuations', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)

    # Removing new line
    if newline == 'on':
        analyzed = ''
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {"porpuse": 'Remove punctuations', 'analyzed_text': analyzed}
        text = analyzed
        # return render(request, 'analyze.html', params)

    # Removing extra space

    if extra_space == 'on':
        analyzed = ""
        for indx, char in enumerate(text):
            if not (text[indx] == " " and text[indx + 1] == " "):
                analyzed = analyzed + char
        params = {"porpuse": 'Remove punctuations', 'analyzed_text': analyzed}
    elif char_count == 'on':
        analyzed = f"Total chars are : {len(orignal_text)}"
        params = {"porpuse": 'Remove punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    return render(request, 'analyze.html', params)

    # Counting chars

