from django.shortcuts import render
# from django.http import HttpResponse, HttpRequest
import random, datetime

quotesList = [
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.",
    "If you can't explain it to a six year old, you don't understand it yourself."
]

imageList = [
    "https://upload.wikimedia.org/wikipedia/commons/3/3e/Einstein_1921_by_F_Schmutzer_-_restoration.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Albert_Einstein_sticks_his_tongue.jpg/250px-Albert_Einstein_sticks_his_tongue.jpg",
    "https://images.newscientist.com/wp-content/uploads/2019/06/18142824/einstein.jpg"
]

def quote(request):

    template_name = 'quotes/quote.html'

    random_quote = random.choice(quotesList)
    random_image = random.choice(imageList)

    context = {
        'quote': random_quote,
        'image': random_image,
        'current_time': datetime.datetime.now(),
    }

    return render(request, template_name, context)


def show_all(request):

    context = {
        'quote1': quotesList[0],
        'quote2': quotesList[1],
        'quote3': quotesList[2],

        'image1': imageList[0],
        'image2': imageList[1],
        'image3': imageList[2],

        'current_time': datetime.datetime.now(),
    }

    return render(request, 'quotes/show_all.html', context)


def about(request):

    template_name = 'quotes/about.html'

    context = {
        'current_time' : datetime.datetime.now(),
    }

    return render(request, template_name, context)