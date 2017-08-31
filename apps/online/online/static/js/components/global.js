define(['knockout', 'jquery'], function(ko, $) {
  function ViewModel(params) {
    this.messagesData = params.messagesData;
  }

  function pollCallback(params) {
    $.get('/categorized-messages')
      .done(function(response) {
        params.messagesData(response.messages);
      })
    ;
  }

  function pollMessages(params) {
    pollCallback(params);
    var poll = setInterval(pollCallback.bind(null, params), 4000);
  }

  function factoryViewModel(params, componentInfo) {
    params = params || {};
    params.messagesData = ko.observable();

    pollMessages(params);
    return new ViewModel(params);
  }
 
  return {
    viewModel: {createViewModel: factoryViewModel},
    template: '<!-- ko template: {nodes: $componentTemplateNodes } --><!-- /ko -->'
  };
});
