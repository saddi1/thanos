$(function () {
  $(".get_detail").click(function () {
    student_id = $(this).find('a').attr('data-id');
    console.log(student_id)
    $.ajax({
      url: '/dashboard/' + student_id + '/',
      type: 'get',
      success: function (data) {
        $(document).find("#modal_student .modal-content").html(data);
        $(document).find("#modal_student").modal("show");
      }
    });
  });

});