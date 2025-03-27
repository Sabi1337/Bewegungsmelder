import React, { useState, useEffect } from 'react';

const RecordButton = () => {
    const [isRecording, setIsRecording] = useState(false);

    useEffect(() => {
        const recordBtn = document.getElementById("record-btn");
        return () => {
        };
    }, []);

    const handleClick = async () => {
        const response = await fetch("/toggle_recording", { method: "POST" });
        const data = await response.json();

        if (data.recording) {
            setIsRecording(true);
        } else {
            setIsRecording(false);
        }
    };

    return (
        <button
            id="record-btn"
            onClick={handleClick}
            className={isRecording ? "btn btn-danger" : "btn btn-success"}
        >
            {isRecording ? "🛑 Stop Recording" : "🎥 Start Recording"}
        </button>
    );
};

export default RecordButton;
