"""comandos de shell django modelos"""


# python manage.py shell
#paera activar la shell

from App1.models import MiModelo

p = MiModelo(id="nueva fila", temperatura="nueva temperatura")# no me sirvio xd

p.save()
MiModelo.objects.all().delete()# eliminar todos
MiModelo.objects.filter(id=1).delete()# eliminar por id
MiModelo.objects.update_or_create(id=2, temperatura=2.1)# crea o actualiza un registro o fila
MiModelo.objects.filter(id="1").update(temperatura=500) # actualiza un valor de la tabla buscandolo por su id

persona, created = Persona.objects.update_or_create(
    nombre='John',
    apellido='Doe',
    defaults={'edad': 30, 'ciudad': 'Nueva York'}
)
# ejemplo de como usar update_or_create si no existen esos datos los crea

MiModelo.objects.all()

# devuelve un queryset, con junto de datos

MiModelo.objects.get(id=1)
#consultar datos buscando por campo, id, nombre, etc


MiModelo.objects.get(id="1")
p= MiModelo.objects.get(id="1")

p.temperatura_set.all()
# me devuelve un queryset vacio   jmm   'MiModelo' object has no attribute 'temperatura_set'
p.task_set.create(title="descargar IDE")

# crea una tarea en la tabla task

MiModelo.objects.filter(name__startswith="")
#filtrado por nombres que empiecen con
p= MiModelo.objects
p.filter(name__startswith="cadena")

MiModelo.objects.filter(id="1").update(temperatura=500)