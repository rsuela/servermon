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