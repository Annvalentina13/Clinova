function sendData() {
    let formData = new FormData();

    formData.append("age", document.getElementById("age").value);
    formData.append("gender", document.getElementById("gender").value);
    formData.append("symptoms", document.getElementById("symptoms").value);

    let val = document.getElementById("durationValue").value;
    let unit = document.getElementById("durationUnit").value;
    formData.append("duration", val + " " + unit);

    formData.append("history", document.getElementById("history").value);

    let file = document.getElementById("report").files[0];
    if (file) formData.append("report", file);

    document.getElementById("loader").style.display = "block";
    document.getElementById("output").textContent = "";

    fetch("/analyze", {
        method: "POST",
        body: formData
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("loader").style.display = "none";
        document.getElementById("output").textContent = data.summary;

        document.getElementById("pdfData").value = data.summary;
        document.getElementById("pdfBtn").disabled = false;
    });
}

function startVoice() {
    let recognition = new webkitSpeechRecognition();
    recognition.lang = "en-US";
    recognition.onresult = e => {
        document.getElementById("symptoms").value = e.results[0][0].transcript;
    };
    recognition.start();
}
