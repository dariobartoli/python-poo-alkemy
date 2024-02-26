from enum import Enum
from datetime import datetime


class TipoContrato(Enum):
    COMISION = 'comision'
    FIJO = 'fijo'

class Empleado:
    def __init__(self, dni, nombre, apellido, anio_ingreso, tipo_contrato):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.anio_ingreso = anio_ingreso
        self.tipo_contrato = tipo_contrato
    def calcularSalario(self):
        pass
    def mostrarSalario(self):
        pass

class EmpleadoComision(Empleado):
    def __init__(self, dni,nombre,apellido, anio_ingreso, tipo_contrato, salario_minimo, cant_clientes, monto_por_cliente):
        super().__init__(dni,nombre,apellido, anio_ingreso, tipo_contrato)
        self.salario_minimo = salario_minimo
        self.cant_clientes = cant_clientes
        self.monto_por_cliente = monto_por_cliente
    def calcularSalario(self):
        salarioComision = self.cant_clientes * self.monto_por_cliente
        if(salarioComision < self.salario_minimo):
            return self.salario_minimo
        else: return salarioComision
    def mostrarSalario(self):
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Salario: {self.calcularSalario()}')
        print('------------------------------------------------')


class EmpleadoFijo(Empleado):
    def __init__(self, dni,nombre,apellido, anio_ingreso, tipo_contrato, salario_fijo):
        super().__init__(dni,nombre,apellido, anio_ingreso, tipo_contrato)
        self.salario_fijo = salario_fijo
    def calcularSalario(self):
        fecha_hoy = datetime.now().year
        antiguedad = fecha_hoy - self.anio_ingreso
        salario = self.salario_fijo
        if(antiguedad > 5):
            return salario * 1.1
        elif(antiguedad > 2):
            return salario * 1.05
        else: return salario
    def mostrarSalario(self):
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Salario: {self.calcularSalario()}')
        print('------------------------------------------------')


empleado1 = EmpleadoFijo("25548125", "Juan", "Lopez", 2015, TipoContrato.FIJO, 320000)
empleado2 = EmpleadoFijo("35458512", "Martin", "Martelo", 2023, TipoContrato.FIJO, 310000)
empleado3 = EmpleadoFijo("48521365", "Pablo", "Picasso", 2022, TipoContrato.FIJO, 350000)
empleado4 = EmpleadoFijo("51325845", "Juana", "Herrero", 2021, TipoContrato.FIJO, 25000)
empleado5 = EmpleadoFijo("45125421", "Florencia", "Caro", 2010, TipoContrato.FIJO, 200000)
empleado6 = EmpleadoComision("39542541", "Maria", "Garcia", 2019, TipoContrato.COMISION, 250000, 30, 10000)
empleado7 = EmpleadoComision("35412151", "Tomas", "Simpson", 2019, TipoContrato.COMISION, 250000, 24, 10000)
empleado8 = EmpleadoComision("42454358", "Facundo", "Mansilla", 2019, TipoContrato.COMISION, 250000, 22, 10000)
empleado9 = EmpleadoComision("45879256", "Nahuel", "Garcia", 2019, TipoContrato.COMISION, 250000, 35, 10000)
empleado10 = EmpleadoComision("45452148", "Pablo", "Aguero", 2019, TipoContrato.COMISION, 250000, 15, 10000)
empleado1.mostrarSalario()
empleado2.mostrarSalario()
empleado3.mostrarSalario()
empleado4.mostrarSalario()
empleado5.mostrarSalario()
empleado6.mostrarSalario()
empleado7.mostrarSalario()
empleado8.mostrarSalario()
empleado9.mostrarSalario()
empleado10.mostrarSalario()


empleados_comision = []
empleados_comision.append(empleado6)
empleados_comision.append(empleado7)
empleados_comision.append(empleado8)
empleados_comision.append(empleado9)
empleados_comision.append(empleado10)


def empleadoConMasClientes(lista):
    mayor_cliente = 0
    nombre_empleado = ''
    apellido_empleado = ''
    for empleado in lista:
        if(empleado.cant_clientes > mayor_cliente):
            mayor_cliente = empleado.cant_clientes
            nombre_empleado = empleado.nombre
            apellido_empleado = empleado.apellido
    print(mayor_cliente)
    print(nombre_empleado)
    print(apellido_empleado)

empleadoConMasClientes(empleados_comision)



