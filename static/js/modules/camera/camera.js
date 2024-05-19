import { defaultOptions } from "../../utils.js";

$(document).ready(function () {
	let cameraTable = $("#tableCamera");
	cameraTable.DataTable(defaultOptions());

	$(".select2bs4").select2({
		theme: "bootstrap4",
		placeholder: "Selecione o ambiente",
		allowClear: true,
		language: "pt-BR",
		width: "100%",
	});

	$(".view-camera").click(function (e) {
		e.preventDefault();
		var streamUrl = $(this).data("stream-url");
		$("#cameraPreview").attr("src", streamUrl);
	});
});
