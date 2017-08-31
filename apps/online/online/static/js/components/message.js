define(['knockout'], function(ko) {
  function ViewModel(params) {
    this.message = params.message.message;
    this.created = makeCreated(params.message.created);
  }

  function pad(number) {
    if (number < 10) {
      return '0' + number;
    }
    return number;
  }

  function makeCreated(timestamp) {
    var date = new Date(timestamp*1000);
    created = pad(date.getHours())+':'+pad(date.getMinutes());
    return created;
  }

  return {
    viewModel: ViewModel,
    template: { element: 'message-template' },
  };
});
