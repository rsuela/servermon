$('.card').click(function(){
    var cardid;
    cardid = $(this).find('.cardid').text();
    <!-- cardtitle = $(this).find('.card-title').text(); -->
    $.get('/server_details', {server_id: cardid}, function(data){
        $('#myModal').html(data);
        $('#myModal').modal({
            show: 'true'
        }); 
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$(document).ready(function() {
    var csrftoken = getCookie('csrftoken');
    var term = $('.term-area').terminal(function(command, term) {
        term.pause();
        $.post('terminal', {command: command,csrfmiddlewaretoken: csrftoken}).then(function(response) {
            term.echo(response).resume();
        });
    }, {
        enabled: false,
        greetings: 'Command Line Interface:',
        onBlur: function() {
            return false;
        }
    });

    $('#myModal').on('shown', function() {
        term.enable();
    })
});