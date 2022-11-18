from django.shortcuts import render

def main_info(request):
    name = 'Rekruto'
    message = 'Давай дружить'
    return render(request, 'first_page.html',{'name': name, 'message': message})

def greetings(request):
    greet = request.GET['message']
    return render(request, 'second_page.html', {'message': greet})
