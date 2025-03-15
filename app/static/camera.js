document.addEventListener("DOMContentLoaded", () => {
    const video = document.getElementById("video");
    const canvas = document.getElementById("canvas");
    const snapButton = document.getElementById("snap");
    const facescanInput = document.getElementById("facescanInput");

    // Request camera access
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => { video.srcObject = stream; })
        .catch(error => { console.error("Camera access denied:", error); });

    // Capture the image when button is clicked
    snapButton.addEventListener("click", () => {
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);

        // Convert to Base64
        facescanInput.value = canvas.toDataURL("image/png");
        alert("Face captured successfully!");
    });
});
