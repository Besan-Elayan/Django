
from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%b %d, %Y ", gmtime()),
        "date": strftime(" %H:%M %p", gmtime())
    }
    return render(request,'time_display/index.html', context)


