jQuery(function($) {

  function openNav(e) {
    document.getElementById("nav-overlay").style.width  = "100%";
  }

  function closeNav(e) {
    document.getElementById("nav-overlay").style.width = "0%";
    return false;
  }

  $('.nav-humb').click(openNav);
  $('#nav-overlay .closebtn').click(closeNav);

  $('nav#nav-menu-sidebar').mmenu();
  $('html').niceScroll();
  $('#news-content').niceScroll();
});
