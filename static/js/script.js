$(document).ready(function() {
  $("#runBtn").on("click", function() {
    $("#preview").html(marked($("#content").val()));
  });
  function getCookie(name) {
    var arr = document.cookie.split("; ");
    function getStr(str) {
      return str.indexOf(name) != -1;
    }
    var items = arr.filter(getStr);
    return items[0].split("=")[1];
  }
});
