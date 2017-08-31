define(['knockout'], function(ko) {
  function ViewModel(params) {
    this.message = params.message.message;
    this.category = params.message.category;
    this.created = makeCreated(params.message.created);
    this.withCategory = params.withCategory || false;
  }

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
