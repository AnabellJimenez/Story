from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from post.models import Post, Comment, Gallery
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from django_boto.s3 import upload



# Create your views here.
@login_required(login_url = login)
def post(request):
	return render(request, "post/new.html", {})

@login_required(login_url = login)
def create(request):
	new_post = Post()
	new_post.post_title = request.POST["post_title"]
	new_post.post_text = request.POST["post_text"]
	new_post.user = request.user
	new_post.save()

	return HttpResponseRedirect(reverse('post:show', args=(new_post.id,)))

@login_required(login_url = login)
def show(request, post_id):
	try: 
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404("Post Does Not Exist")
	return render(request, 'post/show.html', {'post': post, 'post_id': post_id})

@login_required(login_url = login)
def comment(request, post_id):

	post = Post.objects.get(pk=post_id)
	new_comment = request.POST["comment_text"]
	user = request.user
	post.comment_set.create(comment_text = new_comment, user = user)

	return render(request, 'post/show.html', {'post': post})

@login_required(login_url = login)
def list(request):

	lista = Post.objects.all()
	user = request.user
	post_list = lista.filter(user = user)


	return render(request, 'post/list.html', {'post': post_list})

@login_required(login_url = login)
def feed(request):

	post_list = Post.objects.all()

	return render(request, 'post/list.html', {'post': post_list})

@login_required(login_url = login)
def delete_comment(request, comment_id):
	print comment_id

	del_comment = Comment.objects.get(pk = comment_id)
	new_post = del_comment.post
	print "\n COMMENT: ", del_comment, "\n"
	print "\n post: ", new_post, "\n"
	print "\n post id: ", new_post.id, "\n"
	Comment.delete(del_comment)
	
	return HttpResponseRedirect(reverse('post:show', args=(new_post.id,)))
	
@login_required(login_url = login)
def delete_post(request, post_id):
	print post_id
	del_post = Post.objects.get(pk = post_id)
	Post.delete(del_post)
	for i in Post.objects.all():
		print i.id

	lista = Post.objects.all()
	user = request.user
	post_list = lista.filter(user = user)

	photo = Gallery.filter(post = del_post)
	print photo


	return render(request, 'post/list.html', {'post': post_list})

# @login_required(login_url = login)
# def pic(request):
# 	return render(request,'post/upload.html')

@login_required(login_url = login)
def upload_file(request, post_id):
	# print post_id
	if request.method == 'POST':
		# print "Upload"
		# print request.POST
		# print request.FILES
		form = UploadFileForm(request.POST, request.FILES)
		# print "finish3"
		# print type(request.FILES['file'])

		# print form.is_valid()
		if form.is_valid():
			print "form valid"
			print request.FILES['file']
			print upload(request.FILES['file'])
			pic = Gallery()
			pic.name = request.FILES['file']
			pic.pic_url = upload(request.FILES['file'])
			pic.user = request.user
			pic.post = Post.objects.get(pk = post_id)
			pic.save()
#        	handle_uploaded_file(request.FILES['file'])
        #     return HttpResponseRedirect('/success/url/')
		return HttpResponseRedirect(reverse('post:gallery'))
	else:
		form = UploadFileForm()
	return render(request,'post/upload.html', {'form': form, "post_id": post_id})

@login_required(login_url = login)
def gallery(request):
	pics_list = []
	for pics in Gallery.objects.all():
		print pics.id
		pics_list.append([pics.pic_url, pics.post.id])

	return render(request, 'post/gallery.html', {'pics_list': pics_list})

def user_profile(request):
	
	pics_list = Gallery.objects.all()
	user_list = pics_list.filter(user = request.user)
	pics = []
	post_id = []

	for photo in user_list:
		pics.append([photo.pic_url,photo.post.id])

	print pics
	return render(request, 'post/profile.html', { 'pics': pics })


@login_required(login_url = login)
def add_list(request):
	return HttpResponse("Add to List")