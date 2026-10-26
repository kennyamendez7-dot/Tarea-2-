# Tarea 2: Sistema de Inventario de una Tienda
**Curso:** Principios de Programación  
**Estudiante:** Kennya Mendez Castro  

## Descripción del Proyecto
Este repositorio contiene la solución programada en Python para el **Problema 3: Inventario de una tienda**. El objetivo principal del programa es permitir el registro sistemático y controlado de artículos comerciales en un inventario digital, aplicando conceptos fundamentales de programación imperativa como variables, constantes, flujos secuenciales, condicionales anidados y ciclos controlados por el usuario.

## Características del Programa
* **Ciclo Iterativo Controlado (`while`):** Permite el ingreso continuo de artículos hasta que el operador decida finalizar el proceso (entrada `s/n`).
* **Validación Crítica de Datos:** Bloquea de inmediato el registro y cálculo de cualquier producto cuyo precio unitario sea menor o igual a cero (`price <= 0`), evitando la alteración de los acumuladores financieros.
* **Control de Stock Mínimo:** Evalúa de forma automática si las existencias físicas son inferiores al límite establecido por la constante (`MIN_STOCK = 5`), emitiendo una alerta de reposición.
* **Módulo de Confirmación:** Implementa un paso de verificación (`confirmChoice`) que asegura que el producto solo se sume oficialmente al inventario global si el usuario valida los datos previamente digitados.
* **Reporte Estadístico Final:** Al romper el ciclo, despliega el valor monetario acumulado total, la cantidad neta de productos registrados con éxito y el número de artículos que requieren un reabastecimiento urgente.

## Estructura del Repositorio
* `tarea2.PY`: Código fuente ejecutable desarrollado en Python 3.
* `Tarea2_KennyaMendez_Prin-Progra 1.pdf`: Documento formal que incluye la portada institucional, tabla de variables, diagrama de flujo (Draw.io), tabla de traza y las capturas de pantalla de los 4 casos de prueba obligatorios.
