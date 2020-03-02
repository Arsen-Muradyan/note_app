$(document).ready(function() {
  $("#runBtn").on("click", function() {
    $("#preview").html(marked($("#content").val()));
  });
});
