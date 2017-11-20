$(document).ready(function() {
    
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    $('.card').click(function(){
        var cardid;
        cardid = $(this).find('.cardid').text();
        <!-- cardtitle = $(this).find('.card-title').text(); -->
        $.get('/server_details', {server_id: cardid}, function(data){
            $('#server-info').html(data);
            $('#server-info').modal({
                show: 'true'
            }); 
            
            
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

            $('#server-info').on('shown', function() {
                term.enable();
            });
            
            $('#server-info').on('hidden.bs.modal', function() {
                $('#server-info').modal('hide');
                $('body').removeClass('modal-open');
                $('.modal-backdrop').remove();
                term.disable();
            });

        });
    });
});