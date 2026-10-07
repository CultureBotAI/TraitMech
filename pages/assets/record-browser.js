/* Enhance the fully rendered catalogue without a fetch or a framework. */
(function () {
  'use strict';
  var form = document.getElementById('record-filters');
  if (!form) return;
  var query = document.getElementById('record-query');
  var category = document.getElementById('record-category');
  var kind = document.getElementById('record-kind');
  var count = document.getElementById('record-count');
  var empty = document.getElementById('record-empty');
  var records = Array.from(document.querySelectorAll('#record-table tbody tr')).map(function (row) {
    return {row: row, text: (row.textContent + ' ' + (row.dataset.synonyms || '')).toLowerCase()};
  });
  function apply() {
    var term = query.value.trim().toLowerCase();
    var visible = 0;
    records.forEach(function (record) {
      var match = record.text.indexOf(term) !== -1 &&
        (!category.value || record.row.dataset.category === category.value) &&
        (!kind.value || record.row.dataset.kind === kind.value);
      record.row.hidden = !match;
      if (match) visible += 1;
    });
    count.textContent = visible + ' of ' + records.length + ' records shown';
    empty.hidden = visible !== 0;
  }
  form.addEventListener('submit', function (event) { event.preventDefault(); });
  function remember() {
    var url = new URL(window.location.href);
    [["q", query], ["category", category], ["kind", kind]].forEach(function (pair) {
      if (pair[1].value) url.searchParams.set(pair[0], pair[1].value);
      else url.searchParams.delete(pair[0]);
    });
    history.replaceState(null, '', url);
    apply();
  }
  function restore() {
    var params = new URLSearchParams(window.location.search);
    [["q", query], ["category", category], ["kind", kind]].forEach(function (pair) {
      pair[1].value = params.get(pair[0]) || '';
    });
    apply();
  }
  form.addEventListener('input', remember);
  form.addEventListener('change', remember);
  window.addEventListener('pageshow', restore);
  // Native reset restores controls after the event has been dispatched.
  form.addEventListener('reset', function () { setTimeout(remember, 0); });
  form.hidden = false;
  restore();
})();
