// ------------------------------
// Multi-Agent Interview Platform
// script.js
// ------------------------------

// Timer

let totalTime = 300; // 5 minutes

const timer = document.getElementById("timer");

if (timer) {

    const countdown = setInterval(function () {

        let minutes = Math.floor(totalTime / 60);
        let seconds = totalTime % 60;

        timer.innerHTML =
            minutes + ":" + (seconds < 10 ? "0" + seconds : seconds);

        totalTime--;

        if (totalTime < 0) {

            clearInterval(countdown);

            alert("Time is Over!");

            document.querySelector("form").submit();

        }

    }, 1000);

}


// Progress Bar

const progress = document.getElementById("progress");

if (progress) {

    const current = Number(progress.dataset.current);

    const total = Number(progress.dataset.total);

    progress.value = (current / total) * 100;

}


// Character Counter

const answerBox = document.getElementById("answer");

const counter = document.getElementById("counter");

if (answerBox && counter) {

    answerBox.addEventListener("input", function () {

        counter.innerHTML = answerBox.value.length + " Characters";

    });

}


// Prevent Empty Answer

const form = document.querySelector("form");

if (form) {

    form.addEventListener("submit", function (e) {

        if (answerBox.value.trim() === "") {

            e.preventDefault();

            alert("Please enter your answer.");

        }

    });

}

// ----------------------
// Voice Recognition
// ----------------------

if ('webkitSpeechRecognition' in window) {

    const recognition = new webkitSpeechRecognition();

    recognition.continuous = false;

    recognition.lang = "en-US";

    recognition.interimResults = false;

    recognition.maxAlternatives = 1;

    const voiceBtn = document.getElementById("voiceBtn");

    if (voiceBtn) {

        voiceBtn.onclick = function () {

            recognition.start();

            voiceBtn.innerHTML = "🎙 Listening...";

        };

    }

    recognition.onresult = function (event) {

        document.getElementById("answer").value =
            event.results[0][0].transcript;

        counter.innerHTML =
            document.getElementById("answer").value.length +
            " Characters";

        voiceBtn.innerHTML = "🎤 Speak Again";

    };

    recognition.onerror = function () {

        voiceBtn.innerHTML = "🎤 Try Again";

    };

}

const question = document.querySelector("h3");

if(question){

const speech = new SpeechSynthesisUtterance(question.innerText);

speech.lang="en-US";

window.speechSynthesis.speak(speech);

}

// ----------------------
// Voice Answer
// ----------------------

if ('webkitSpeechRecognition' in window) {

    const recognition = new webkitSpeechRecognition();

    recognition.lang = "en-US";
    recognition.continuous = false;
    recognition.interimResults = false;

    const voiceBtn = document.getElementById("voiceBtn");

    if (voiceBtn) {

        voiceBtn.onclick = function () {

            recognition.start();

            voiceBtn.innerHTML = "🎙 Listening...";

        };

        recognition.onresult = function (event) {

            document.getElementById("answer").value =
                event.results[0][0].transcript;

            voiceBtn.innerHTML = "🎤 Speak Again";

        };

        recognition.onend = function () {

            voiceBtn.innerHTML = "🎤 Speak Again";

        };

    }

}