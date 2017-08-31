define(['knockout'], function(ko) {
  function ViewModel(params) {
    var self = this;
    this.messages = ko.observableArray();
    this.categoryLimit = params.categoryData.category_limit;
    this.name = ko.computed(function() {
      self.messages.removeAll();
      params.categoryData.items.forEach(function(message) {
        self.messages.push(message);
      });
      return params.categoryData.category;
    });
  }

  return {
    viewModel: ViewModel,
    template: { element: 'message-category-template' },
  };
});

