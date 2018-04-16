function addRequest() {
    console.log("gotin")
    var newKeyPhrase = $("#new-request-KeyPhrase").val();
    var newTargetTerms = $("#new-request-TargetTerms").val();
    // var newsepKP = $("#new-request-sepKP").val();
    newsepKP = "False"
    if ($("#new-request-sepKP").is(':checked')) {
        newsepKP = "True";
    }
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

function fillTargetTermsWithStatic(filename) {
    console.log("fillTargetTermsWithStatic")
    $.get(
        "/../static/" + filename,
        function(data) {
            $("#new-request-TargetTerms").val(data);
        }
    );
}

$(document).ready(function() {
    $("#fillgenes").click(function() {
        fillTargetTermsWithStatic("all_genes.txt");
    });

    $("#filltfs").click(function() {
        fillTargetTermsWithStatic("all_tfs.txt");
    });

    $("#fillligands").click(function() {
        fillTargetTermsWithStatic("all_ligands.txt");
    });

    $("#fillmirnas").click(function() {
        fillTargetTermsWithStatic("all_mirnas.txt");
    });

    $("#filldrugs").click(function() {
        fillTargetTermsWithStatic("all_charlesdrugs.txt");
    });

});
