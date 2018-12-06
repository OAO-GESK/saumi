$.when($.ready).then(function(){

    $("#sendbtn").click(function(){
        var q = $("#querybox").val()
        $.post("/admin/dbquery", { query: q }).done(function(data){
            $("#responsebox").html(data);
        });
    });

    $("#querybox").keydown(function (e){
        if (e.ctrlKey && e.keyCode == 13) {
            $("#sendbtn").click();
        }
    });

    $("#bFind").click(function(){
        var q = $("#iFind").val()
        $.post("/find", { query: q }).done(function(data){
            $("#dResult").html('Error while database query: table doesn\'t exist')
        });
    });
});