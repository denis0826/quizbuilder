jQuery(document).ready(function() {
  $('.agenda-date input').datepicker({
      format: "yyyy-mm-dd"
  });

  $('#sandbox-container div').datepicker({
      format: "yyyy-mm-dd",
      clearBtn: true,
      calendarWeeks: true,
      todayHighlight: true
  }).on('changeDate', function() {
    var my_date = $(this).datepicker('getFormattedDate');
    console.log(my_date);
    var date = $('#my_hidden_input').val(my_date);

    $.ajax({
        url: '/ajax/show_date/',
        data: {
          'date': date
        },
        dataType: 'json',
        success: function (data) {
          console.log(data)
        }
      });

  });

});