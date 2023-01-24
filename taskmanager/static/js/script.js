document.addEventListener('DOMContentLoaded', function () {
  // Materialize css sidenav initialization
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // Datepicker initialization
  var datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    i18n: { done: "Select" }
  });
});