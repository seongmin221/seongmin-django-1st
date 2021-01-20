from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members
# Create your views here.

def index(req):
    print(dir(req))
    return HttpResponse("hello world")

def test(req):
    return HttpResponse("<h2>Test</h2>")

def signup(req):
    if req.method == 'POST':

        username = req.POST['username']
        email = req.POST['email']
       # if username == 'exit':
        #    return HttpResponse("나가기")
       # elif username=='codigon':
        #    return render(req,'login.html')
        member = Members(
                username = username,
                useremail = email
        )

        member.save()

        res_data = {}
        res_data['res'] = '등록됨'

        return render(req, 'index.html', res_data)

    return render(req, 'index.html')

    def git(req):
        return HttpResponse("<h2>git version</h2>")