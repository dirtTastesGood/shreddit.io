import json
from django.shortcuts import render, redirect
from django.contrib import messages
from chord_progressions.models import ChordProgression
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist



def home(request):
    # messages.info(request, 'Welcome to the home page')
    return render(request, 'pages/home.html')

def explore(request, id):
    if id != 0:
        try:
            progression = ChordProgression.objects.get(id=id)
            
            if request.user == progression.creator:

                context = {
                    'loaded_progression_id': id,
                    'loaded_progression'   : progression.progression,
                    'chord_scale_objects'  : progression,
                    'path'                 : request.path_info.split('/')[1]
                }
                if len(messages.get_messages(request)) == 0:
                    messages.success(request, 'Progression loaded!')
            else:
                messages.error(request, "You can only edit progressions you've created. Try again.")
                context = {
                    'path'       : request.path_info.split('/')[1]
                }
            

        except ObjectDoesNotExist:
            print(f"loaded progression: {request.path_info.split('/')}")

            messages.warning(request, 'Progression does not exist. Try again.')
            context = {
                'path': request.path_info.split('/')[1]
            }

        return render(request, 'pages/explore.html', context)

    else:
        print(f"loaded progression: {request.path_info.split('/')}")


        context = {
                'path': request.path_info.split('/')[1]
        }
    
    return render(request, 'pages/explore.html', context)
