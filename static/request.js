function addRequest() {
    var newKeyPhrase = $("#new-request-KeyPhrase").val();
    var newTargetTerms = $("#new-request-TargetTerms").val();
    var newsepKP = $("#new-request-sepKP").val();
    $.post(
        "/request_add",
        {
            type: "add",
            KeyPhrase: newKeyPhrase,
            TargetTerms: newTargetTerms,
            sepKP: newsepKP
        },
        function (data) {
            if (data.success == true) {
                location.reload();
            }
        }
    )
}