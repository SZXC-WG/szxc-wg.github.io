(() => {
  "use strict";
  const root = document.documentElement;
  const themeQuery = window.matchMedia("(prefers-color-scheme: dark)");
  const themeToggle = document.querySelector("[data-theme-toggle]");
  const storageKey = "localgen-theme";
  function savedTheme() {
    try {
      const value = localStorage.getItem(storageKey);
      return ["light", "dark"].includes(value) ? value : null;
    } catch {
      return null;
    }
  }
  function applyTheme(theme) {
    root.dataset.theme = theme;
    root.style.colorScheme = theme;
    document
      .querySelector('meta[name="theme-color"]')
      ?.setAttribute("content", theme === "dark" ? "#14171e" : "#ffffff");
    if (themeToggle) {
      const label =
        theme === "dark"
          ? themeToggle.dataset.labelDark
          : themeToggle.dataset.labelLight;
      themeToggle.setAttribute("aria-pressed", String(theme === "dark"));
      themeToggle.setAttribute(
        "aria-label",
        themeToggle.dataset.toggleLabel + " (" + label + ")",
      );
      themeToggle.title = themeToggle.getAttribute("aria-label");
    }
  }
  applyTheme(savedTheme() || (themeQuery.matches ? "dark" : "light"));
  themeToggle?.addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    try {
      localStorage.setItem(storageKey, next);
    } catch {
      /* The current page still updates. */
    }
    applyTheme(next);
  });
  themeQuery.addEventListener("change", (event) => {
    if (!savedTheme()) applyTheme(event.matches ? "dark" : "light");
  });
  window.addEventListener("storage", (event) => {
    if (event.key === storageKey)
      applyTheme(savedTheme() || (themeQuery.matches ? "dark" : "light"));
  });

  const navToggle = document.querySelector("[data-nav-toggle]");
  const navigation = document.querySelector("[data-site-navigation]");
  function closeNavigation(restoreFocus = false) {
    const wasOpen = navigation?.classList.contains("is-open");
    navigation?.classList.remove("is-open");
    navToggle?.setAttribute("aria-expanded", "false");
    if (restoreFocus && wasOpen) navToggle?.focus();
  }
  navToggle?.addEventListener("click", () => {
    const open = navigation.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", String(open));
  });
  navigation?.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeNavigation();
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeNavigation(true);
  });
  document.addEventListener("click", (event) => {
    if (
      !navigation?.contains(event.target) &&
      !navToggle?.contains(event.target)
    )
      closeNavigation();
  });
  window
    .matchMedia("(min-width: 801px)")
    .addEventListener("change", (event) => {
      if (event.matches) closeNavigation();
    });

  const docsMenu = document.querySelector(".docs-sidebar-disclosure");
  if (docsMenu) {
    const mobile = window.matchMedia("(max-width: 600px)");
    const updateMenu = () => {
      docsMenu.open = !mobile.matches;
    };
    updateMenu();
    mobile.addEventListener("change", updateMenu);
  }

  if (navigator.clipboard?.writeText) {
    document.querySelectorAll(".prose pre").forEach((pre) => {
      const code = pre.querySelector("code");
      if (!code) return;
      let wrapper = pre.closest(".highlight");
      if (!wrapper) {
        wrapper = document.createElement("div");
        wrapper.className = "code-block";
        pre.before(wrapper);
        wrapper.append(pre);
      }
      const button = document.createElement("button");
      button.type = "button";
      button.className = "code-copy-button";
      button.textContent = document.body.dataset.copyLabel;
      button.setAttribute("aria-label", document.body.dataset.copyLabel);
      const status = document.createElement("span");
      status.className = "sr-only";
      status.setAttribute("role", "status");
      button.addEventListener("click", async () => {
        try {
          await navigator.clipboard.writeText(code.textContent);
          button.textContent = document.body.dataset.copiedLabel;
          status.textContent = document.body.dataset.copiedLabel;
        } catch {
          button.textContent = document.body.dataset.copyFailedLabel;
          status.textContent = document.body.dataset.copyFailedLabel;
        }
        window.setTimeout(() => {
          button.textContent = document.body.dataset.copyLabel;
          status.textContent = "";
        }, 2000);
      });
      wrapper.append(button, status);
    });
  }
})();
