function addRequest() {
    var newEmail = $("#new-request-email").val();
    var newName = $("#new-request-name").val();
    var newDescription = $("#new-request-description").val();
    $.post(
        "/request_add",
        {
            type: "add",
            email: newEmail,
            name: newName,
            description: newDescription
        },
        function (data) {
            if (data.success == true) {
                location.reload();
            }
        }
    )
}