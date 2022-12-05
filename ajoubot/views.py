from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def keyboard(request):
        return JsonResponse({
                'type' : 'buttons',
                'buttons' : ['학사','도서']
		})

@csrf_exempt
def message(request):

        json_str = ((request.body).decode('utf-8'))
        json_data = json.loads(json_str)
        return_str = json_data['content']
        data = return_str.encode('utf-8')

        if return_str == '학사' :
                return JsonResponse({
                        'message' : {
                                'text' : '무엇이 궁금합니까?'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['처음으로']
                        }
                })

        elif return_str == '도서' :
                return JsonResponse({
                        'message' : {
                                'text' : '무슨 책을 찾으십니까?'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['처음으로']
                        }
                })

        elif return_str == '처음으로' :
                return JsonResponse({
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['학사', '도서']
                        }
                })              

        else :
                return JsonResponse({
                        'message' : {
                                'text' : '다시 입력해주세요.'
                        },
                        'keyboard' : {
                                'type' : 'buttons',
                                'buttons' : ['학사2', '도서']
                        }
                })


