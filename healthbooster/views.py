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

def all_people(request):
    people_list = Person.objects.all()
    return render(request, "people.html", {'people_list': people_list})

def people_search(request):
    result_set = Person.objects.filter(first_name__contains='a').filter(last_name__contains='a')
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
            cities = City.objects.filter(name__icontains=q)
            return render(request, 'search_results.html', {'cities': cities, 'query': q})
    else:
        errors.append('Enter a city.')

    return render(request, 'search_form.html', {'errors': errors})
