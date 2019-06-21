from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
from .forms import Post_form
from user_profile.models import education, UserSkill

# Create your views here.
def home(request):
    user= request.user
    userEducation = education.objects.filter(user=request.user)
    userSkill = UserSkill.objects.filter(user=request.user)
    # pagination
    Post_list = Post.objects.all().order_by("id")
    paginator = Paginator(Post_list, 4)  # Show 25 contacts per page

    page = request.GET.get('page')
    post = paginator.get_page(page)

    context = {
        'user': user,
        'education': userEducation,
        'skills': userSkill,
        'posts': post
    }
    return render(request,'nuces_circle/home.html', context)



def postForm_view(request): # for posting
    form = Post_form(request.POST or None)
    if form.is_valid():
        form.save(user=request.user, commit=False)

    context = {
        'form': form
    }
    return render(request, 'nuces_circle/posts.html', context)


def logout(request):
    if request.method == 'POST':
       auth.logout(request)
       return render(request, 'accounts/login.html')