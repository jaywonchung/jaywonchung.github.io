var main_key = "bluebird";
var music_title_map = {
  "bluebird": "Bluebird",
  "floral": "Floral Raindrops",
}
var music_audio_map = {}
var music_button_map = {}
var music_li_map = {}
for (var key in music_title_map) {
  music_audio_map[key] = document.getElementById(`audio-${key}`);
  music_button_map[key] = document.getElementById(`audio-${key}-button`);
  music_li_map[key] = document.getElementById(`audio-${key}-li`);
}

var recordings_activated = false;
function toggle_recordings() {
  if (recordings_activated) {
    for (var key in music_title_map) {
      music_li_map[key].style.display = "none";
      music_audio_map[key].pause();
    }
    document.getElementById("fingerstyle-guitar-text").innerHTML = "Fingerstyle Guitar";
    recordings_activated = false;
  } else {
    audio_button(main_key);
    for (var key in music_title_map) {
      music_li_map[key].style.display = "block";
    }
    document.getElementById("fingerstyle-guitar-text").innerHTML = "Me playing:";
    recordings_activated = true;
  }
}

// Invoked when the play/pause button is clicked.
function audio_button(clicked_key) {
  var clicked_button = document.getElementById(`audio-${clicked_key}-button`);
  // If music is paused, pause all other recordings and play this one.
  if (music_audio_map[clicked_key].paused) {
    for (var key in music_title_map) {
      if (key == clicked_key) continue;
      music_audio_map[key].pause();
      var button = document.getElementById(`audio-${key}-button`);
      button.classList.remove("fa-pause");
      button.classList.add("fa-play");
    }
    music_audio_map[clicked_key].play();
    clicked_button.classList.remove("fa-play");
    clicked_button.classList.add("fa-pause");
  }
  
  // If music was playing, just pause this one.
  else {
    music_audio_map[clicked_key].pause();
    clicked_button.classList.remove("fa-pause");
    clicked_button.classList.add("fa-play");
  }
}
