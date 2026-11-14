---
name: Erik Monsonís Pérez · Hoja Técnica Suiza
description: Sistema visual de hoja técnica suiza para portfolio editorial de ingeniería móvil y fichas de producto.
colors:
  primary: "#b53a0e"
  primary-signal: "#d94f1e"
  primary-deep: "#962e09"
  neutral-ground: "#eceff3"
  neutral-surface: "#f8fafc"
  neutral-surface-alt: "#e2e7ee"
  neutral-ink: "#111418"
  neutral-prose: "#2c3540"
  neutral-muted: "#475260"
  rule-structural: "#bfc7d1"
  rule-hairline: "#d8dfe8"
typography:
  display:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(1.55rem, 8.1cqi, 5.15rem)"
    fontWeight: 800
    lineHeight: 0.96
    letterSpacing: "-0.035em"
  headline:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(1.4rem, 1.15rem + 1.1vw, 2rem)"
    fontWeight: 800
    lineHeight: 1.12
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(1.06rem, 1.2vw, 1.85rem)"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Golos Text, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.58
    letterSpacing: "0em"
  label:
    fontFamily: "JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: "0.78rem"
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: "0.04em"
rounded:
  none: "0"
  brand-mark: "7px"
  app-icon: "22%"
  dot: "50%"
spacing:
  gutter: "clamp(1rem, 4.2vw, 3.5rem)"
  row: "0.65rem 0"
  control: "0.5rem 0.85rem"
  sheet: "1.75rem"
  grid-gap: "1.5rem"
components:
  button-primary:
    backgroundColor: "{colors.neutral-ink}"
    textColor: "{colors.neutral-surface}"
    rounded: "{rounded.none}"
    padding: "0.45rem 1rem"
    height: "46px"
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral-surface}"
  button-secondary:
    backgroundColor: "{colors.neutral-ground}"
    textColor: "{colors.neutral-ink}"
    rounded: "{rounded.none}"
    padding: "0.45rem 1rem"
    height: "46px"
  chip-segmented:
    backgroundColor: "{colors.neutral-surface}"
    textColor: "{colors.neutral-muted}"
    rounded: "{rounded.none}"
    padding: "0.5rem 0.85rem"
    height: "44px"
  chip-segmented-active:
    backgroundColor: "{colors.neutral-ink}"
    textColor: "{colors.neutral-surface}"
  dossier-card:
    backgroundColor: "{colors.neutral-surface}"
    textColor: "{colors.neutral-ink}"
    rounded: "{rounded.none}"
    padding: "1.75rem"
  nav-link:
    textColor: "{colors.neutral-muted}"
    height: "44px"
---

# Design System: Erik Monsonís Pérez · Hoja Técnica Suiza

## Overview

**Creative North Star: "Hoja Técnica Suiza"**

Este sistema trata cada pantalla como un pliego de especificación técnica impreso en mesa de dibujo fría. La jerarquía se apoya en contraste tipográfico de gran escala, líneas estructurales continuas y separación limpia entre campo gris de trabajo y fichas blancas sin ornamento.

Las decisiones visuales evitan sombras proyectadas, degradados decorativos, tarjetas anidadas y rejillas genéricas de cajas iguales. La lectura técnica y las acciones hacia tienda conviven al mismo nivel visual mediante una retícula disciplinada, esquinas rectas y acento naranja restringido a puntos vivos y enlaces de acción.

**Key Characteristics:**
- Campo frío de papel técnico combinado con láminas blancas de bordes rectos y reglas de 1px.
- Titular principal en una sola línea adaptado por contenedor, acompañado de metadatos monoespaciados estrictos.
- Tablas de especificaciones abiertas con divisores horizontales finos en lugar de cajas encapsuladas.
- Cero sombras, cero desenfoques y una única entrada de asentamiento inicial desactivable bajo `prefers-reduced-motion`.

## Colors

Paleta de alto contraste basada en grises fríos de planos técnicos y un único acento naranja reservado para estado en producción y navegación directa.

### Primary
- **Signal Rust Ink** (`#b53a0e`): Texto de enlaces de ficha, valores vivos en arquitectura y contornos de foco (`outline: 2px`) con contraste superior a 4.5:1 sobre superficies claras.
- **Signal Orange Dot** (`#d94f1e`): Reservado exclusivamente para el indicador circular de 8px de disponibilidad activa y bordes de tarjeta resaltada.
- **Pressed Rust Ink** (`#962e09`): Estado hover de enlaces en naranja para reforzar respuesta táctil sin cambiar de tono.

### Neutral
- **Drafting Gray Ground** (`#eceff3`): Lienzo base de todo el documento y fondo de botones secundarios.
- **Technical Sheet White** (`#f8fafc`): Superficie de láminas principales, fichas de proyecto, diagrama arquitectónico y tablas de disponibilidad.
- **Recessed Spec Field** (`#e2e7ee`): Fondo sutil para etiquetas de código en línea y estado hover de controles secundarios.
- **Graphite Ink** (`#111418`): Títulos principales, botones primarios, filtros activos y texto de valores técnicos.
- **Body Charcoal** (`#2c3540`): Párrafos descriptivos principales y resúmenes de producto para lectura cómoda.
- **Slate Metadata** (`#475260`): Navegación superior, claves de tabla técnica, textos auxiliares y pie de página.
- **Structural Rule** (`#bfc7d1`): Bordes de 1px en cabecera, portada, fichas completas y botones secundarios.
- **Hairline Divider** (`#d8dfe8`): Divisores internos de 1px entre filas de especificación y columnas arquitectónicas.

### Named Rules
**The Signal Restraint Rule.** El acento naranja aparece solo en indicadores de estado activo, enlaces de detalle y foco; nunca en fondos completos ni títulos decorativos.
**The Verified Contrast Rule.** Todo texto naranja interactivo utiliza **Signal Rust Ink** (`#b53a0e`), nunca **Signal Orange Dot** (`#d94f1e`), garantizando legibilidad WCAG AA sobre blanco y gris técnico.

## Typography

**Display Font:** `Archivo` (`sans-serif` de respaldo)
**Body Font:** `Golos Text` (`-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`)
**Label/Mono Font:** `JetBrains Mono` (`ui-monospace, SFMono-Regular, Menlo, monospace`)

**Character:** Titulares rotundos y compactos en `Archivo` 800 combinados con prosa técnica directa en `Golos Text`, dejando `JetBrains Mono` estrictamente para identificadores de paquete, estados y etiquetas de tabla.

### Hierarchy
- **Display** (`800`, `clamp(1.55rem, 8.1cqi, 5.15rem)`, `line-height: 0.96`): Nombre completo en portada dentro de una sola línea a anchos habituales (`letter-spacing: -0.035em`).
- **Headline** (`800`, `clamp(1.4rem, 1.15rem + 1.1vw, 2rem)`, `line-height: 1.12`): Títulos de sección y encabezados principales de cada ficha de aplicación (`letter-spacing: -0.03em`).
- **Title** (`700–800`, `clamp(1.06rem, 1.2vw, 1.85rem)`, `line-height: 1.1`): Nombres de proyecto dentro de tarjetas y subtítulos de bloques técnicos.
- **Body** (`400`, `1rem`, `line-height: 1.58`): Prosa descriptiva de portada, resúmenes de ficha y explicaciones funcionales con anchura máxima de `65ch`.
- **Label** (`500`, `0.78rem–0.8125rem`, `letter-spacing: 0.04em`): Claves técnicas en mayúsculas, nombres de paquete (`com.erikmp.*`) y estados de disponibilidad.

### Named Rules
**The Mono Discipline Rule.** `JetBrains Mono` se limita exclusivamente a metadatos técnicos, nombres de paquete e indicadores de estado; los controles de filtro y enlaces de regreso utilizan `Golos Text`.
**The Single-Line Masthead Rule.** El título `Erik Monsonís Pérez` utiliza unidades de contenedor (`cqi`) con `white-space: nowrap` para mantenerse en una línea desde escritorio hasta móvil estándar.

## Layout

Contenedor único centrado de anchura máxima `76rem` con márgenes laterales fluidos (`--gutter: clamp(1rem, 4.2vw, 3.5rem)`). En escritorio la portada reparte descripción y dos celdas técnicas en proporción `1.55fr 1fr 1fr`, los proyectos forman dos columnas simétricas con separación de `1.5rem`, y las secciones secundarias de arquitectura y funcionalidades emplean columnas abiertas separadas por filetes superiores de `1px solid` sin cajas contenedoras. En tablet (`<= 60rem`) las rejillas colapsan a una columna manteniendo todo el bloque a ancho completo; en móvil (`<= 36rem`) los botones de tienda ocupan `100%` y las tablas clave-valor apilan etiqueta sobre valor.

## Elevation & Depth

Sistema estrictamente plano sin `box-shadow`, `radial-gradient` ni `backdrop-filter`. La profundidad jerárquica se resuelve mediante cambio tonal directo entre el lienzo base `#eceff3` y las láminas `#f8fafc`, reforzado por bordes continuos de `1px solid` (`#bfc7d1` exterior y `#d8dfe8` interior).

### Named Rules
**The Zero-Shadow Rule.** Ningún contenedor ni botón proyecta sombra en reposo o hover; el estado hover se comunica por desplazamiento sutil (`translateY(-2px)` en fichas, `translateY(-1px)` en acciones) y cambio de color de borde a `#111418`.
**The Flat-Sheet Rule.** Quedan prohibidas las cajas bordeadas anidadas dentro de otra caja; las tablas internas utilizan únicamente filetes horizontales o verticales abiertos de `1px solid`.

## Shapes

Geometría ortogonal de esquinas rectas (`border-radius: 0`) en todos los paneles estructurales, segmentos de filtro, botones, tablas de especificación y fragmentos `<code>`. Las únicas curvas del sistema corresponden al recorte de icono de aplicación Android (`22%`), al marco del monograma SVG (`7px`) y al punto circular de estado activo (`50%`, `8px × 8px`).

## Components

### Buttons
Botones rectangulares de borde limpio con área táctil mínima de `46px` de altura e icono integrado de `20px–22px`.
- **Shape:** Rectángulo afilado (`border-radius: 0`), borde `1px solid`.
- **Primary:** Fondo **Graphite Ink** (`#111418`), texto **Technical Sheet White** (`#f8fafc`), padding `0.45rem 1rem`.
- **Hover / Focus:** Fondo cambia a **Signal Rust Ink** (`#b53a0e`) con ligero ascenso vertical (`translateY(-1px)`); foco mediante contorno externo `2px solid #b53a0e` separado `2px`.
- **Secondary:** Fondo **Drafting Gray Ground** (`#eceff3`), texto `#111418`, borde `#bfc7d1`; en hover cambia a fondo `#e2e7ee` y borde `#111418`. Estado pasivo iOS usa borde discontinuo (`border-style: dashed`) y no es interactivo.

### Chips
Barra segmentada unificada de filtro discriminante con tres estados mutuamente exclusivos (`Todas (2)`, `Con web (1)`, `Solo móvil (1)`).
- **Style:** Contenedor horizontal sin envoltorio en dos líneas (`flex-wrap: nowrap`), fondo `#f8fafc`, borde exterior `1px solid #bfc7d1` y divisores verticales internos de `1px solid #bfc7d1`; tipografía `Golos Text` `0.85rem`.
- **State:** Botón inactivo en texto `#475260`; hover sobre `#e2e7ee`; estado seleccionado (`aria-pressed="true"`) invertido con fondo `#111418` y texto `#f8fafc`.

### Cards / Containers
Fichas técnicas modulares alineadas a la retícula de `76rem` con separación clara entre cabecera, cuerpo abierto y pie de acciones.
- **Corner Style:** Esquinas rectas (`border-radius: 0`).
- **Background:** `#f8fafc` sobre lienzo `#eceff3`.
- **Shadow Strategy:** Plano (`0` sombras), transición de borde a `#111418` en hover.
- **Border:** `1px solid #bfc7d1`; tarjetas atenuadas por filtro reducen opacidad a `0.42` y la activa resalta borde con `#d94f1e`.
- **Internal Padding:** `1.75rem` en escritorio y `1.35rem` en móvil (`<= 36rem`); tablas clave-valor internas abiertas con filetes horizontales `#d8dfe8` y `0.65rem` de respiro vertical sin caja interior.

### Navigation
Cabecera horizontal única con monograma SVG de marca (`34px`) junto a identificador de hoja (`Archivo` 700 en mayúsculas) y enlaces derechos en `Golos Text` (`0.9rem`, altura mínima `44px`) con subrayado animado por escala horizontal desde la izquierda en hover y foco.

### Signature Component: Ruled Architectural & Spec Ledgers
Diagrama horizontal de arquitectura multiplataforma (`.arch-flow`) y rejillas editoriales de principios/funcionalidades (`.pillars-ledger` y `.feature-ledger`) que sustituyen rejillas de cajas iguales por columnas abiertas con filetes superiores de `1px solid` o divisores internos continuos sin recuadros anidados.

## Do's and Don'ts

### Do:
- **Do** mantener todas las láminas, tablas de disponibilidad y cabeceras de detalle alineadas al mismo ancho de columna (`76rem`) para conservar bordes iguales.
- **Do** usar filetes horizontales de `1px solid #d8dfe8` para tablas de especificaciones dentro de tarjetas en lugar de crear subcajas con fondo propio.
- **Do** desactivar transiciones y la animación de entrada `dossier-enter` bajo `@media (prefers-reduced-motion: reduce)`.

### Don't:
- **Don't** anidar elementos con borde y fondo distinto dentro de otro contenedor con borde.
- **Don't** aplicar `JetBrains Mono` a botones de filtro ni enlaces de navegación conversacional; utilízalo solo en paquetes, claves y métricas técnicas.
- **Don't** reintroducir tarjetas uniformes con esquinas redondeadas para secciones puramente informativas ni filtros con múltiples opciones que devuelvan resultados idénticos.
