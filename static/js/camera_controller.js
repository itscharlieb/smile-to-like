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
        document.getElementById('my_result').innerHTML = '<img src="'+data_uri+'"/>';
        process_photo(data_uri);
    });
}

function process_photo(data_uri){
	$.ajax({
		url: "{{ url_for('get_test') }}",
		contentType: 'application/json',
		data: data_uri,
		success: function (){
			on_processed();
		}
	});
}

function on_processed(){

}