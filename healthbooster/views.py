from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from healthbooster.models import Person, City
from healthbooster.forms import PersonForm

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            a = Person(first_name=form.cleaned_data["first_name"],
                       last_name=form.cleaned_data["last_name"],
                       email=form.cleaned_data["email"])
            a.save()
            return HttpResponseRedirect('/people/')
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

def all_authors(request):
    investors_list = Person.objects.all()
    return render(request, "people.html", {'investors_list': investors_list})

def author_search(request):
    result_set = Person.objects.filter(email__contains='boun.edu.tr', last_name__contains= 'G')
    return HttpResponse(result_set)

def search_form(request):
    return render(request, "search_form.html")

def search(request):
    errors = []
    if request.GET['q']:
        q = request.GET['q']
        print('query', q)
        if len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = City.objects.filter(title__icontains=q)
            return render(request, 'search_results.html', {'books': books, 'query': q})
    else:
        errors.append('Enter a city.')

    return render(request, 'search_form.html', {'errors': errors})
