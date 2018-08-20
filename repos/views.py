
from django.shortcuts import render,redirect
from .forms import APIform
from django.http import HttpResponse
import requests
import json
from django.views.generic.base import TemplateView

def usersearch(request):
	if request.method=='GET':
		form=APIform()
		return render(request,'view.html',{'form':form})
	if request.method=='POST':
		form=APIform(request.POST)
		if form.is_valid():
			git_username=form.cleaned_data.get('g_username')
			r=requests.get("https://api.github.com/users/%s"%git_username)
			r1=requests.get("https://api.github.com/users/%s/repos"%git_username)
			repo=r1.json()
			repo1=[]

			for repos in repo:
				if isinstance(repos,dict):
					repo1.append((repos["name"],repos["language"]))
					s=requests.get("https://api.github.com/repos/%s/%s/commits"%(git_username,repos["name"]))
					s1=s.json()
					print(s1)

			if r.status_code==200:
				found=True
			else:
				found=False
			request.session['git_username']=git_username
			request.session['repo']=repo
			return render(request,'view.html',{'form':form,'git_username':git_username,'found':found,'repo':repo1})


	else:
		form=APIform()
	return render(request,'templates/View.html',{'form':form})


def repos(request,reponame):
	git_user=request.session['git_username']
	print (git_user)
	r1=requests.get("https://api.github.com/repos/%s/%s/commits"%(git_user,reponame))
	repo=r1.json()
	print(repo)
	s2=[]
	for keys in repo:
		s2.append(keys["commit"]["committer"]["date"])
	return render(request,'repo.html',{'dict':s2,'git_username':git_user,'reponame':reponame})
# Create your views here.
