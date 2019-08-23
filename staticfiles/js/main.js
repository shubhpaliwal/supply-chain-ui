$(document).ready(function() {
  $.get("https://newcelebal.azurewebsites.net/.auth/me", function(data) {
    console.log(data);
    document.getElementById("username").innerHTML = data[0].user_claims[11].val;
  });
  $(".generate").click(function() {
    $.ajax({
      type: "get",
      url: "/all/",
      contentType: "application/json",
      success: function(data) {
        $("#generateuniqueid").val(data["output"]);
      },
      error: function() {
        alert("error");
      }
    });
  });
  $("#datafactorysources").on("change", function() {
    var a = ["BQ", "Oracle", "SAP", "SalesForce"];
    if (a.indexOf(this.value) > -1) {
      a.splice(a.indexOf(this.value, 1));
    }
    for (var i = 0; i < a.length; i++) {
      $("#" + a[i] + "_show")
        .find("input")
        .val("");
      $("#" + a[i] + "_show").hide();
    }
    $("#" + this.value + "_show").show();
  });
});
