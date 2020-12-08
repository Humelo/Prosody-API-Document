function GenerateVoice(signature) {
	const xhr = new XMLHttpRequest();
	const audio = new Audio();
	const api_url = "https://api.prosody-tts.com/api/ttsapi/voice-generation/" + signature + "/generate/"
	let url = null;

	xhr.open("GET", api_url, true);
    xhr.setRequestHeader("Authorization", "Api-Key {홈페이지에서 발급받은 APIKey}")
	xhr.addEventListener("load", function () {
		url = URL.createObjectURL(xhr.response);
		audio.src = url;
		audio.play();
	});
	xhr.send();
	audio.addEventListener('ended', function() {
		URL.revokeObjectURL(url);
	}, false);
}
