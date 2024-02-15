#3. Crea una función llamada verificar_calificacion que reciba tres
#parámetros: nota1, nota2 y nota3
#↪ Dentro de la función calcular el promedio de notas
#↪ Si el promedio es mayor o igual a 6, entonces la función debe
#retornar un mensaje “Aprobado”, en caso contrario
#“Reprobado”
#● Guardar en un archivo llamado ejercicio3.py

def verificar_calificacion(nota1, nota2, nota3):
    promedio = (nota1+nota2+nota3)/3
    if(promedio >= 6):
        print(f'Tu promedio es de {promedio}, estas aprobado')
    else:
        print(f'Tu promedio es de {promedio}, estas reprobado')

verificar_calificacion(10,1,4)
verificar_calificacion(8,4,7)