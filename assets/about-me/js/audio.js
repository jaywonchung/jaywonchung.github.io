var recordings_activated = false;

function toggle_recordings() {
  var player = document.getElementById("audio-player");
  if (recordings_activated) {
    player.querySelectorAll("audio").forEach(function(a) { a.pause(); });
    player.style.display = "none";
    recordings_activated = false;
  } else {
    player.style.display = "block";
    var bluebird = player.querySelector("audio");
    if (bluebird) bluebird.play();
    recordings_activated = true;
  }
}

document.addEventListener("DOMContentLoaded", function() {
  var player = document.getElementById("audio-player");
  if (!player) return;
  var audios = player.querySelectorAll("audio");
  audios.forEach(function(audio) {
    audio.addEventListener("play", function() {
      audios.forEach(function(other) {
        if (other !== audio) other.pause();
      });
    });
  });
});
