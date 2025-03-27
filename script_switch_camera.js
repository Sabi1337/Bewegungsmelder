import React, { useState } from 'react';

const CameraControl = () => {
    const [isRecording, setIsRecording] = useState(false);
    const [selectedCamera, setSelectedCamera] = useState('');

    const handleCameraSwitch = (event) => {
        const selected = event.target.value;
        setSelectedCamera(selected);
        console.log("Selected Camera: ", selected);
    };

    const handleRecordButtonClick = async () => {
        const response = await fetch('/toggle_recording', { method: 'POST' });
        const data = await response.json();

        if (data.recording) {
            setIsRecording(true);
        } else {
            setIsRecording(false);
        }
    };

    return (
        <div>
            <select
                id="camera-select"
                value={selectedCamera}
                onChange={handleCameraSwitch}
            >
                <option value="">Select a Camera</option>
                {/* Wähle Cam */}
                <option value="camera1">Camera 1</option>
                <option value="camera2">Camera 2</option>
                <option value="camera3">Camera 3</option>
            </select>
            <button
                id="record-btn"
                onClick={handleRecordButtonClick}
            >
                {isRecording ? 'Stop Recording' : 'Start Recording'}
            </button>
        </div>
    );
};

export default CameraControl;
