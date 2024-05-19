$(document).ready(function () {
	$(".update-camera").click(function () {
		$(this).prop("disabled", true);
		const streamUrl = $(this).data("stream-url");
		const imgId = $(this).closest(".card").find("img").attr("id");
		$("#" + imgId).attr("src", streamUrl + "?_t=" + Date.now());
		setTimeout(() => {
			$(this).prop("disabled", false);
		}, 1000);
	});

	$(".view-camera").click(function (e) {
		e.preventDefault();
		var streamUrl = $(this).data("stream-url");
		$("#cameraPreview").attr("src", streamUrl);
	});
});
