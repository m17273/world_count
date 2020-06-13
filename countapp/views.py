from django.shortcuts import render
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, "about.html")

def count(request):
    return render(request, "count.html")
def count(request):
    entered_text = request.GET['fulltext']
    word_list = entered_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'count.html', {'alltext':entered_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})