// import keys
var imported = document.createElement('script');
imported.src = 'js/config.js';
document.body.appendChild(imported);

// source URLs
var streetViewURL = "http://maps.googleapis.com/maps/api/streetview?";
var newYorkTimeURL = "https://api.nytimes.com/svc/search/v2/articlesearch.json?";
var wikipediaURL = "https://en.wikipedia.org/w/api.php?";

function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview
    var city = $("#city").val();
    var address = $("#street").val() + ", " + city;

    $greeting.text("So, you want to live at " + address + "?");

    var imageSize = "size=600x400";
    var location = "location=" + address;
    var key = "key=" + myStreetViewKey;
    var signature = "signature=" + myStreetViewSignature;

    var src = streetViewURL + imageSize + "&" + location + "&" + key + "&" + signature;

    $body.append("<img class='bgimg' src='" + src + "' >");

    // load nytimes
    var nyURL = newYorkTimeURL + "q=" + city + "&sort=newest&api-key=" + myNYTimesKey;
    $nytHeaderElem.text("New York Times Articles About " + city);
    $.getJSON(nyURL, function (data) {
        var articles = data.response.docs;
        for (var i = 0; i < articles.length; i++) {
            var article = articles[i];
            $nytElem.append('<li class="article">' +
                '<a href="' + article.web_url + '" target="_blank">' + article.headline.main + '</a>' +
                '<p>' + article.snippet + '</p>' +
                '</li>');
        };
    }).fail(function () {
        $nytHeaderElem.text("New York Times Articles Could Not Be Loaded");
    });

    // load wikipédia
    var wikiURL = wikipediaURL + "action=opensearch&search='" + city +
        "'&format=json&callback=wikiCallback";
    var wikiRequestTimeout = setTimeout(function () {
        $wikiElem.text("Failed to get wikipédia resources");
    }, 8000);
    $.ajax({
        url: wikiURL,
        dataType: "jsonp",
        success: function (data) {
            var articles = data[1];
            for (var i = 0; i < articles.length; i++) {
                var article = articles[i];
                var url = "https://en.wikipedia.org/wiki/" + article;
                $wikiElem.append('<li>' +
                    '<a href="' + url + '" target="_blank">' + article + '</a>' +
                    '</li>');
            };

            clearTimeout(wikiRequestTimeout);
        },
        fail: function () {
            $wikiElem.text("Failed to get wikipédia resources");
        }
    });

    return false;
};

$('#form-container').submit(loadData);