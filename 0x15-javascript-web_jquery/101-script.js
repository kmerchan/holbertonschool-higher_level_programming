// script that adds, removes, and clears  a LI element to a list
// when the user clicks tags DIV#add_item, DIV#remove_item, or DIV#clear_list
// using jQuery API
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list li').last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').remove();
  });
});
