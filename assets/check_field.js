$('#check_field_name').on('focusout', function(e){
    $.ajax({
        url: "check_field/"+$('#check_field_name').attr('name')+"/",
        type: 'POST',
        data: {name:$('#check_field_name').val()},
        dataType:'json',

        success: function(response){
            $('#msg_check_name').html("").removeClass();
            $('#msg_check_name').prepend(
                `
                <h5 class="alert-success" id="msg_check_name">${ response.msg }</h5>
                `
            )
        console.log(response);
        },
        error: function(response){
          $('#msg_check_name').html("").removeClass();
          response.responseJSON.data.name.forEach(err =>  {
              $('#msg_check_name').prepend(
                `
                <h5 class="alert-danger" id="msg_check_name">${ err }</h5>
                `
            )
        });
          console.log(response.responseJSON.data.name[0])
        }
    });
});

$('#check_field_cell').on('focusout', function(e){
    $.ajax({
        url: "check_field/"+$('#check_field_cell').attr('name')+"/",
        type: 'POST',
        data: {cell:$('#check_field_cell').val()},
        dataType:'json',

        success: function(response){
            $('#msg_check_cell').html("").removeClass();
            $('#msg_check_cell').prepend(
                `
                <h5 class="alert-success" id="msg_check_cell">${ response.msg }</h5>
                `
            )
        console.log(response);
        },
        error: function(response){
          $('#msg_check_cell').html("").removeClass();
          response.responseJSON.data.cell.forEach(err =>  {
              $('#msg_check_cell').prepend(
                `
                <h5 class="alert-danger" id="msg_check_cell">${ err }</h5>
                `
            )
        });
          console.log(response.responseJSON.data.name[0])
        }
    });
});


$('#check_field_road').on('focusout', function(e){
    $.ajax({
        url: "check_field/"+$('#check_field_road').attr('name')+"/",
        type: 'POST',
        data: {road:$('#check_field_road').val()},
        dataType:'json',

        success: function(response){
            $('#msg_check_road').html("").removeClass();
            $('#msg_check_road').prepend(
                `
                <h5 class="alert-success" id="msg_check_road">${ response.msg }</h5>
                `
            )
        console.log(response);
        },
        error: function(response){
          $('#msg_check_road').html("").removeClass();
          response.responseJSON.data.road.forEach(err =>  {
              $('#msg_check_road').prepend(
                `
                <h5 class="alert-danger" id="msg_check_road">${ err }</h5>
                `
            )
        });
          console.log(response.responseJSON.data.road[0])
        }
    });
});


$('#check_field_house_number').on('focusout', function(e){
    $.ajax({
        url: "check_field/"+$('#check_field_house_number').attr('name')+"/",
        type: 'POST',
        data: {house_number:$('#check_field_house_number').val()},
        dataType:'json',

        success: function(response){
            $('#msg_check_house_number').html("").removeClass();
            $('#msg_check_house_number').prepend(
                `
                <h5 class="alert-success" id="msg_check_house_number">${ response.msg }</h5>
                `
            )
        console.log(response);
        },
        error: function(response){
          $('#msg_check_house_number').html("").removeClass();
          response.responseJSON.data.house_number.forEach(err =>  {
              $('#msg_check_house_number').prepend(
                `
                <h5 class="alert-danger" id="msg_check_house_number">${ err }</h5>
                `
            )
        });
          console.log(response.responseJSON.data.house_number[0])
        }
    });
});