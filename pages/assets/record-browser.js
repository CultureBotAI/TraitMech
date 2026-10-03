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
  form.addEventListener('input', apply);
  form.addEventListener('change', apply);
  // Native reset restores controls after the event has been dispatched.
  form.addEventListener('reset', function () { setTimeout(apply, 0); });
  form.hidden = false;
  apply();
})();
