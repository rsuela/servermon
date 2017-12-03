(function($) {

  $(window).on('scroll', function(event) {
    event.preventDefault()

    var height = $(window).scrollTop();

    if (height > 0) {
      $('#header').addClass('scrolled')
    } else {
      $('#header').removeClass('scrolled')
    }
  })
})(jQuery);

function bindButtonClick(){
    $('.card').click(function(){
        var cardid;
        cardid = $(this).find('span').attr('cardid');
      
        $.ajax({
            url: "/server_details?server_id=" + cardid,
            type: "GET",
            card_id: cardid,
            success: function(data, textStatus) {
                $('.container-sidepanel').html(data);
            }
        });
      $('.container-sidepanel').toggleClass('open');
    });
        
    $(document).mouseup(function(e) 
    {
        var container = $('.container-sidepanel');
        if (!container.is(e.target) && container.has(e.target).length === 0) 
        {
            $('.container-sidepanel').removeClass('open');
        }
    });
}



$('document').ready(function(){
    $('#search,#searchinput').on('keyup click', function(e){
        var search_term = $('#searchinput').val();
        $.get( "search?q=" + search_term, function( data ) {
            $('.card-container').html(data);
            bindButtonClick();
        });
        
    });
    
    bindButtonClick();
    

});