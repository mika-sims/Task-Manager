document.addEventListener('DOMContentLoaded', function () {
  // Materialize css sidenav initialization
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // Datepicker initialization
  let datepicker = document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    i18n: { done: "Select" }
  });

  // Select initialization
  let selects = document.querySelectorAll('select');
  M.FormSelect.init(selects);

  // Collapsible initialization
  let collapsibles = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapsibles);
});