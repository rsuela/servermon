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

$('document').ready(function(){
    $('#search,#searchinput').on('keyup click', function(e){
        var search_term = $('#searchinput').val();
        $.get( "search?q=" + search_term, function( data ) {
            $('.card-container').html(data);
            console.log(data);
        });
    });
});