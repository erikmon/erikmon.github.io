(() => {
  const root = document.documentElement;
  if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    root.classList.add("js-enter");
  }

  const filterButtons = Array.from(document.querySelectorAll("[data-filter]"));
  const cards = Array.from(document.querySelectorAll("[data-scope]"));
  const statusRegion = document.getElementById("filter-status");
  if (!filterButtons.length || !cards.length) return;

  const setFilter = (target) => {
    let matches = 0;
    filterButtons.forEach((btn) => {
      btn.setAttribute("aria-pressed", String(btn.dataset.filter === target));
    });

    cards.forEach((card) => {
      const scopes = (card.dataset.scope || "").split(/\s+/);
      const isMatch = target === "all" || scopes.includes(target);
      card.classList.toggle("is-dimmed", !isMatch);
      card.classList.toggle("is-highlighted", target !== "all" && isMatch);
      if (isMatch) matches += 1;
    });

    if (statusRegion) {
      statusRegion.textContent =
        target === "all"
          ? "Mostrando las 2 aplicaciones publicadas."
          : `${matches} aplicación${matches === 1 ? "" : "es"} compatible${matches === 1 ? "" : "s"} con la selección.`;
    }
  };

  filterButtons.forEach((btn) => {
    btn.addEventListener("click", () => setFilter(btn.dataset.filter || "all"));
  });
})();
