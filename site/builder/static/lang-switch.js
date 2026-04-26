(function () {
  "use strict";

  var LANGS = {
    en: { label: "English", targetLabel: "中文" },
    zh: { label: "中文", targetLabel: "English" },
  };

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

  function createButton() {
    var currentLang = findLanguage(window.location.pathname);
    var targetLang = currentLang === "zh" ? "en" : "zh";

    var button = document.createElement("a");
    button.className = "cyranyx-lang-switch";
    button.href = "#";
    button.setAttribute("data-current-lang", currentLang);
    button.setAttribute("data-target-lang", targetLang);
    button.setAttribute("aria-label", "Switch language");
    button.textContent = LANGS[currentLang]
      ? LANGS[currentLang].targetLabel
      : LANGS.en.targetLabel;

    button.addEventListener("click", function (event) {
      event.preventDefault();
      switchLanguage(currentLang, targetLang);
    });

    document.body.appendChild(button);
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

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", createButton);
  } else {
    createButton();
  }
})();
