"""Módulo de pruebas de penalización - Análisis estático Python (Flake8).

Score base: 100 pts (archivo limpio, sin errores).

Instrucciones:
  1. Ejecutar el análisis con este archivo tal como está → score 100.
  2. Descomentar SOLO UN bloque a la vez.
  3. Volver a ejecutar y verificar la penalización aplicada.
  4. Comentar el bloque nuevamente antes de probar el siguiente.
"""


def calculate_sum(first_value: int, second_value: int) -> int:
    """Return the sum of two integers."""
    return first_value + second_value


def get_version() -> str:
    """Return the application version string."""
    return "1.0"


# =============================================================================
# TIPO 1 | CRÍTICO | Regla: F401 | Penalización: -5 pts c/u
# Descripción: Módulo importado pero nunca utilizado en el archivo.
# Acción   : Descomentar las 2 líneas de import debajo.
# Esperado : 100 - 10 = 90 pts  (2 violaciones × -5 pts)
# =============================================================================
#import os
#import sys


# =============================================================================
# TIPO 2 | CRÍTICO | Regla: F841 | Penalización: -5 pts c/u
# Descripción: Variable local asignada pero cuyo valor nunca se usa.
# Acción   : Descomentar la función completa (4 líneas debajo).
# Esperado : 100 - 5 = 95 pts  (1 violación × -5 pts)
# =============================================================================
# def dead_variable_example() -> int:
#     """Función con variable local asignada pero sin uso."""
#     unused_result = calculate_sum(1, 2)
#     return 0


# =============================================================================
# TIPO 3 | INDENTACIÓN | Regla: W191 | Penalización: -1 pt c/u
# Descripción: Línea indentada con tabulador en lugar de espacios.
# Acción   : Descomentar las 2 líneas debajo.
#             IMPORTANTE: la segunda línea usa un TAB real — no reemplazar.
# Esperado : 100 - 1 = 99 pts  (1 violación × -1 pt)
# =============================================================================
# def tab_indented_function() -> bool:
# 	return True


# =============================================================================
# TIPO 4 | ESTILO | Regla: E225 | Penalización: -0.2 pts c/u
# Descripción: Falta espacio alrededor del operador de asignación/suma.
# Acción   : Descomentar la función completa (4 líneas debajo).
# Esperado : 100 - 0.4 = 99.6 pts  (2 violaciones × -0.2 pts)
# =============================================================================
def operator_no_spaces(value: int) -> int:
     """Sin espacios alrededor de operadores '=' y '+'."""
     result=value+1
     return result


# =============================================================================
# TIPO 5 | ESTILO | Regla: E231 | Penalización: -0.2 pts c/u
# Descripción: Falta espacio después de coma en lista de parámetros.
# Acción   : Descomentar la función completa (3 líneas debajo).
# Esperado : 100 - 0.4 = 99.6 pts  (2 violaciones × -0.2 pts)
# =============================================================================
# def comma_no_space(first: int,second: int,third: int) -> int:
#     """Sin espacio después de comas en la firma del método."""
#     return first + second + third
