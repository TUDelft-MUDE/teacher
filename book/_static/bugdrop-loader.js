(function () {
  var FEEDBACK_SVG =
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="1em" height="1em" ' +
    'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" ' +
    'aria-hidden="true" class="bugdrop-feedback-icon">' +
    '<path d="M21 15a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>' +
    '<line x1="12" y1="7" x2="12" y2="11"/><line x1="12" y1="14" x2="12.01" y2="14"/></svg>';

  function loadBugDrop() {
    var s = document.createElement("script");
    s.src = "https://bugdrop.neonwatty.workers.dev/widget.v1.59.1.js";
    s.dataset.repo = "TUDelft-MUDE/teacher";
    s.dataset.button = "false"; // hide floating pill; we open from menu
    document.body.appendChild(s);
  }

  function swapGithubDropdownIcon() {
    // Replace the icon on the GitHub dropdown toggle button
    var icon =
      document.querySelector(".dropdown-source-buttons .fa-github") ||
      document.querySelector(".menu-dropdown-source-repository .fa-github") ||
      document.querySelector(".dropdown-buttons-trigger .fa-github");

    if (!icon || document.querySelector(".bugdrop-feedback-icon")) return;

    var wrap = document.createElement("span");
    wrap.innerHTML = FEEDBACK_SVG;
    icon.parentNode.replaceChild(wrap.firstChild, icon);
  }

  function addFeedbackItem() {
    if (document.querySelector(".btn-bugdrop-button")) return true;

    // Clone existing "open issue" item to preserve theme classes
    var issueBtn = document.querySelector(".btn-source-issues-button");
    var li = issueBtn && issueBtn.closest("li");
    if (!li) return false;

    var item = li.cloneNode(true);
    var a = item.querySelector("a");
    a.href = "#";
    a.removeAttribute("target");
    a.classList.remove("btn-source-issues-button");
    a.classList.add("btn-bugdrop-button");
    a.title = "Send feedback";

    var text = a.querySelector(".btn__text-container");
    if (text) text.textContent = "Send feedback";
    else a.textContent = "Send feedback";

    // Use your own hosted icon file in _static
    var feedbackIconUrl = "_static/icon_bugdrop.png";

    // Try to find existing icon container used by the theme
    var iconContainer = a.querySelector(".btn__icon-container");
    if (!iconContainer) {
    iconContainer = document.createElement("span");
    iconContainer.className = "btn__icon-container";
    a.insertBefore(iconContainer, a.firstChild);
    }

    // Replace icon content
    iconContainer.innerHTML = "";
    var img = document.createElement("img");
    img.src = feedbackIconUrl;
    img.alt = "";
    img.setAttribute("aria-hidden", "true");
    img.style.width = "1em";
    img.style.height = "1em";
    img.style.objectFit = "contain";
    img.style.verticalAlign = "text-bottom";
    iconContainer.appendChild(img);

    a.addEventListener("click", function (e) {
      e.preventDefault();
      window.BugDrop && window.BugDrop.open();
    });

    li.parentNode.insertBefore(item, li.nextSibling);
    return true;
  }

  function initMenuIntegration() {
    swapGithubDropdownIcon();

    if (!addFeedbackItem() && window.BugDrop && window.BugDrop.show) {
      // Fallback if menu selectors differ
      window.BugDrop.show();
    }
  }

  function start() {
    loadBugDrop();

    // Wait for widget API
    window.addEventListener("bugdrop:ready", function () {
      initMenuIntegration();
      // theme may render header a bit later
      setTimeout(initMenuIntegration, 400);
      setTimeout(initMenuIntegration, 1200);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
})();