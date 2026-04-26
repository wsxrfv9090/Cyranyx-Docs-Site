(function () {
  "use strict";

  var LANGS = {
    en: { label: "English", targetLabel: "中文" },
    zh: { label: "中文", targetLabel: "English" },
  };

  var remountTimer = null;

  function normalizePath(pathname) {
    return pathname.replace(/\\/g, "/");
  }

  function findLanguage(pathname) {
    var normalized = normalizePath(pathname);
    var match = normalized.match(/(?:^|\/)\b(en|zh)\b(?:\/|$)/);
    return match ? match[1] : "en";
  }

  function outputKey(pathname) {
    var normalized = normalizePath(pathname);
    var parts = normalized.split("/").filter(Boolean);
    var langIndex = parts.findIndex(function (part) {
      return part === "en" || part === "zh";
    });

    if (langIndex < 0) {
      return "en/index.html";
    }

    var tail = parts.slice(langIndex).join("/");
    if (tail.endsWith("/")) {
      return tail + "index.html";
    }
    if (!tail.endsWith(".html")) {
      return tail + "/index.html";
    }
    return tail;
  }

  function pathPrefixToLangRoot(pathname, lang) {
    var normalized = normalizePath(pathname);
    var marker = "/" + lang + "/";
    var index = normalized.indexOf(marker);

    if (index >= 0) {
      return normalized.slice(0, index + 1);
    }

    var parts = normalized.split("/");
    var langIndex = parts.findIndex(function (part) {
      return part === "en" || part === "zh";
    });

    if (langIndex >= 0) {
      return parts.slice(0, langIndex).join("/") + "/";
    }

    return "";
  }

  function isVisible(element) {
    if (!element) {
      return false;
    }

    var style = window.getComputedStyle(element);
    if (
      style.display === "none" ||
      style.visibility === "hidden" ||
      style.opacity === "0"
    ) {
      return false;
    }

    var rect = element.getBoundingClientRect();
    return rect.width > 0 && rect.height > 0;
  }

  function findVisibleThemeToggle() {
    var selectors = [
      ".theme-toggle-container",
      "button.theme-toggle",
      ".theme-toggle",
      "[data-theme-toggle]",
      "[aria-label*='theme' i]",
      "[title*='theme' i]",
    ];

    var candidates = [];

    selectors.forEach(function (selector) {
      document.querySelectorAll(selector).forEach(function (element) {
        if (!candidates.includes(element)) {
          candidates.push(element);
        }
      });
    });

    var visibleCandidates = candidates.filter(isVisible);

    if (visibleCandidates.length > 0) {
      return visibleCandidates[0];
    }

    return candidates[candidates.length - 1] || null;
  }

  function createOrUpdateButton() {
    var currentLang = findLanguage(window.location.pathname);
    var targetLang = currentLang === "zh" ? "en" : "zh";

    var button = document.querySelector(".cyranyx-lang-switch");

    if (!button) {
      button = document.createElement("a");
      button.className = "cyranyx-lang-switch";
      button.href = "#";
      button.setAttribute("aria-label", "Switch language");

      button.addEventListener("click", function (event) {
        event.preventDefault();

        var current = button.getAttribute("data-current-lang") || findLanguage(window.location.pathname);
        var target = button.getAttribute("data-target-lang") || (current === "zh" ? "en" : "zh");

        switchLanguage(current, target);
      });
    }

    button.setAttribute("data-current-lang", currentLang);
    button.setAttribute("data-target-lang", targetLang);
    button.textContent = LANGS[currentLang]
      ? LANGS[currentLang].targetLabel
      : LANGS.en.targetLabel;

    mountButton(button);
  }

  function mountButton(button) {
    var themeToggle = findVisibleThemeToggle();

    if (themeToggle) {
      var mountTarget = themeToggle;

      if (
        themeToggle.classList.contains("theme-toggle") ||
        themeToggle.tagName.toLowerCase() === "button"
      ) {
        mountTarget = themeToggle.parentElement || themeToggle;
      }

      if (mountTarget.parentElement && isVisible(mountTarget.parentElement)) {
        mountTarget.parentElement.classList.add("cyranyx-header-control-row");
        button.classList.remove("cyranyx-lang-switch--fallback-fixed");
        button.classList.add("cyranyx-lang-switch--inline");
        mountTarget.parentElement.insertBefore(button, mountTarget);
        return;
      }
    }

    var headerArea =
      document.querySelector(".article-header-buttons") ||
      document.querySelector(".content-icon-container") ||
      document.querySelector(".top-right-area") ||
      document.querySelector(".header-article") ||
      document.querySelector("header");

    if (headerArea && isVisible(headerArea)) {
      headerArea.classList.add("cyranyx-header-control-row");
      button.classList.remove("cyranyx-lang-switch--fallback-fixed");
      button.classList.add("cyranyx-lang-switch--inline");
      headerArea.insertBefore(button, headerArea.firstChild);
      return;
    }

    button.classList.remove("cyranyx-lang-switch--inline");
    button.classList.add("cyranyx-lang-switch--fallback-fixed");
    document.body.appendChild(button);
  }

  function scheduleRemount() {
    window.clearTimeout(remountTimer);
    remountTimer = window.setTimeout(createOrUpdateButton, 120);
  }

  function switchLanguage(currentLang, targetLang) {
    fetchStaticJson("lang-map.json")
      .then(function (payload) {
        var key = outputKey(window.location.pathname);
        var target = payload && payload.map ? payload.map[key] : null;

        if (!target) {
          target = targetLang + "/index.html";
        }

        var prefix = pathPrefixToLangRoot(window.location.pathname, currentLang);
        window.location.href = prefix + target;
      })
      .catch(function () {
        var prefix = pathPrefixToLangRoot(window.location.pathname, currentLang);
        window.location.href = prefix + targetLang + "/index.html";
      });
  }

  function fetchStaticJson(filename) {
    var scripts = document.getElementsByTagName("script");
    var currentScript = scripts[scripts.length - 1];
    var src = currentScript && currentScript.src ? currentScript.src : "";
    var url = src ? src.replace(/[^/]+$/, filename) : "_static/" + filename;

    return fetch(url, { cache: "no-cache" }).then(function (response) {
      if (!response.ok) {
        throw new Error("Failed to load " + filename);
      }
      return response.json();
    });
  }

  function observeHeaderChanges() {
    var observer = new MutationObserver(function () {
      scheduleRemount();
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ["class", "style", "data-theme"],
    });
  }

  function init() {
    createOrUpdateButton();

    window.setTimeout(createOrUpdateButton, 150);
    window.setTimeout(createOrUpdateButton, 500);

    window.addEventListener("resize", scheduleRemount);
    window.addEventListener("orientationchange", scheduleRemount);

    observeHeaderChanges();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();