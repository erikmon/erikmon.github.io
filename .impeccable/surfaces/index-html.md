---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: ["terretatrad/index.html","mdnote/index.html"]
---

# Surface Brief · Portfolio Erik Monsonís Pérez

- **Scope:** Portada (`/`) y fichas dedicadas (`/terretatrad/`, `/mdnote/`) compartiendo un único sistema visual en `styles.css`.
- **Visitor mode:** `experience`
- **Audience & job:** Reclutadores/equipos técnicos que evalúan criterio Android/KMP en segundos y usuarios finales que descargan TerretaTrad o mdNote en Google Play o acceden a la web oficial.
- **Primary actions:** Descargar en Google Play (`com.erikmp.terretatrad`, `com.erikmp.mdnote`), abrir `terretatrad.com`, inspeccionar fichas de proyecto y visitar LinkedIn.
- **Chosen direction:** Hoja Técnica Suiza (`r1-pick`), con inspección interactiva ligera de plataforma/especificación en JS vanilla progresivo (opcional, 100% funcional sin JS).
- **Constraints:** `lang="es"`, cero dependencias externas ni build step, `Erik Monsonís Pérez` en una línea en tamaños habituales, solo TerretaTrad y mdNote, iconos oficiales (`monograma.svg`, `terretatrad.webp`, `mdnote.webp`), sin fechas de iOS ni métricas inventadas, actualizar `tests/test_site.py` junto con el rediseño.

## Direction contract

THESIS: Sustituye el portfolio editorial crema/terracota por una hoja técnica suiza de especificación de producto donde Erik y sus dos aplicaciones reales se leen como expedientes de ingeniería verificables.

OWN-WORLD: Papel técnico frío (`#ECEFF3`), superficies limpias (`#F8FAFC`), tinta grafito (`#111418`), pizarra secundaria (`#525D6B`), filetes estructurales de 1px (`#BFC7D1`) y naranja de señalización (`#D94F1E`) reservado exclusivamente a lanzamientos vivos, links de ficha y foco; tipografía `Archivo` + `Golos Text` + `JetBrains Mono` solo para paquetes y specs.

STORY: El visitante reconoce en el primer pantallazo a un desarrollador Android/KMP serio, compara al instante `TerretaTrad` y `mdNote` con su estado real en tiendas y profundiza sin ruido en fichas y arquitectura.

FIRST VIEWPORT: Barra superior de ancho completo con monograma e índice (`Proyectos`, `Arquitectura`, `LinkedIn ↗`), titular de una línea (`Erik Monsonís Pérez`) sobre franja de tres columnas (resumen + 2 bloques clave-valor `Especialidad` y `Multiplataforma`) y debajo los dos expedientes técnicos paralelos con icono oficial, punto naranja de estado vivo, tabla clave-valor (`Paquete`, `Plataformas`) y acción primaria a Google Play.

FORM: 1 · Hoja Técnica Suiza · seed:27b2daba8e2e41c6

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance
