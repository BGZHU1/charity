//just for landing page
$(document).ready(function() {
  var scroll_start = 0;
  var startchange = $('#startchange');
  var offset = startchange.offset();
  if (startchange.length) {
    $(document).scroll(function() {
      scroll_start = $(this).scrollTop();
      if (scroll_start > offset.top) {
        $(".navbar-default").css('background-color', '#c1292e');
      } else {
        $('.navbar-default').css('background-color', 'transparent');
      }
    });
  }

  /*add modal*/
  this.querySelectorAll('.modal-button').forEach(function(el) {
    el.addEventListener('click', function() {
      console.log('clicked')
      var target = document.querySelector(el.getAttribute('data-target'));

      target.classList.add('is-active');

      target.querySelector('.modal-close').addEventListener('click',   function() {
          target.classList.remove('is-active');
       });
    });
  });

});
