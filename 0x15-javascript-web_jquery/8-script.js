$.ajax({
    type: "GET",
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    success: function (data) {
        data.results.forEach(result => {
            $("UL#list_movies").append(`<li>` + result.title +`</li>`)
        });
        
    }
})
