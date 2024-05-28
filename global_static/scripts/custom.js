$(document).ready(function(){
	// add to selection function

    $('.select-room').on('click', function(){
        let button = $(this)
        let rid = button.attr("data-index")
       

        let hostel_id = $('#hostel_id').val()
        let hostel_name = $('#hostel_name').val()
        let roomtype_name = $('#roomtype_name').val()
        let roomtype_price = $('#roomtype_price').val()
        let roomtype_rtid = $('#roomtype_rtid').val()
        let roomtype_residents = $('#roomtype_residents').val()
        console.log(roomtype_residents)
    

       
        let room_id = $('#room_rid_' + rid).val();
        let room_number = $('#room_number_' + rid).val();
        

        
        $.ajax({
            url:'/booking/select_room',
            data:{
                'room_id':room_id,
                'room_number':room_number,
                'hostel_id':hostel_id,
                'hostel_name':hostel_name,
                'roomtype_name':roomtype_name,
                'roomtype_price': roomtype_price,
                'roomtype_residents': roomtype_residents,
                'roomtype_rtid': roomtype_rtid
 
            },
            dataType:"json",
            beforeSend: function() {
                console.log("sending data to server")
            },
            success: function(response) {
                console.log(response)
            }
        })

    })
});