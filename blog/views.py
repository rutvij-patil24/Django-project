from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post

# dummy data (list of dictionaries)
# posts = [

# 	{
# 		'author':'Rutvij Patil',
# 		'title':'My First Blog',
# 		'content':'In this blog I will be talking about Wordpress',
# 		'date_posted':'February 24, 2020'
# 	},
# 	{
# 		'author':'Rick Sanchez',
# 		'title':'Impact of 5G on humans',
# 		'content':'In this blog I will be talking about 5G',
# 		'date_posted':'March 1, 2020'
# 	}

# ]


def home(request):
	# return HttpResponse('<h1>Blog Home</h1>')

	# context = {
	# 	'posts':posts
	# } # assigned list of posts as value to the key 'posts'

	context = {
		'posts': Post.objects.all()
	}

	return render(request,'blog/home.html',context)
	# render function returns http response


def about(request):
	# return HttpResponse('<h1>About this Blog Website</h1>')
	return render(request,'blog/about.html',{'title':'About'})

