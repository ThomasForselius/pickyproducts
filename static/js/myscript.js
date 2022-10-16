function like(product_id){
    $.ajax({
        type: 'POST',
        url: 'like_prod',
        data: {
            product_id: product_id,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'POST'
        },
        success: function (json){ 
            $('#likes'+product_id).html(json['result'])
            let name = '#heart' + product_id
            $(name).toggleClass('fa-regular fa-solid')
        }
    })
}