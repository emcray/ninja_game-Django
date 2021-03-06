from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

# helper dictionary, for easy access to min/max gold values
GOLD_MAP = {
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (0,50)
}

def gold_home(request):
    if not "gold" in request.session or "activities" not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    return render(request, "gold_home.html")

def process(request):
    if request.POST['location'] == 'farm':
        earned_gold = random.randint(10, 20)
        request.session['gold'] += earned_gold
        message = f'You earned {earned_gold} coins from the Farm! {strftime ("%Y-%m-%d %H:%M %p", gmtime())}'
        request.session['activities'].append(message)
    if request.POST['location'] == "cave":
        earned_gold = random.randint(5, 10)
        request.session['gold'] += earned_gold
        message = f'You earned {earned_gold} coins from the Cave! {strftime ("%Y-%m-%d %H:%M %p", gmtime())}'
        request.session['activities'].append(message)
    if request.POST['location'] == 'house':
        earned_gold = random.randint(2, 5)
        request.session['gold'] += earned_gold
        message = f'You earned {earned_gold} coins from the House! {strftime ("%Y-%m-%d %H:%M %p", gmtime())}'
        request.session['activities'].append(message)
    if request.POST['location'] == "casino":
        earned_gold = random.randint(0, 50)
        request.session['gold'] += earned_gold
        message = f'You earned {earned_gold} coins from the Casino! {strftime ("%Y-%m-%d %H:%M %p", gmtime())}'
        request.session['activities'].append(message)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')
