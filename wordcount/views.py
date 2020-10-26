from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html', {'hiClaire': 'We are doing great today!'})

#NOTE: New Page creation
def about(request):
    return render(request, 'about.html')

def  eggs(request):
    return HttpResponse('Eggs are delicious. I own a poultry')


def agriculture(request):
    return HttpResponse('<h1>Agriculture is our backbone</h1>')

def cominsud(request):
    return HttpResponse('Community Initatice for Sustainable Development has a head office at Ntarinkon')


def mycountry(request):
    return HttpResponse('My Country is beautiful')


def count(request):
    return render(request, 'count.html')


#Lesson is Coounting the words

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist)})

"The following code using a dictionary is to actually count frequency of words in a submited text"
"That is, to get which words appear the most"
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase:
            worddictionary[word] += 1

        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)


    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist), 'sortedwords':sortedwords})
