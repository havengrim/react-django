from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        members_list = Member.objects.filter(
            fname__contains=search_query
        ) | Member.objects.filter(
            lname__contains=search_query
        ) | Member.objects.filter(
            email__contains=search_query
        )
    else:
        members_list = Member.objects.all()
    
    total_members = members_list.count()
    paginator = Paginator(members_list, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'home.html', {
        'page_obj': page_obj,
        'total_members': total_members,
        'search_query': search_query
    })

def join(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        age = request.POST['age']
        email = request.POST['email']
        passwd = request.POST['passwd']
        is_active = request.POST['is_active'] == 'true'

        member = Member(fname=fname, lname=lname, age=age, email=email, passwd=passwd, is_active=is_active)
        member.save()

        return redirect('home')

    return render(request, 'join.html')

def edit(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        member.fname = request.POST.get('fname')
        member.lname = request.POST.get('lname')
        member.age = request.POST.get('age')
        member.email = request.POST.get('email')
        member.passwd = request.POST.get('passwd')
        member.is_active = request.POST.get('is_active') == 'true'

        member.save()
        messages.success(request, 'Your Form Has Been Updated!')
        return redirect('home')
    else:
        return render(request, 'edit.html', {'member': member})
    
def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        member.delete()
        messages.success(request, 'Member has been deleted!')
        return redirect('home')
    return redirect('home')



