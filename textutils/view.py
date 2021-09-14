from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	# get the text
	djText = request.POST.get('text','default')
	# Analyse the text
	return render(request,'index.html')

def analyze(request):
	# Get the Text 
	djText = request.POST.get('text','default')
	removepunc = request.POST.get('removepunc','off')
	fullupper = request.POST.get('fullupper','off')
	fulllower = request.POST.get('fulllower','off')
	newlinermover = request.POST.get('newlineremover','off')
	spaceremover = request.POST.get('extraspaceremover','off')
	charcount = request.POST.get('charcount','off')

	if removepunc == 'on':
		punctiations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		analyzed = ""
		for char in djText:
			if char not in punctiations:
				analyzed = analyzed + char
		params = {'purpose': 'Remove Punctuations','analyzed_text':analyzed}
		djText = analyzed
		# return render(request,'analyze.html',params)

	if fullupper == 'on':
		analyzed = ""
		for char in djText:
			analyzed = analyzed + char.upper()
		params = {'purpose': 'Convert to Upper Case','analyzed_text':analyzed}
		djText = analyzed
		# return render(request,'analyze.html',params)

	if fulllower == 'on':
		analyzed = ""
		for char in djText:
			analyzed = analyzed + char.lower()
		params = {'purpose': 'Convert to Lower Case','analyzed_text':analyzed}
		djText = analyzed
		# return render(request,'analyze.html',params)
		
	if newlinermover == 'on':
		analyzed = ""
		for char in djText:
			if char !='\n' and char !='\r'	:
				analyzed = analyzed + char
		params = {'purpose': 'New Line Remover','analyzed_text':analyzed}
		djText = analyzed
		# return render(request,'analyze.html',params)

	if spaceremover == 'on':
		analyzed = ""
		for index,char in enumerate(djText):
			if djText[index] == " " and djText[index+1] == " ":
				pass
			else:
				analyzed = analyzed + char
			
		params = {'purpose': 'Extra Space Remover','analyzed_text':analyzed}
		djText = analyzed
		# return render(request,'analyze.html',params)
		
	if charcount == 'on':
		counter = 1
		for char in djText:
			counter = counter + 1
		params = {'purpose': 'Total Characters','analyzed_text':counter}
		# djText = analyzed
		# return render(request,'analyze.html',params)

	if(removepunc != "on" and fullupper != "on" and fulllower != "on" and newlinermover != "on" and spaceremover != "on" and charcount != "on"):
		# return HttpResponse("Error")
		return render(request,'Error.html')

	return render(request,'analyze.html',params)