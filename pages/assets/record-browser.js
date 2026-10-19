/* Enhance the fully rendered catalogue without a fetch or a framework. */
(function () {
  'use strict';
  var form = document.getElementById('record-filters');
  if (!form) return;
  var query = document.getElementById('record-query');
  var category = document.getElementById('record-category');
  var kind = document.getElementById('record-kind');
  var sort = document.getElementById('record-sort');
  var count = document.getElementById('record-count');
  var empty = document.getElementById('record-empty');
  var tbody = document.querySelector ? document.querySelector('#record-table tbody') : null;
  var records = Array.from(document.querySelectorAll('#record-table tbody tr')).map(function (row, idx) {
    var cells = row.querySelectorAll ? row.querySelectorAll('td') : [];
    var labelEl = row.querySelector ? row.querySelector('td a') : null;
    return {
      row: row,
      idx: idx,
      text: (row.textContent + ' ' + (row.dataset.synonyms || '')).toLowerCase(),
      label: (labelEl ? labelEl.textContent : (cells[0] ? cells[0].textContent : row.textContent)).trim().toLowerCase(),
      id: (cells[1] ? cells[1].textContent : '').trim().toLowerCase(),
      category: (row.dataset.category || '').toLowerCase(),
      kind: (row.dataset.kind || '').toLowerCase(),
      kgm: cells[4] ? (parseInt(cells[4].textContent, 10) || 0) : 0,
      synonymsCount: cells[5] ? (parseInt(cells[5].textContent, 10) || 0) : 0
    };
  });
  var sidebar = document.getElementById('facet-sidebar');
  function syncSidebar() {
    if (!sidebar || !sidebar.querySelectorAll) return;
    Array.from(sidebar.querySelectorAll('.facet-btn')).forEach(function (btn) {
      var facet = btn.dataset.facet;
      var val = btn.dataset.val || '';
      var activeVal = facet === 'category' ? category.value : kind.value;
      if (val === activeVal) btn.classList.add('active');
      else btn.classList.remove('active');
    });
  }
  function sortRecords() {
    if (!sort || !tbody || !tbody.appendChild) return;
    var mode = sort.value || 'label-asc';
    var sorted = records.slice().sort(function (a, b) {
      if (mode === 'label-desc') return b.label.localeCompare(a.label) || (a.idx - b.idx);
      if (mode === 'id-asc') return a.id.localeCompare(b.id) || a.label.localeCompare(b.label);
      if (mode === 'category') return a.category.localeCompare(b.category) || a.label.localeCompare(b.label);
      if (mode === 'kind') return a.kind.localeCompare(b.kind) || a.label.localeCompare(b.label);
      if (mode === 'kgm-desc') return (b.kgm - a.kgm) || a.label.localeCompare(b.label);
      if (mode === 'synonyms-desc') return (b.synonymsCount - a.synonymsCount) || a.label.localeCompare(b.label);
      return a.label.localeCompare(b.label) || (a.idx - b.idx);
    });
    sorted.forEach(function (r) { tbody.appendChild(r.row); });
  }
  function apply() {
    sortRecords();
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
    syncSidebar();
  }
  form.addEventListener('submit', function (event) { event.preventDefault(); });
  function remember() {
    var url = new URL(window.location.href);
    [["q", query], ["category", category], ["kind", kind]].forEach(function (pair) {
      if (pair[1].value) url.searchParams.set(pair[0], pair[1].value);
      else url.searchParams.delete(pair[0]);
    });
    if (sort) {
      if (sort.value && sort.value !== 'label-asc') url.searchParams.set('sort', sort.value);
      else url.searchParams.delete('sort');
    }
    history.replaceState(null, '', url);
    apply();
  }
  function restore() {
    var params = new URLSearchParams(window.location.search);
    [["q", query], ["category", category], ["kind", kind]].forEach(function (pair) {
      pair[1].value = params.get(pair[0]) || '';
    });
    if (sort) sort.value = params.get('sort') || 'label-asc';
    apply();
  }
  form.addEventListener('input', remember);
  form.addEventListener('change', remember);
  window.addEventListener('pageshow', restore);
  // Native reset restores controls after the event has been dispatched.
  form.addEventListener('reset', function () { setTimeout(remember, 0); });
  if (sidebar && sidebar.querySelectorAll) {
    Array.from(sidebar.querySelectorAll('.facet-btn')).forEach(function (btn) {
      btn.addEventListener('click', function () {
        var facet = btn.dataset.facet;
        var val = btn.dataset.val || '';
        if (facet === 'category') category.value = (category.value === val && val !== '') ? '' : val;
        else if (facet === 'kind') kind.value = (kind.value === val && val !== '') ? '' : val;
        remember();
      });
    });
    var clearBtn = document.getElementById('facet-clear-btn');
    if (clearBtn && clearBtn.addEventListener) {
      clearBtn.addEventListener('click', function () {
        query.value = '';
        category.value = '';
        kind.value = '';
        if (sort) sort.value = 'label-asc';
        remember();
      });
    }
  }
  form.hidden = false;
  restore();
})();
