from django.shortcuts import render
from datetime import datetime, timedelta
import random
# Create your views here.
def main(request):
    '''This is where the main page is processed'''
    template_name = "restaurant/main.html"

    context = {
        "image" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTg8JmHD1np7oKTaSAptIAWPVPVR4wA11TIww&s"
    }

    return render(request, template_name, context)

def order(request):
    '''This is where the order page is processed, holds the form'''
    template_name = "restaurant/order.html"
    
    return render(request, template_name)

def submit(request):
    '''This is where the form request is processed'''
    template_name = "restaurant/confirmation.html"

    # Checking if the Post Request is being used
    if request.POST:
        price = 10
        item1 = ""
        item2 = ""
        item3 = ""
        item4 = ""
        special_sauce = ""
        # Reading data from the post Request
        if (request.POST.get("item1", False) == "on"):
            price += 7
            item1 = "Tony's Big Sausage"
        if (request.POST.get("item2", False) == "on"):
            price += 2
            item2 = "Crying Tony's Onions"
        if (request.POST.get("item3", False) == "on"):
            price += 4
            item3 = "Spicyony Pepperoni"
        if (request.POST.get("item4", False) == "on"):
            price += 30
            item4 = "Tony's pig feet"
        if (request.POST.get("special_sauce", False) == "on"):
            price += 3
            special_sauce = "Spicy Barbecue"
        print(price)
        time = datetime.now() + timedelta(minutes=random.randrange(30, 61))
        special_instruction = request.POST["special_instruction"]
        name = request.POST["name"]
        phone = request.POST["phone"]
        email = request.POST["email"]

        context =  {
            "item1" : item1,
            "item2" : item2,
            "item3" : item3,
            "item4" : item4,
            "special_sauce" : special_sauce,
            "time" : time,
            "special_instruction" : special_instruction,
            "price" : price,
            "name" : name,
            "phone" : phone,
            "email" : email,

        }

    return render(request, template_name, context)