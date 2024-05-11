from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def add_to_selection(request):
    room_selection={}

    room_selection[str(request.GET['ID'])] ={
        "hostel_id": request.get['hostel_id'],
        "hostel_name":request.get['hostel_name'],
        "room_name":request.get['room_name'], 
        "room_price":request.get['room_price'],
        "number_of_beds":request.get['number_of_beds'],
        "noom_number":request.get['noom_number'],
        "room_type":request.get['room_type'],
        "room_id":request.get['room_id'],
    }
    if 'selection_data_obj' in request.session:
        if str(request.GET['id']) in request.session['selection_data_obj']:
            selection_data = request.session['selection_data_obj']
            selection_data = request. session['selection_data_obj']
            selection_data.update(room_selection)
            request. session['selection_data_obj'] = selection_data
    else:
        request.session['selection_data_obj'] = room_selection


    data={
        'data':request.session['selection_data_obj'],
        'total_selected_items': len(request.session['selection_data_obj'])
    }
    return JsonResponse(data)
