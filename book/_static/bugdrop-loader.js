(function () {
  function load() {
    var s = document.createElement("script");
    s.src = "https://bugdrop.neonwatty.workers.dev/widget.v1.59.1.js";
    s.dataset.repo = "TUDelft-MUDE/teacher";
    document.body.appendChild(s);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", load);
  } else {
    load();
  }
})();