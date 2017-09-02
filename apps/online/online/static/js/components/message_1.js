define(['knockout', 'jquery'], function(ko, $) {
  function ViewModel(params) {
    this.id = params.message.id;
    this.message = params.message.message;
    this.category = params.message.category;
    this.photo = params.message.photo
    this.photo_full = params.message.photo_full
    this.created = makeCreated(params.message.created);
    this.withCategory = params.withCategory || false;
    this.showControls = params.showControls || false;
  }
  ViewModel.prototype = Object.create(Object.prototype, {
    remove: {value: function(model, e) {
      var sure = confirm('Вы дакладна жадаеце выдаліць гэтае паведамленне?');
      if ( ! sure)
        return;
      $.ajax({
        type: 'DELETE',
        url: '/messages/'+model.id,
      });
    }},
  });

  function pad(number) {
    if (number < 10) {
      return '0' + number;
    }
    return number;
  }

  function makeCreated(timestamp) {
    var date = new Date(timestamp*1000);
    var now = new Date();
    var time = pad(date.getHours())+':'+pad(date.getMinutes());
    var created = '';
    if (now.getDate() == date.getDate()) {
      created = time;
    }
    else if (now.getDate() - date.getDate() == 1) {
      created = 'Учора, '+ time;
    }
    else {
      created = pad(date.getDate())+'.'+pad(date.getMonth()+1)+', '+time;
    }
    return created;
  }

  return {
    viewModel: ViewModel,
    template: { element: 'message-template' },
  };
});
