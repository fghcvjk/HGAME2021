function getStatus(){
    $.ajax({
        type:"GET",
        url: "/api/getStatus",
        dataType:"json",
        success:function(data){
            let solving = data['solving']
            $("#status").text(solving);
            if(solving === 100)
                getFlag();
        }
    });
}

function getQuestion(){
    $.ajax({
        type: "GET",
        url: "/api/getQuestion",
        dataType: "json",
        xhrFields: {
            withCredentials: true
        },
        crossDomain: true,
        success:function(data){
            $('#integral').html(data['question']);
        }
    });
}

function getFlag(){
    $.ajax({
        type: "GET",
        url: "/api/getFlag",
        dataType: "json",
        success:function(data){
            $('#flag').html(data['flag']);
        }
    });
}

function init(){
    getQuestion();
    getStatus();
}

function submit(){
    $.ajax({
    type: "POST",
    url: "/api/verify",
    data: JSON.stringify({answer:parseFloat($('#answer').val())}),
    dataType: "json",
    contentType: "application/json;charset=utf-8",
    xhrFields: {
        withCredentials: true
    },
    crossDomain: true,
    success: function(data) {
        console.log(data);
        if (data['result'] === true) {
            init();
            $('#alert').html(`
                <div class="alert alert-success">\n
                    <strong>Right!</strong>\n
                </div>`)
        } else {
            $('#alert').html(`
                <div class="alert alert-danger">\n
                    <strong>Wrong!</strong>\n
                </div>`)
        }
    }
});
}