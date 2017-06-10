jQuery(function($) {

  $.fn.isOnScreen = function(){
    var element = this.get(0);
    var bounds = element.getBoundingClientRect();
    return bounds.top < window.innerHeight && bounds.bottom > 0;
  }

  function openNav(e) {
    document.getElementById("nav-overlay").style.width  = "100%";
  }

  function closeNav(e) {
    document.getElementById("nav-overlay").style.width = "0%";
    return false;
  }

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

  function showAnimations() {
    $('.animated').each(function() {
      var animation, delay;
      animation = $(this).data('animation') || 'fadeInUp';
      delay = $(this).data('animation-duration') || 600;
      if ($(this).hasClass('scroll-animation-done'))
        return;
      if ( ! $(this).isOnScreen())
        return;
      $(this)
        .css({
          '-moz-animation-duration': delay,
          '-webkit-animation-duration': delay,
          '-ms-animation-duration': delay,
          '-o-animation-duration': delay,
        })
        .css('visibility', 'visible')
        .addClass(animation+' scroll-animation-done')
        .one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
          $(this).removeClass('animated '+animation);
        })
      ;
    });
  }

  function setGuestHovers() {
    var timeout,
        animation = 'pulse';
    $('.musical-guest > a, .other-guest > a').hover(
        function(e) {
          timeout = setTimeout(function() {
            $(this).parent()
              .addClass('animated '+animation);
          }.bind(this), 50);
        },
        function(e) {
          clearTimeout(timeout);
          $(this).parent().removeClass('animated '+animation);
        }
    );
  }

  $('.animated').css('visibility', 'hidden');
  $('.nav-humb').click(openNav);
  $('#nav-overlay .closebtn').click(closeNav);

  $('html').niceScroll({
    mousescrollstep: 120,
    scrollspeed: 100,
  });

  if ($('#news-content .news-wrap').length > 2) {
    manageNewsOpacity();
  }
  $('#news-content').on('scroll', function() {
    manageNewsOpacity();
  });
  $(document).on('scroll', function() {
    showAnimations();
  });
  showAnimations();
  setGuestHovers();
  $('nav a, #nav-overlay a').click(scrollToIfOnPage);
  $('.flexslider').flexslider({
    animation: 'fade',
    controlNav: true,
    directionNav: false,
    controlsContainer: '.features-controls',
  });
});
