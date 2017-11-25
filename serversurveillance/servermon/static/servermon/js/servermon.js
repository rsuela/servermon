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
        console.log('wut3');
        console.log(cardid);
        console.log('wut4');
        
        $.ajax({
            url: "/server_details?server_id=" + cardid,
            type: "GET",
            card_id: cardid,
            success: function(data, textStatus) {
                console.log(this.card_id);
                $('#server-info').html(data);
                $('#server-info').modal({
                    show: 'true'
                });
                
                var csrftoken = getCookie('csrftoken');
                var card_id = this.card_id
                var term = $('.term-area').terminal(function(command, term) {
                    term.pause();
                    $.post('terminal', {server_id: card_id, command: command,csrfmiddlewaretoken: csrftoken}).then(function(response) {
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
            }
        });
    });
});