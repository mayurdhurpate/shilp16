function getCSRF(){
    return document.getElementsByName('csrfmiddlewaretoken')[0].value;
}

$( document ).ready(function() {
    // $.notify("Sorry for inconvenience but due to some unexpected error,\
    //          we're unable to send confirmation mails but they are not \
    //          required for participating in event.", {
    //             clickToHide: true,
    //             autoHideDelay: 10000,
    //             className: 'info',
    //             globalPosition: 'top left',
    //          });

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
            csrfmiddlewaretoken: getCSRF(),
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
        $('#signup-submit').toggle();

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
                    location.reload();
                }
            }
        })
        $('#signup-submit').toggle();
    });

    // help question submit
    $('#help-submit').click(function(){
        data = {
            csrfmiddlewaretoken: getCSRF(),
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

    //login submit
    $('#login-submit').click(function(){
        if ($('#login-name').val() && $('#login-pwd').val()){
            data = {
                csrfmiddlewaretoken: getCSRF(),
                name: $('#login-name').val(),
                pwd: $('#login-pwd').val()
            }
            $('#login-submit').toggle();

            $.ajax({
                url: '/quriosity/login/',
                type: 'POST',
                data: data,
                dataType: 'json',
                success: function(data){
                    if (data.error){
                        $('#login-name').val('');
                        $('#login-pwd').val('');
                        alert(data.msg);
                    } else {
                        window.location = "/quriosity/dashboard";
                    }
                }
            });
            $('#login-submit').toggle();
        } else {
            alert('Enter valid credentials!');
        }
    })  
});
