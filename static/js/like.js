
    function Like(){

    var liked = $(this)
    var pk = liked.data('id')
    var action = liked.data('action')
   

    $.ajax({
        url : "/api/" + pk + "/" + action + "/",
        type: 'GET',
        data:{'blog_qs':pk},

        success : function(json){
            console.log(json)
            console.log(json.liked)


            if(json.liked == true){
            
                $('#id_like').addClass('follow_boton_ajax')

                $('#id_like').text('Dislike')
               

            }else if(json.liked == false){


                var UnFollow = "<button class='follow_boton'>Seguir</button>"

                $('#id_like').removeClass('follow_boton_ajax')
                $('#id_like').text('Like')
            }

        }
    })

}

$(function() {
    $('[data-action="Like"]').click(Like);
});
