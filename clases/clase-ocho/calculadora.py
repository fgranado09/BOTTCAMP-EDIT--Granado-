"""
Operaciones aritméticas básicas con validación estricta de operandos.

La API pública declara solo ``int | float``. Las funciones internas de validación
reciben ``object`` a propósito: modelan datos aún no garantizados y los reducen
a un ``float`` finito o lanzan error; el comprobador estático puede seguir ese
estrechamiento gracias a :func:`_es_int_o_float_permitido`.
"""

from __future__ import annotations

import math
from typing import TypeGuard

__all__ = ["PI", "sumar", "restar", "multiplicar", "dividir"]

# Constante π definida en términos de la biblioteca estándar (doble precisión IEEE 754).
PI: float = math.pi


def _es_int_o_float_permitido(valor: object) -> TypeGuard[int | float]:
    """
    True solo para ``int`` y ``float``, excluyendo ``bool`` (subclase de ``int``).

    Debe usarse después de descartar ``None`` y ``complex`` si aplica al flujo.
    """
    if isinstance(valor, bool):
        return False
    return isinstance(valor, (int, float))


def _validar_operando(nombre: str, valor: object) -> float:
    """
    Normaliza el operando a ``float`` finito o lanza ``TypeError`` / ``ValueError``.

    El tipo ``object`` marca la frontera de validación: aquí puede llegar cualquier
    valor en tiempo de ejecución; la API pública sigue restringida a ``int | float``.
    """
    if isinstance(valor, bool):
        raise TypeError(
            f"{nombre}: no se aceptan valores booleanos; use int o float explícitos."
        )
    if valor is None:
        raise TypeError(f"{nombre}: no se admite None.")
    if isinstance(valor, complex):
        raise TypeError(f"{nombre}: no se admiten números complejos.")
    if not _es_int_o_float_permitido(valor):
        raise TypeError(
            f"{nombre}: se esperaba int o float, se obtuvo {type(valor).__name__}."
        )
    x = float(valor)
    if math.isnan(x):
        raise ValueError(f"{nombre}: NaN no es un valor válido.")
    if math.isinf(x):
        raise ValueError(f"{nombre}: infinito no es un valor válido.")
    return x


def _resultado_finito(nombre: str, resultado: float) -> float:
    if math.isnan(resultado):
        raise OverflowError(f"{nombre}: el resultado es NaN (operación no definida o inestable).")
    if math.isinf(resultado):
        raise OverflowError(
            f"{nombre}: el resultado excede el rango representable (desbordamiento)."
        )
    return resultado


def _es_int_seguro(a: float, b: float, r: float) -> bool:
    if not a.is_integer() or not b.is_integer() or not r.is_integer():
        return False
    ia, ib, ir = int(a), int(b), int(r)
    return float(ia) == a and float(ib) == b and float(ir) == r


def sumar(a: int | float, b: int | float) -> int | float:
    """
    Suma dos números. Devuelve ``int`` si ambos operandos y el resultado son enteros
    exactos; en caso contrario, ``float``.
    """
    x = _validar_operando("sumar: primer operando (a)", a)
    y = _validar_operando("sumar: segundo operando (b)", b)
    r = _resultado_finito("sumar", x + y)
    if _es_int_seguro(x, y, r):
        return int(r)
    return r


def restar(a: int | float, b: int | float) -> int | float:
    """Resta ``b`` de ``a``. Misma convención de tipo de retorno que ``sumar``."""
    x = _validar_operando("restar: primer operando (a)", a)
    y = _validar_operando("restar: segundo operando (b)", b)
    r = _resultado_finito("restar", x - y)
    if _es_int_seguro(x, y, r):
        return int(r)
    return r


def multiplicar(a: int | float, b: int | float) -> int | float:
    """Producto de ``a`` y ``b``. Misma convención de tipo de retorno que ``sumar``."""
    x = _validar_operando("multiplicar: primer operando (a)", a)
    y = _validar_operando("multiplicar: segundo operando (b)", b)
    r = _resultado_finito("multiplicar", x * y)
    if _es_int_seguro(x, y, r):
        return int(r)
    return r


def dividir(a: int | float, b: int | float) -> float:
    """
    Cociente ``a / b``. Siempre retorna ``float``.

    El divisor no puede ser cero. Se validan ambos operandos como en las demás funciones.
    """
    x = _validar_operando("dividir: dividendo (a)", a)
    y = _validar_operando("dividir: divisor (b)", b)
    if y == 0.0:
        raise ZeroDivisionError("dividir: división por cero no está definida.")
    r = x / y
    return _resultado_finito("dividir", r)
