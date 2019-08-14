from django.shortcuts import render
from django.http import HttpResponse
import re
# Create your views here.



def upload(request):
    if request.method == "POST":
        file_upload = list(request.FILES.items())
        file_upload = file_upload[0][1]
        file_upload.name = "he.txt"
        request.session["file"] = str(file_upload.read())
        request.session["order"] = request.POST['order']
        return render(request, 'tools/form.html', {'form': "123", })
    else:
        file_upload = ""
        return render(request, 'tools/form.html', {'form': "123", })
#
def result(request, order='order'):
    file_upload = request.session["file"]
    order = request.session["order"]
    pattern = re.compile("\s+")
    file_upload = file_upload.split("\\r\\n")[10]
    text_extract = re.split("\s+", file_upload)
    # print(type(text_extract), len(text_extract))
    # print(type(file_upload[0]))
    text_extract = text_extract[2:]
    if order == 'reverse':
        text_extract = "<br>".join(text_extract[::-1])
    else:
        text_extract = "<br>".join(text_extract)

    return HttpResponse(text_extract)
    # if request.method == 'POST':
    #     return HttpResponse(file_upload)
