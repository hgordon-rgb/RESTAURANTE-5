class Restaurante:
    def __init__(self):
        self.productos = []
        self.clientes = []

    def registrar_producto(self, producto):
        for p in self.productos:
            if p.codigo == producto.codigo:
                print("Error: el código ya existe.")
                return

        self.productos.append(producto)
        print("Producto registrado correctamente.")

    def registrar_cliente(self, cliente):
        for c in self.clientes:
            if c.identificacion == cliente.identificacion:
                print("Error: la identificación ya existe.")
                return

        self.clientes.append(cliente)
        print("Cliente registrado correctamente.")

    def listar_productos(self):
        if not self.productos:
            print("No existen productos registrados.")
            return

        print("\n=== LISTA DE PRODUCTOS ===")
        for producto in self.productos:
            print(producto.mostrar_informacion())

    def listar_clientes(self):
        if not self.clientes:
            print("No existen clientes registrados.")
            return

        print("\n=== LISTA DE CLIENTES ===")
        for cliente in self.clientes:
            print(cliente.mostrar_informacion())