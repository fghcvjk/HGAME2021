$(function () {
    $.get("/contents").done(function (data) {
        let output = document.getElementById("output")
        for (let i = 0; i < data.length; i++) {
            let div = document.createElement("div")
            div.innerHTML = data[i]
            output.appendChild(div)
        }
    })
    $.get("/code").done(function (data) {
        $('#captcha')[0].placeholder = "Code: md5(code)[:6] == " + data.code
    })
    $("#send").click(function () {
        let contentInput = $("#content").val()
        if (contentInput !== "") {
            $.ajax({
                type: 'POST',
                url: '/send',
                data: {content: contentInput}
                ,
                success: function (data) {
                    location.reload()
                }
                ,
                error: function (data) {
                    alert(data.responseText)
                }
                ,
            })
            $('#content').val("")
        }
    })
    // new feature here
    $("#replace").click(function () {
        let substrInput = $("#substr").val()
        let replacementInput = $("#replacement").val()
        if (substrInput !== "" && replacementInput !== "") {
            $.ajax({
                type: 'POST',
                url: '/replace',
                data: {"substr": substrInput, "replacement": replacementInput},
                success: function (data) {
                    window.open("/preview")
                },
                error: function (data) {
                    alert(data.responseText)
                },
            })
            $('#substr').val("")
            $('#replacement').val("")
        }
    })
    $("#clear").click(function () {
        $.get("/clear")
        $('#output').html("")
    })
    $("#submit").click(function () {
        let code = $('#captcha').val()
        $.post("/submit", {'code': code}).done(function (data) {
            alert(data)
        })
    })
})
