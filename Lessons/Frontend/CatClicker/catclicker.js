$(document).ready(() => {
    let click = 0;
    $("#tesla").click(() => {
        $("#clicks").html(++click);
    });

    let clickscat1 = 0;
    $("#cat1").click(() => {
        $("#clickscat1").html(++clickscat1);
    });
    let clickscat2 = 0;
    $("#cat2").click(() => {
        $("#clickscat2").html(++clickscat2);
    });
})