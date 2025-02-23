  document.getElementById('switch-camera').addEventListener('click', function() {
            var selectedCamera = document.getElementById('camera-select').value;
            console.log("Ausgewählte Kamera: ", selectedCamera);
        });

        document.getElementById('record-btn').addEventListener('click', function() {
            fetch('/toggle_recording', { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    if (data.recording) {
                        document.getElementById('record-btn').innerText = 'Stop Recording';
                    } else {
                        document.getElementById('record-btn').innerText = 'Start Recording';
                    }
                });
        });