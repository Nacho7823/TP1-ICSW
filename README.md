# TP1-ICSW — Calculadora Básica

Trabajo Práctico Integrador — *Sistemas de Gestión de la Configuración*.

## Instalación

```bash
git clone https://github.com/Nacho7823/TP1-ICSW.git
cd TP1-ICSW
```

## Uso

```bash
python calculadora.py
```

Menú: sumar, restar, multiplicar, dividir, potencia, raíz cuadrada, residuo.

## Tests

```bash
pytest -v
```

La CI (`.github/workflows/ci.yml`) corre estos tests en cada **Pull Request** y en cada **push a `main` o `develop`**.

## Estructura del repo

```
calculadora.py            # software
test_calculadora.py       # tests (pytest)
.github/CODEOWNERS        # responsables de revisión
.github/workflows/ci.yml  # CI
.gitignore                # archivos locales que NO se suben
```

---

## 8.1 — ¿Qué documentaríamos en el README? ¿Cómo versionarlo?

Qué documentar:

1. Qué es y para qué sirve el proyecto
2. Requisitos e instalación
3. Uso: cómo ejecutarlo, ejemplos y salida esperada
4. Cómo correr los tests y qué cubren
5. Estructura del repositorio y propósito de cada archivo
6. Estado/versionado: versión actual, changelog o historial de releases
7. Autores, licencia y cómo contribuir

Cómo versionarlo: el README es un archivo *trackeado* por git. Cualquier cambio se hace en una rama (`docs/readme-*`), se commitea con un mensaje claro (`docs: actualiza README`) y se mergea mediante PR hacia `develop`. Así GitHub guarda el historial, se puede ver quién cambió qué con `git blame`/`git log --follow`, y el contenido del README en `main` siempre corresponde a la última release.

## 8.2 — Si un externo modifica el código, ¿qué le pedimos? ¿Qué ofrece GitHub?

Datos que le pediría que complete en el PR:

1. Título descriptivo siguiendo Conventional Commits: `feat:`, `fix:`, `docs:`, `refactor:`.
2. Issue que resuelve (o descripción del problema): qué cambia y por qué.
3. Cómo probarlo: pasos exactos y resultado esperado.
4. Impacto y riesgos: qué más puede afectar, si cambia una firma pública o la configuración.
5. Diseño/alternativas: qué otras soluciones consideró y por qué descartó.
6. Checklist: tests nuevos/actualizados, documentación al día, ningún archivo local subido (`.gitignore` respetado).

Qué nos ofrece GitHub para ayudar:

- Plantilla de Pull Request (`.github/PULL_REQUEST_TEMPLATE.md`) para forzar esos campos.
- Descripción en Markdown y edición de commits antes del merge.
- CODEOWNERS + revisores obligatorios: asigna automáticamente quién debe aprobar.
- Checks/CI obligatorios: no se puede mergear si los tests fallan.
- Comentarios anclados a líneas específicas del diff y sugerencias.
- Labels, milestone y asignados para organizar el trabajo.
- Comparación de ramas (`compare`), historial completo, `git blame` y revert con un clic.
- Protección de ramas: impedir merges sin aprobación y sin historial lineal limpio.
