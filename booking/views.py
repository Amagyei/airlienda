from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


# def select_room(request):
#     try:
       
#         room_selection = {
#             "hostel_id": request.GET.get('hostel_id'),
#             "hostel_name": request.GET.get('hostel_name'),
#             "roomtype_name": request.GET.get('roomtype_name'),
#             "roomtype_price": request.GET.get('roomtype_price'),
#             "roomtype_residents": request.GET.get('roomtype_residents'),
#             "room_number": request.GET.get('room_number'),
#             "room_id": request.GET.get('room_id'),
#             "roomtype_rtid": request.GET.get('roomtype_rtid')
#         }

       
#         request.session.pop('selection_data_obj', None)

        
#         request.session['selection_data_obj'] = {request.GET.get('room_id'): room_selection}
#         data = {
#             'data': request.session['selection_data_obj'],
#             'total_selected_items': len(request.session['selection_data_obj'])
#         }
        
        
#         return JsonResponse(data)
#     except Exception as e:
        
#         return JsonResponse({'error': str(e)}, status=500)

from django.http import JsonResponse

from django.http import JsonResponse

from django.http import JsonResponse

def select_room(request):
    try:
        # Retrieve room details from the request
        room_id = request.GET.get('room_id')
        room_number = request.GET.get('room_number')

        # Validate that room_id and room_number are not None
        if not room_id or not room_number:
            return JsonResponse({'error': 'Room ID and Room Number are required.'}, status=400)

        room_selection = {
            "hostel_id": request.GET.get('hostel_id'),
            "hostel_name": request.GET.get('hostel_name'),
            "room_id": room_id,
            "room_number": room_number,
            "roomtype_name": request.GET.get('roomtype_name'),
            "roomtype_price": request.GET.get('roomtype_price'),
            "roomtype_residents": request.GET.get('roomtype_residents'),
            "roomtype_rtid": request.GET.get('roomtype_rtid')
        }

        # Clear previous selection data
        request.session.pop('selection_data_obj', None)

        # Store the new selection data in the session
        request.session['selection_data_obj'] = {room_id: room_selection}
        data = {
            'data': request.session['selection_data_obj'],
            'total_selected_items': len(request.session['selection_data_obj'])
        }

        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)