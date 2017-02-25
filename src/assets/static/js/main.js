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
  $('#news-content').niceScroll({
    mousescrollstep: 7,
    enablescrollonselection: false,
  });

  function inNewsViewport(i, el) {
    var vp = $(this).parent();
    var vpCoords = vp.offset();
    var vpBottom = vpCoords.top + vp.innerHeight();
    return ($(this).offset().top < vpBottom);
  }

  function manageNewsOpacity() {
    $('#news-content .news-wrap').css('opacity', 1);
    $('#news-content .news-wrap').filter(inNewsViewport).slice(-2).each(function(i) {
      $(this).css('opacity', 0.5-i*0.3);
    });
  }

  manageNewsOpacity();
  $('#news-content').on('scroll', function() {
    manageNewsOpacity();
  });
});
