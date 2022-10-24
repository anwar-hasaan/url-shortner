from django.contrib.auth.base_user import BaseUserManager
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import URL

def home(request):
    if request.method == 'POST':
        given_url = request.POST.get('main_url')
        try:
            for i in range(0, 5):
                random_chars = BaseUserManager().make_random_password(5)
                all_url = URL.objects.filter(short_url=random_chars).first()
                if not all_url:
                    url = URL.objects.create(url=given_url, short_url=random_chars)
                    url.save()
                    messages.success(request, "Short URL created")
                
                    current_url = str(request.build_absolute_uri())
                    link = str(current_url) + str(random_chars)
                    short_url = link.split('//')[1]
                    return render(request, 'home.html', {'main_url': given_url, 'short_url': short_url, 'url': random_chars,})
                    break # break of for loop
        except Exception as e:
            messages.error(request, 'Something went worng: ' + str(e))
    return render(request, 'home.html')

def redirect_to_orginal_url(request, url):
    all_url = URL.objects.filter(short_url=url).first()
    if all_url:
        actual_url = all_url.url
        return redirect(actual_url)
    else:
        messages.error(request, 'Wrong URL')
        return redirect('/')