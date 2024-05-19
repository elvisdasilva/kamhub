$(document).ready(function () {
	$(".view-camera").click(function (e) {
		e.preventDefault();
		let streamUrl = $(this).data("stream-url");
		let errorMessage = $(this).closest(".card").find(".error-message");

		// Clear previous error message
		errorMessage.hide().text("");

		$.ajax({
			url: streamUrl,
			type: "GET",
			success: function (data) {
				$("#cameraPreview").attr("src", streamUrl + "?t=" + timestamp);
				$("#cameraModal").modal("show");
			},
			error: function (xhr) {
				let errorText =
					xhr.responseJSON && xhr.responseJSON.error
						? xhr.responseJSON.error
						: "An error occurred while trying to fetch the camera stream.";
				errorMessage.text(errorText).show();
			},
		});
	});

	$(".update-camera").click(function (e) {
		e.preventDefault();
		let streamUrl = $(this).data("stream-url");
		let errorMessage = $(this).closest(".card").find(".error-message");

		// Clear previous error message
		errorMessage.hide().text("");

		$.ajax({
			url: streamUrl,
			type: "GET",
			success: function (data) {
				$("#camera-stream-" + camera.id).attr("src", streamUrl + "?t=" + timestamp);
			},
			error: function (xhr) {
				let errorText =
					xhr.responseJSON && xhr.responseJSON.error
						? xhr.responseJSON.error
						: "An error occurred while trying to update the camera stream.";
				errorMessage.text(errorText).show();
			},
		});
	});
});
