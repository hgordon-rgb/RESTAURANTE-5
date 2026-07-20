# Restaurante App

## Estudiante
Gordon Ortega Henri Daniel

## Descripción
Sistema de gestión básica de productos, bebidas y clientes de un restaurante desarrollado en Python utilizando Programación Orientada a Objetos.

## Estructura

- Producto
- Bebida
- Cliente
- Restaurante
- main.py

## Principios SOLID

### SRP (Responsabilidad Única)
- Producto representa productos.
- Bebida representa bebidas.
- Cliente representa clientes.
- Restaurante administra colecciones.
- main.py gestiona la interacción.

### OCP (Abierto/Cerrado)
La clase Bebida amplía la funcionalidad de Producto mediante herencia sin modificar la lógica existente.

### LSP (Sustitución de Liskov)
Los objetos Bebida pueden utilizarse como objetos Producto dentro de la misma colección.

## Ejecución

```bash
python main.py