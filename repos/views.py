
from django.shortcuts import render,redirect
from .forms import git_userform
from django.http import HttpResponse
import requests
import json
from django.views.generic.base import TemplateView

def reposearch(request):
	if request.method=='GET':
		form=git_userform()
		return render(request,'view.html',{'form':form})
	if request.method=='POST':
		form=git_userform(request.POST)
		if form.is_valid():
			git_username=form.cleaned_data.get('g_username')
			user=requests.get("https://api.github.com/users/%s"%git_username)
			user1=requests.get("https://api.github.com/users/%s/repos"%git_username)
			repo=user1.json()
			repo1=[]

			for repos in repo:
				if isinstance(repos,dict):
					repo1.append((repos["name"],repos["language"]))
			if user.status_code==200:
				found=True
			else:
				found=False
			request.session['git_username']=git_username
			return render(request,'view.html',{'form':form,'git_username':git_username,'found':found,'repo':repo1})


	else:
		form=git_userform()
	return render(request,'view.html',{'form':form})


def commithist(request,reponame):
	git_user=request.session['git_username']
	histreq=requests.get("https://api.github.com/repos/%s/%s/commits"%(git_user,reponame))
	repohist=histreq.json()
	history=[]
	for keys in repohist:
		history.append(keys["commit"]["committer"]["date"])
	return render(request,'repo.html',{'dict':history,'git_username':git_user,'reponame':reponame})
# Create your views here.
