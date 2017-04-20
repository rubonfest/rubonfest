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

  //$('nav#nav-menu-sidebar').mmenu();
  $('html').niceScroll();
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

  function scrollToIfOnPage(e) {
    var anchorTest = /^#/,
        href,
        target
    ;
    target = href = $(this).attr('href');
    if ($(this).is('.nav-humb')) {
      e.preventDefault();
      return false;
    }
    if (anchorTest.test(href)) {
      if (href == '#') {
        target = 'body';
      }
      if ( ! $(this).is('.closebtn')) {
        $.scrollTo(target, {duration: 1000, offset: -98});
      }
    }
    if ($(this).parents('#nav-overlay').length > 0) {
      closeNav();
    }
  }

  manageNewsOpacity();
  $('#news-content').on('scroll', function() {
    manageNewsOpacity();
  });
  $('nav a, #nav-overlay a').click(scrollToIfOnPage);
});
