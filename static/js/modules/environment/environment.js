import { defaultOptions } from "../../utils.js";

$(document).ready(function () {
    let environmentTable = $("#tableEnvironment");
    environmentTable.DataTable(defaultOptions());
});