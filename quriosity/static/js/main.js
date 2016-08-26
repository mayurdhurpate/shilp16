function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$( document ).ready(function() {
    // Typing configrations
    $("#typed").typed({
        stringsElement: $('#typed-strings'),
        typeSpeed: 20,
        backDelay: 500,
        loop: true,
        contentType: 'html', // or text
        // defaults to false for infinite loop
        loopCount: false,
    });

    $(".reset").click(function(){
        $("#typed").typed('reset');
    });

    //signup onchange
    $('#mem').change(function(){
        var mem = $('#mem').val();
        if (mem==1){
            $('#reg3').hide();
        } else {
            $('#reg3').show();
        }
    });

    //signup submit
    $('#signup-submit').click(function(){
        data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            name: $('#name').val(),
            pwd: $('#pwd').val(),
            slot: $('#slot').val(),
            mem: $('#mem').val(),
            name1: $('#signup-name1').val(),
            email1: $('#signup-email1').val(),
            phone1: $('#signup-phone1').val(),
            name2: $('#signup-name2').val(),
            email2: $('#signup-email2').val(),
            phone2: $('#signup-phone2').val()
        }

        $.ajax({
            url: '/quriosity/signup/',
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function(data){
                if (data.error){
                    alert(data.msg);
                }
                else{
                    $('#name').val('');
                    $('#pwd').val('');
                    // $('#slot').val('');
                    // $('#mem').val('');
                    $('#signup-name1').val('');
                    $('#signup-email1').val('');
                    $('#signup-phone1').val('');
                    $('#signup-name2').val('');
                    $('#signup-email2').val('');
                    $('#signup-phone2').val('');
                    alert(data.msg);
                }
            }
        })
    });

    // help question submit
    $('#help-submit').click(function(){
        data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            name: $('#help-name').val(),
            email: $('#help-email').val(),
            msg: $('#help-msg').val()
        }

        $.ajax({
            url: '/quriosity/help/',
            type: 'POST',
            data: data,
            dataType: 'json',
            success: function(data){
                if (data.error){
                    alert(data.msg);
                } else {
                    $('#help-name').val('');
                    $('#help-email').val('');
                    $('#help-msg').val('');
                    alert('We will contact you as soon as possible...');
                }
            }
        });
    });  
});
