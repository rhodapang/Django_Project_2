from django.shortcuts import render 

posts = [
    {
        'author':'Rhoda',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'data_post': 'August 27, 2018'
    },
     {
        'author':'Asaph',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'data_post': 'August 26, 2018'
    }

]


def home(request):
    context = {
        'posts': posts 
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
