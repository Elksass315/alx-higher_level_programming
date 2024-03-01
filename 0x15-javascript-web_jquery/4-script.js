$("DIV#toggle_header").on("click", function () {
    const el = $("header");
    if (el.hasClass("red")) {
        el.removeClass();
        el.addClass("green");
    } else {
        el.removeClass();
        el.addClass("red");
    }
});
