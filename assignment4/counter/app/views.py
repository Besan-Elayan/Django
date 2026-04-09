from django.shortcuts import render, redirect


def index(request):

    if 'counter' in request.session:
        request.session['counter'] += 1       
        print('key exists!')
    else:
        request.session['counter'] = 1
        print("key 'key_name' does NOT exist")
    return render(request,'app/index.html', {'counter': request.session['counter']})



def destroy_session(request):
    if 'counter' in request.session:

        del request.session ['counter']
    return redirect ('/')
