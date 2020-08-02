$(document).ready(function () {
  $('#type')
    .change(function () {
      $(this)
        .find('option:selected')
        .each(function () {
          var optionValue = $(this).attr('value');
          if (optionValue) {
            $('.SubMenu')
              .not('.' + optionValue)
              .hide();
            $('.' + optionValue).show();
          } else {
            $('.SubMenu').hide();
          }
        });
    })
    .change();
  $('.subtype')
    .change(function () {
      $(this)
        .find('option:selected')
        .each(function () {
          var suboptionValue = $(this).attr('value');
          if (suboptionValue) {
            $('.Table')
              .not('.' + suboptionValue)
              .hide();
            $('.' + suboptionValue).show();
          } else {
            $('.Table').hide();
          }
        });
    })
    .change();
});
