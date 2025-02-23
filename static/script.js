document.addEventListener("DOMContentLoaded", function () {
    const recordBtn = document.getElementById("record-btn");

    if (recordBtn) {
        recordBtn.addEventListener("click", function () {
            fetch("/toggle_recording", { method: "POST" })
                .then(response => response.json())
                .then(data => {
                    if (data.recording) {
                        recordBtn.textContent = "🛑 Stop Recording";
                        recordBtn.className = "btn btn-danger";
                    } else {
                        recordBtn.textContent = "🎥 Start Recording";
                        recordBtn.className = "btn btn-success";
                    }
                });
        });
    }
});
