// using jQuery
url1 = 'http://bhargavreddi.pythonanywhere.com';
url2 = 'http://127.0.0.1:8000';
url_link = url1;
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function addHeader(){
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
}
function sendData(image_id,user_id,user_name) {
    addHeader();
	$.ajax({
		url: url_link+'/api/images/',
		type: 'POST',
		contentType: 'application/json',
		data: JSON.stringify({

			image_id:image_id,
			user_id : user_id
		}),
		dataType: 'json'
	});
	var color = $(".glyphicon-thumbs-up").css("color");
	if(color=="rgb(0, 0, 255)")
	{
		$(".glyphicon-thumbs-up").css("color","black");
		var x =parseInt($("#json").html());
		$("#json").html(x-1);
		$("#user"+user_id).remove();
	}
	else {
		$(".glyphicon-thumbs-up").css("color", "blue");
		var x =parseInt($("#json").html());
		$("#json").html(x+1);
		$('#user_liked').append(
			"<a href=\"/profile/"+user_id+"\" id=\"user"+user_id+"\">"+"<li class=\"list-group-item\"><h3 align=\"left\">" + user_name + "</h3></li></a>"
		);
	}
}
function clickComment(image_id,user_id,nameUser){
	addHeader();
	var text = $("#comment").val();
	$.ajax({
		url: url_link+'/api/comments/',
		type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({

            image_id:image_id,
			user_id : user_id,
            comment : text
        }),
        dataType: 'json'
    });
    $('#comments').append(
        "<li class=\"list-group-item\"><h3 align=\"left\">"+ nameUser +" </h3><p align=\"left\">" + text + "</p></li>"
    );
    $('#comment').val('');
}
function search()
{
	var context = $("#search_user").val();
	if(context =="" || context == null)
		return;
	window.location.replace(url_link+"/search/"+context+"/");
}