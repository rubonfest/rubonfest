var fotakonkurs = (function($) {
  var api = {};
  var container;
  var hostUrl = "http://apps.rubonfest.by/fotakonkurs";

  function init() {
    container = $('#fotakonkurs-container');
    if (container.length == 0)
      return;
    $('<script src="'+hostUrl+'/jsonp/loadImages"></script>').appendTo('body');
  }
	$(document).ready(init);

  api.loadImages = function(images) {
    if (typeof images.records !== 'object') {
      console.log('Malformed response from fotakonkurs');
      return;
    }
    images.records.forEach(function(image) {
      container.append($('<div>').addClass('fotakonkurs-image-block fotakonkurs-mid-image-block')
          .append($('<a>').attr('href', hostUrl+image.big).attr('target', '_blank')
            .append($('<img>').attr('src', hostUrl+image.mid).addClass('fotakonkurs-image'))
          )
      );
    });
  }

  return api;
})(jQuery);
