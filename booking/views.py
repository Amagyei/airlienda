from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def select_room(request):
    # room_selection={}

    # room_selection[str(request.GET['rid'])] ={
    #     "hostel_id": request.get['hostel_id'],
    #     "hostel_name":request.get['hostel_name'],
    #     "roomtype_name":request.get['roomtype_name'], 
    #     "roomtype_price":request.get['roomtype_price'],
    #     "roomtype_residents":request.get['roomtype_residents'],
    #     "room_number":request.get['room_number'],
    #     "room_id":request.get['room_id'],
    #     'roomtype_rtid':request.get['roomtype_rtid']
    # }
    # if 'selection_data_obj' in request.session:
    #     if str(request.GET['rid']) in request.session['selection_data_obj']:
    #         selection_data = request.session['selection_data_obj']
    #         selection_data = request. session['selection_data_obj']
    #         selection_data.update(room_selection)
    #         request. session['selection_data_obj'] = selection_data
    # else:
    #     request.session['selection_data_obj'] = room_selection


    # data={
    #     'data':request.session['selection_data_obj'],
    #     'total_selected_items': len(request.session['selection_data_obj'])
    # }
    # return JsonResponse(data)
    
    try:
        
        room_selection = {
            "hostel_id": request.GET.get('hostel_id'),
            "hostel_name": request.GET.get('hostel_name'),
            "roomtype_name": request.GET.get('roomtype_name'),
            "roomtype_price": request.GET.get('roomtype_price'),
            "roomtype_residents": request.GET.get('roomtype_residents'),
            "room_number": request.GET.get('room_number'),
            "room_id": request.GET.get('room_id'),
            "roomtype_rtid": request.GET.get('roomtype_rtid')
        }

       
        if 'selection_data_obj' in request.session:
            selection_data = request.session['selection_data_obj']
            selection_data.update({request.GET.get('rid'): room_selection})
            request.session['selection_data_obj'] = selection_data
        else:
            request.session['selection_data_obj'] = {request.GET.get('rid'): room_selection}

        
        data = {
            'data': request.session['selection_data_obj'],
            'total_selected_items': len(request.session['selection_data_obj'])
        }
        return JsonResponse(data)
    except Exception as e:
        
        return JsonResponse({'error': str(e)}, status=500)
    

