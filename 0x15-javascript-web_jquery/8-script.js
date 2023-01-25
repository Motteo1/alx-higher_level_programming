$(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data, textStatus) {
    const results = data.results;
    for (let movie of results) {
      const listItem = $('<li></li>').text(movie.title);
      $('ul#list_movies').append(listItem);
    }
  });
});
