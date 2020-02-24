
$( document ).ready(function() {

    $('#submit_btn').click(function(e){
        e.preventDefault();
        var csrftoken = $('[name="csrfmiddlewaretoken"]').val()
        var url = $('#url_input').val()
        var data = {
            csrfmiddlewaretoken: csrftoken,
            url:url
        }
        console.log(data)
        $( ".result_container").hide();
        $('#loadingmessage').show();
        $.post("/sumarize",data).done(function( result ) {
            $('#loadingmessage').hide();
            $( ".result" ).html( result );
            $( ".result_container" ).show();

          });
    });



});