Webcam.set({
	width: 320,
	height: 240,
	image_format: 'jpeg',
	jpeg_quality: 90
});
Webcam.attach( '#my_camera' );
function take_snapshot() {
    // take snapshot and get image data
    Webcam.snap( function(data_uri) {
        // display results in page
        // document.getElementById('my_result').innerHTML = '<img src="'+data_uri+'"/>';
        console.log("here");
        process_photo(data_uri);
    });
}

function process_photo(data_uri){
	$.ajax({
		// url: "{{ url_for('get_test') }}",
		url: "http://localhost:5000/get_test",
		type: 'POST',
		data: JSON.stringify({
			'uri': "" + data_uri
		}),
		contentType: 'application/json',
		success: function(data) {
			console.log(JSON.stringify(data));
			console.log(data.action);
			if (data.action == "LIKE") {
				$("#like-animation").animate({opacity:"1"}, 300).animate({opacity:"0"},300);
			};
			// document.getElementById('my_test').innerHTML = JSON.stringify(data)
		}
	});
}

function on_processed(){

}