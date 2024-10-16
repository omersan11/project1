from django.shortcuts import render

# Create your views here.

def home(request):
    received_text = None

    if request.method == "POST":
        received_text = request.POST.get('text_input')  # Formdan gelen veriyi al

    return render(request, 'home.html', {'received_text': received_text})