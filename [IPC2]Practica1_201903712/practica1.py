global lista
lista = []
global lista1
lista1 = []
class Producto():
    def __init__(self, codigo, producto, descripcion, precio_unitario):
        self.codigo = codigo
        self.producto = producto
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario
    i = 0
    lista =[]

class Compra:
    def __init__(self, cliente, id_compra):
        self.cliente = cliente
        self.id_compra = id_compra
        self.lista_productos = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def generar_factura(self):
        costo_total = sum(producto.precio_unitario for producto in self.lista_productos)
        impuesto = costo_total * 0.12
        return costo_total, impuesto


class registro():
    def __init__(self, nombre, correo, nit):
        self.nombre = nombre
        self.correo = correo
        self.nit = nit
 
   

def main():
    productos = []
    clientes = []
    compras = []

    while True:
        print("------------- Menú Principal -------------")
        print("1. Registrar Producto")
        print("2. Registrar Cliente")
        print("3. Realizar Compra")
        print("4. Reporte de Compra")
        print("5. Datos del Estudiante")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = lisatdo()
            productos.append(producto)
            print("Producto registrado exitosamente.")
        elif opcion == "2":
            cliente = Rcliente()
            clientes.append(cliente)
            print("Cliente registrado exitosamente.")
        elif opcion == "3":
            print( "redirigiendo a menu de compras ......")
            realizar_compra(clientes, productos, compras)
        elif opcion == "4":
            reporte(compras)
        elif opcion == "5":
            print(" marvin Obidio Perez Larios")
            print("carnet: 201903712")   
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")



 

def lisatdo():
    c = input("ingrese codigo ")
    np = input("ingrese nombre de producto ")
    d = input("ingrese descripcion ")
    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    return Producto(c, np, d, precio_unitario)


def Rcliente():
    n = input("ingrese nombre: ")
    co = input("ingrese correo: ")
    nit = input("ingrese nit: ") 
    return registro( n, co, nit)
    


def realizar_compra(clientes, productos, compras):
    nit_cliente = input("Ingrese el NIT del cliente: ")
    cliente = next((c for c in clientes if c.nit == nit_cliente), None)
    if cliente is None:
        print("Cliente no encontrado.")
        return

    compra = Compra(cliente, len(compras) + 1)
    while True:
        print("------------- Menú Compra -------------")
        print("1. Agregar Producto")
        print("2. Terminar Compra y Facturar")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
           
            codigo_producto = input("Ingrese el código del producto: ")
            producto = next((p for p in productos if p.codigo == codigo_producto), None)
            if producto is None:
                print("Producto no encontrado.")
            else:
                compra.agregar_producto(producto)
        elif opcion == "2":
            costo_total, impuesto = compra.generar_factura()
            print(f"Costo Total: Q{costo_total}")
            print(f"Impuesto: Q{impuesto}")
            compras.append(compra)
            break
        else:
            print("Opción inválida.")

def compra():
    opcion1 = "0"
    while opcion1 is not "4":
        print("=============== MENU ===============")
        print(" 1. agregar producto")
        print(" 2. terminar compras y facturar")
        print("====================================")
        opcion1 = input("Ingrese una opción: ")
        if opcion1 is "1":
            print("leyendo archivo")
            mostrar()
        elif opcion1 is "2":
            print("compra finalizada ")
            return main()
        elif opcion1 is "3":
          return main()
            

def reporte(compras):
    id_compra = int(input("Ingrese el ID de la compra: "))
    compra = next((c for c in compras if c.id_compra == id_compra), None)
    if compra is None:
        print("Compra no encontrada.")
    else:
        print("------------- REPORTE DE COMPRA ------------")
        print("CLIENTE:")
        print(f"Nombre: {compra.cliente.nombre}")
        print(f"Correo electrónico: {compra.cliente.correo}")
        print(f"NIT: {compra.cliente.nit}")
        print("ARTÍCULOS COMPRADOS:")
        for producto in compra.lista_productos:
            print(f"Código: {producto.codigo}, Nombre: {producto.producto}, Precio: Q{producto.precio_unitario}")
        costo_total, impuesto = compra.generar_factura()
        print(f"Total: Q{costo_total}")
        print(f"Impuestos: Q{impuesto}")

if __name__ == "__main__":
    main()