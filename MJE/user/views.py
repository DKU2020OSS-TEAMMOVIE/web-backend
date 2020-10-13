from django.shortcuts import render

import json

from django.views import View
from django.http import JsonResponse

from .models import User

class Sign_in_work(View) :
    def post(self, request):
        data = json.loads(request.body)
        User(
            user_id = data['user_id'],
            nickname=data['nickname'],
            email = data['email'],
            password = data['[password'],
        )

        if User.objects.filter(user_id = data['user_id']).exists() :   #아이디 동일할 시 오류 생성
            return JsonResponse({"message": "이미 존재하는 아이디입니다"}, status = 401)
        elif User.objects.filter(nickname = data['nickname']).exists() == True :    #닉네임 동일할 시 오류 생
            return JsonResponse({"message": "이미 존재하는 닉네임입니다"}, status = 401)
        else:
            User(
                user_id = data['user_id'],
                nickname = data['nickname'],
                email = data['email'],
                password = data['password'],
            ).save()
            return JsonResponse({"message":"회원으로 가입되었습니다. "}, status = 200)


    def get(self, request):
        users = User.objects.values()
        return JsonResponse({"data" : list(users)}, status = 200)

class Log_in_Work(View):
    def post(self, request):
        data = json.loads(request.body)
        User(
            user_id = data['user_id'],
            nickname=data['nickname'],
            email = data['email'],
            password = data['[password'],
        )

        if User.objects.filter(user_id = data['user_id'], password = data['password']).exists() ==True :
            return JsonResponse({"message" : "로그인에 성공했습니다."}, status = 200)
        else:
            return JsonResponse({"message" : "아이디나 비밀번호가 일치하지 않습니다. "}, status = 401)

    def get(self, request):
        user = User.objects.values()
        return JsonResponse({"list" : list(user)}, status = 200)


