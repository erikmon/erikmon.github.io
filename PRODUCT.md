# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Público dual con igual prioridad:

1. **Reclutadores, tech leads y clientes potenciales** que evalúan el criterio técnico, la arquitectura y la calidad de producto de Erik Monsonís Pérez como desarrollador de aplicaciones.
2. **Usuarios finales** que llegan para conocer, evaluar y descargar sus aplicaciones publicadas (**TerretaTrad** y **mdNote**) en Google Play o acceder a su versión web.

## Product Purpose

Portfolio personal y escaparate independiente de aplicaciones de **Erik Monsonís Pérez** (`erikmon.github.io`). Presenta su perfil profesional como desarrollador de aplicaciones especializado en Android —sin limitar su trabajo únicamente a esa plataforma, con evolución activa hacia iOS y web— y ofrece acceso directo y fichas técnicas detalladas para cada producto propio publicado.

## Positioning

Desarrollador móvil independiente que combina criterio de ingeniería nativo (Android, Kotlin, Jetpack Compose, Clean Architecture) con lógica multiplataforma compartida (Kotlin Multiplatform) y lo demuestra con productos propios publicados, rápidos, claros y sin fricción.

## Operating Context

- Sitio estático alojado en GitHub Pages (`erikmon.github.io`), íntegramente en español (`lang="es"`).
- Flujo principal desde la portada (`/`) hacia las fichas dedicadas (`/terretatrad/` y `/mdnote/`), las fichas externas en Google Play, la web oficial `terretatrad.com` y el perfil profesional en LinkedIn.
- Verificación automatizada local mediante `python3 -B -m unittest discover -s tests` (`tests/test_site.py`).

## Capabilities and Constraints

- **Stack de ejecución:** HTML estático y CSS compartido (`styles.css`), permitiendo JavaScript vanilla mínimo sin dependencias externas ni paso de compilación/build. *(Nota: `tests/test_site.py` actualmente prohíbe `<script>` y comprueba tokens de la paleta anterior; deberán actualizarse junto con el rediseño).*
- **Rutas y archivos de verificación:** Mantener intactas las rutas `/`, `/terretatrad/`, `/mdnote/` y los archivos raíz `app-ads.txt` y `googlea2b8e85e238fd56b.html`.
- **Veracidad estricta:** No anunciar fechas de lanzamiento ni disponibilidad no confirmada en tiendas (iOS figura únicamente como *en desarrollo / próximamente*). No reintroducir proyectos retirados (como `ML Node`) ni inventar métricas, reseñas o testimonios.
- **Identificadores y enlaces oficiales:** Conservar `com.erikmp.terretatrad`, `com.erikmp.mdnote`, sus enlaces a Google Play, `https://terretatrad.com/` y `https://www.linkedin.com/in/erikmonsonisperez/`.
- **Restricción tipográfica de portada:** El nombre completo (`Erik Monsonís Pérez`) debe mantenerse en una sola línea en tamaños de pantalla habituales.

## Brand Commitments

- **Nombre:** Erik Monsonís Pérez.
- **Marca y favicon:** `assets/monograma.svg` en todas las páginas; conservar `assets/developer-icon.png` (512×512 RGBA) y `assets/developer-header.png` (4096×2304 RGB) para Google Play.
- **Iconos oficiales de producto:** `assets/terretatrad.webp` y `assets/mdnote.webp` en las tarjetas y fichas de proyecto.
- **Tono:** Directo, técnico y sobrio; claridad editorial sin ruido visual ni promesas infladas.

## Evidence on Hand

- **TerretaTrad** (`com.erikmp.terretatrad`, icono `assets/terretatrad.webp`): Traductor bidireccional castellano ↔ valenciano con corrección ortográfica y gramatical previa según normativa valenciana, historial local y traducciones guardadas. Disponible en Google Play y en `https://terretatrad.com/`; iOS en desarrollo.
- **mdNote** (`com.erikmp.mdnote`, icono `assets/mdnote.webp`): Editor ligero de notas y documentos Markdown sobre archivos `.md` locales en texto plano, con vista previa enriquecida en tiempo real, autoguardado y exportación a Markdown, texto plano, HTML o PDF. Disponible en Google Play; iOS en desarrollo.
- **Perfil profesional:** `https://www.linkedin.com/in/erikmonsonisperez/`.
- **Ausencias confirmadas (no inventar):** No hay capturas de pantalla reales de las apps en `assets/`, ni métricas de descargas, reseñas de usuarios, enlaces a GitHub o correo público en el repositorio.

## Product Principles

1. **Doble claridad desde el primer pantallazo:** Identidad profesional y acceso directo a las dos aplicaciones publicadas sin obligar a buscar.
2. **Solo hechos verificables:** Cada texto, estado de plataforma y capacidad corresponde a producto real en producción o en desarrollo confirmado.
3. **Cero dependencias de ejecución:** Entrega estática rápida con HTML semántico, CSS compartido y JS vanilla solo cuando aporte interacción real.
4. **Integridad de rutas y activos:** Conservar URLs públicas, enlaces de tienda, verificación de Google Play y recursos gráficos oficiales.

## Accessibility & Inclusion

- HTML semántico con jerarquía clara de encabezados, foco visible por teclado (`:focus-visible`), contraste legible y respeto a `prefers-reduced-motion`.
