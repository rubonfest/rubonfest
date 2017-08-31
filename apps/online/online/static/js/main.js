requirejs.config({
  baseUrl: "static/js/",
  paths: {
    knockout: 'knockout-3.4.1',
    jquery: 'jquery-3.1.1.min',
  },
});
require(['knockout'], function(ko) {
  ko.components.register('global', { require: 'components/global' });
  ko.components.register('message-catalog', { require: 'components/message_catalog' });
  ko.components.register('message-category', { require: 'components/message_category' });
  ko.components.register('all-messages', { require: 'components/all_messages' });
  ko.components.register('message', { require: 'components/message' });
  ko.applyBindings();
});
