jQuery(function($) {
  var _ = window.rubonGetMessage.bind(null, 'contacts_wrap');
  var expander = $('<a href="#">');

  expander.css('outline', 'none');
  expander.text(_('EXPANDER_TITLE'));
  expander.click(function(e) {
    e.preventDefault();
    if ($(this).is('.expanded')) {
      $('.contact:not(.main-contact)').fadeOut();
      $(this)
        .text(_('EXPANDER_TITLE'))
        .removeClass('expanded')
      ;
    }
    else {
      $('.contact:not(.main-contact)').fadeIn();
      $(this)
        .text(_('WRAPPER_TITLE'))
        .addClass('expanded')
      ;
    }
    return false;
  });
  $('.contact:not(.main-contact)').hide();
  $('#contacts, #contacts-mobile').append(expander);
});
