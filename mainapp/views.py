from django.shortcuts import render, redirect
# import datetime
from datetime import datetime, timedelta
from .models import Team
from django import forms
# Create your views here.


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name', 'image_path', 'end_time',
                  'description', 'author', ]


def get_index(request):
    return render(request, 'index.html')


def get_initiate(request):
    date = datetime.now() + timedelta(days=1)
    setDate = (date).strftime("%Y-%m-%dT%H:%M:%S")
    return render(request, 'initiate.html', locals())


def post_initiate(request):
    team_name = request.POST['team_name']
    image_path = request.POST['image_path']
    description = request.POST['description']
    author = request.POST['author']
    end_time = request.POST['end_time'].replace("T", " ")
    # print('end_time', end_time)

    data = {'team_name': team_name,
            'image_path': image_path,
            'description': description,
            'end_time': end_time,
            'author': author}

    form = TeamForm(data)

    if form.is_valid():
        form.save()
        # print('新增的recipe: ' + new_recipe)
        return redirect('/index')
    else:
        return redirect('/initiate')
