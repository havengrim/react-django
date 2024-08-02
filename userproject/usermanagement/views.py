from django.shortcuts import render, redirect, get_object_or_404
from .models import Member
from .forms import MemberForm
from django.contrib import messages

def home(request):
    all_members = Member.objects.all()
    return render(request, 'home.html', {'all': all_members})

def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Form Has Been Submitted!')
            return redirect('home')
    else:
        form = MemberForm()
    return render(request, 'join.html', {'form': form})

def edit(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Form Has Been Updated!')
            return redirect('home')
    else:
        form = MemberForm(instance=member)
        return render(request, 'edit.html', {'form': form, 'member': member})
    
def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        member.delete()
        messages.success(request, 'Member has been deleted!')
        return redirect('home')
    return redirect('home')
