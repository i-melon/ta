
from django.shortcuts import render
from .models import Market
from .forms import MarketForm
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from django.db.models import Q




def smart_search(String):
    # stop_words = set(stopwords.words("russian")) # Замените 'english' на соответствующий язык
    #
    # # Токенизация запроса
    # tokens = word_tokenize(query)
    #
    # # Удаление стоп-слов из запроса
    # tokens = [token for token in tokens if token.lower() not in stop_words]
    #
    # # Построение Q-объекта Django для поиска
    # q_objects = Q()
    # for token in tokens:
    #     q_objects |= Q(description__icontains=token)

    # Выполнение поиска и возврат результатов
    # results = Market.objects.filter(q_objects)
    results = []
    initialList = Market.objects.all()
    for el in initialList:
        x = el.description.split(', ')
        for i in x:
            if String == i:
                results.append(el)
    print(results)
    return results

def index(request):
    form = MarketForm()
    results = None
    error = ''

    if request.method == 'POST':
        form = MarketForm(request.POST)

        if form.is_valid():
            search_query = form.cleaned_data['description']
            print(search_query)
            results = smart_search(search_query)
        else:
            error = 'rooot'

    context = {
        'error': error,
        'form': form,
        'results': results
    }
    return render(request, 'analizer/index.html', context)

# Create your views here.
# def index(request):
#     markets = Market.objects.all()
#     form = MarketForm()
#     data = {
#         'markets': markets,
#         'form': form,
#     }
#     return render(request, 'analizer/index.html', data)