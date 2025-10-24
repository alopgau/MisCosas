> CLI que **suma** y **resta** números binarios de **1-8 bits**.

> **Salida exclusivamente en binario de 8 bits**

> Si no se indica signo, el programa ejecuta **ambas operaciones** (suma y resta).

---
## 1) Descripción del módulo

  

Este proyecto implementa una **calculadora binaria de 1-8 bits** que opera con **enteros sin signo**.

- Los **operandos** se introducen como **cadenas binarias** de **1-8 bits** (`0`/`1`).

- La **operación** se define por **signo**: `+` (suma) o `-` (resta).

- Si **no** se especifica el signo, el programa **realiza ambas operaciones** con los mismos operandos y muestra **dos bloques** de salida.

---
## 2) Requisitos

  

- **Python 3.10 o superior**.

- **Sin dependencias externas obligatorias.**
---
## 4) Ejecución del módulo

  

### Sintaxis general

```bash

python calculadorabinario.py OPERANDO1 OPERANDO2 [SIGNO]

```

- `OPERANDO1` y `OPERANDO2`: binarios de **1 a 8 bits**.

- `SIGNO` (opcional): `+` para **suma**, `-` para **resta**.

- Si **omites el signo**, el programa realiza **suma y resta** y muestra **dos bloques** de salida.

  

> En Windows puedes usar `py` en lugar de `python`.

> En Linux, si conviven varias versiones, usa `python3`.

---
### Ejemplos

**Suma explícita**

```bash
# Entrada esperada
# Linux/macOS
python3 calculadorabinario.py 01111111 01111111 +
# Windows
python calculadorabinario.py 01111111 01111111 +
# Salida esperada
01111111
+
01111111
---------
11111110
```

**Resta explícita**

```bash
# Entrada esperada
# Linux/macOS
python3 calculadorabinario.py 01111111 01111111 -
# Windows
python calculadorabinario.py 01111111 01111111 -
# Salida esperada
01111111
-
01111111
--------
00000000
```

**Sin signo (realiza ambas)**
```bash
# Entrada esperada
# Linux/macOS
python3 calculadorabinario.py 01111111 01111111
# Windows
python calculadorabinario.py 01111111 01111111
# Salida esperada
01111111
+
01111111
---------
11111110


01111111
-
01111111
--------
00000000
```
---
## 6) Mensajes de error y códigos de salida

  

- **Operando inválido** (no binario o no igual a 8 bits)

- Mensaje: `El formato del [primer,segundo,ambos] número(s) es incorrecto. Por favor, vuelve a introducirlo(s). (Debe ser binario y de 8 dígitos):`

- **Signo/operación inválida** (distinta de `+` o `-`)

- Mensaje: `Introduce una operación válida, o ninguna para realizar ambas (suma y resta, usando sus respectivos símbolos`
---
## 7) Problemas frecuentes (FAQ)

- **Formato de operando incorrecto** → Revisa que sean solo `0`/`1` y longitud ≤ 8.
- **Asegúrate de usar la siguiente estructura:** `OPERANDO1 OPERANDO2 [SIGNO]`.
