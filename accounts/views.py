from django.shortcuts import render, redirect
from django.contrib.auth import logout

def logout_view(request):
    active_path = request.session['active_path']
    logout(request)
    return redirect("post_list", path=active_path)
