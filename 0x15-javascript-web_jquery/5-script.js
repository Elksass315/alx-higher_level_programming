$("DIV#add_item").on("click", function () {
    const el = $("UL.my_list");
    el.append("<li>Item</li>")
});
