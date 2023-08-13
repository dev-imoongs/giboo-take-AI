$(document).ready(function() {
  $("#selectAll").click(function() {
    $(".subCheckbox").prop("checked", this.checked);
  });

  $(".subCheckbox").click(function() {
    if ($(".subCheckbox:checked").length === $(".subCheckbox").length) {
      $("#selectAll").prop("checked", true);
    } else {
      $("#selectAll").prop("checked", false);
    }
  });
});