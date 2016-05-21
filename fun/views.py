from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request, 'fun/post_list.html', {})