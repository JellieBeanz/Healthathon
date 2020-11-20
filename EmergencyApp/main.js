$(document).ready(function() {
    $("#get_info").click(getInfo)

});






//get the data from a given id and display it to the screen
function getInfo() {
    $("#info").text("")
    var id = $("#HealthID").val();
    document.querySelector("#info").innerHTML += '<h2> Health ID: ' + id + '</h2>' +
        '<h2>Health Proxy Details:</h2>' +
        '<table class="table-condensed">' +
        '<thead>' +
        '<th>Phone</th>' +
        '<th>Address</th>' +
        '<th>Email</th>' +
        '<th>HIP</th>' +
        '<th>Directive Custodian</th>' +
        '</thead>' +
        '<tbody>' +
        '<td>9783879464 </td>' +
        '<td>24 Gandhi Road, Chennai , India 600024</td>' +
        '<td>sathya3003@yahoo.com</td>' +
        '<td>directive health</td>' +
        '<td>www.directive.com</td>' +
        '</tbody>' +

        '</table>'





}