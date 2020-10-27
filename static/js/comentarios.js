    function comentario(){

        var comentar = $(this);
        var type       = comentar.data('type')
        var pk         = comentar.data('id')
        var action     = comentar.data('action')

        $.ajax({
            url  : "/api/" + type + "/" + pk + "/" + action + "/",
            type : 'POST',
            data : {comentario : $('#id_comentario').val()},

            success : function(json){

             $('#id_comentario').val('');

             console.log(json)

            },


        });

        return false;

    }

    $(function(){
        $('[data-action="comentar"]').click(comentario);
    })