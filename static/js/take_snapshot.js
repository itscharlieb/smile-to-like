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
                    type: 'POST',
                    data: JSON.stringify({
                        'uri': "" + data_uri
                    }),
                    contentType: 'application/json',
                    success: function(data) {
                        document.getElementById('my_test').innerHTML = JSON.stringify(data)
                    }
                });
            }

            function on_processed(){

            }