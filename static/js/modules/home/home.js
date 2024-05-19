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
});
