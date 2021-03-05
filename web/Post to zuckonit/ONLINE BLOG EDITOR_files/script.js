$(function () {
    $.get("/code").done(function (data) {
        $('#captcha')[0].placeholder = "Code: md5(code)[:6] == " + data.code;
    });
    $("#send").click(function () {
        let contentInput = $("#content").val();
        if (contentInput !== "") {
            $.ajax({
                type: 'POST',
                url: '/send',
                data: {"content": contentInput}
                ,
                success: function (data) {
                    location.reload();
                }
                ,
                error: function (data) {
                    alert(data.responseText);
                }
                ,
            })
            $('#content').val("");
        }
    })
    ;
    $("#clear").click(function () {
        $.get("/clear");
        $('#output').html("");
    });
    $("#submit").click(function () {
        let code = $('#captcha').val();
        $.post("/submit", {'code': code}).done(function (data) {
            alert(data);
        });
    });
})
;
