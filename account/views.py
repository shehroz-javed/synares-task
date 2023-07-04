from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserRegisterSerializer, UserLoginSerializer,  WebLinkSerializer
from .utils import get_tokens_for_user
from .models import WebLinks, Linkcount


class Register(APIView):

    def post(self, request):

        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg": "user registerd successfully"},  status=status.HTTP_201_CREATED)


class Login(APIView):

    def post(self, request):

        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({"msg": "Login successful", "token": token}, status=status.HTTP_200_OK)
            else:
                return Response({"msg": "Email and Password does not match"}, status=status.HTTP_400_BAD_REQUEST)


class AddLink(APIView):

    def post(self, request):
        serializer = WebLinkSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"msg": "url add suceesfully"}, status=status.HTTP_201_CREATED)


def login_t(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('logint')
    return render(request, 'login.html')


@login_required(login_url="/account/logint/")
def home(request):
    links = WebLinks.objects.all()
    data = {
        'links': links
    }

    return render(request, 'home.html', data)


def update_view_count(request, pk):

    user = request.user
    web_link = get_object_or_404(WebLinks, id=pk)
    link_count, created = Linkcount.objects.get_or_create(
        user=user, url=web_link)
    if created:
        link_count.visit_count = 1
    else:
        link_count.visit_count += 1
    link_count.save()

    data = {
        'link': web_link
    }
    return render(request, 'iframe.html', data)
