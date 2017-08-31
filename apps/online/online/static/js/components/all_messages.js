define(['knockout', 'jquery'], function(ko, $) {

  function ViewModel(params) {
    this.offset = 0;
    this.messages = ko.observableArray();
  }
  ViewModel.prototype = Object.create(Object.prototype, {
    load: {value: function(model, e) {
      $.get('/messages', {offset: model.offset})
        .done(this._loadSuccess.bind(model))
      ;
    }},
    _loadSuccess: {value: function(response) {
      response.messages.forEach(function(message) {
        this.messages.push(message);
      }, this);
      this.offset = response.next_offset;
    }},
    clear: {value: function(model, e) {
      model.messages.removeAll();
      this.offset = 0;
    }},
  });

  return {
    viewModel: ViewModel,
    template: { element: 'all-messages-template' },
  };
});
