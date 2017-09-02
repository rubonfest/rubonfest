define(['knockout'], function(ko) {
  function ViewModel(params) {
    this.categoriesNames = ko.observableArray();
    this.messageCategories = ko.computed(fetchCategories.bind(this, params.messagesData));
  }
  
  function fetchCategories(messagesData) {
    var data = messagesData();
    var result = [];
    this.categoriesNames.removeAll();
    for (var cat in data) {
      this.categoriesNames.push(cat);
      result.push(data[cat]);
    }
    return result;
  }

  return {
    viewModel: ViewModel,
    template: '<!-- ko template: {nodes: $componentTemplateNodes} --><!-- /ko -->'
  };
});
