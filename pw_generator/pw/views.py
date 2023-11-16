import random
from django.shortcuts import render

def pw_struct(request):
    
    return render(request, 'pw_form.html')

def pw(request):

    if request.method == 'POST':

    #pw_list
        pw_list = list('abcdefghijklmnopqrstuvwxyz')

    #new_pw
        new_pw = ' '

    #pw_length
        length = int(request.POST.get('pw_length', '8'))

    #upper
        upper = request.POST.get('upper')

        if upper:
            pw_list.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    #numbers
        numbers = request.POST.get('numbers')

        if numbers:
            pw_list.extend("1234567890")

    #special
        special = request.POST.get('special', ' ')

        if special:
            pw_list.extend('~_!@#$%^&*?')


        for i in range(length):
            new_pw += random.choice(pw_list)
       

    return render(request, 'pw.html', {'new_pw': new_pw, 'length': length, 'upper': upper, 'numbers':numbers, 'special': special})
