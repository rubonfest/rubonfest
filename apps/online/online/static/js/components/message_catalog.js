define(['knockout'], function(ko) {
  function ViewModel(params) {
    this.messageCategories = ko.computed(fetchCategories.bind(null, params.messagesData));
  }
  
  function fetchCategories(messagesData) {
    var data = messagesData();
    var result = [];
    for (var cat in data) {
      result.push(data[cat]);
    }
    return result;
  }

  return {
    viewModel: ViewModel,
    template: '<!-- ko template: {nodes: $componentTemplateNodes} --><!-- /ko -->'
  };
});
