import ClaseOperaciones

obj = ClaseOperaciones.OperacionesAritmeticas()

obj.setVal(20)
obj.setVal2(2)

obj.sumar(obj.getVal(),obj.getVal2())
print(obj.getR())

obj.restar(obj.getVal(),obj.getVal2())
print(obj.getR())

obj.multiplicar(obj.getVal(),obj.getVal2())
print(obj.getR())

obj.division(obj.getVal(),obj.getVal2())
print(obj.getR())
