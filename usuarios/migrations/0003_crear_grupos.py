from django.db import migrations


# Permisos del usuario comun: solo crear posteos y ver el catalogo.
PERMISOS_USUARIO_COMUN = [
    'comunidad.add_posteo',
    'videojuegos.view_juego',
    'videojuegos.view_oferta',
]

# Apps sobre las que "develop" puede hacer todo.
APPS_DEVELOP = ['comunidad', 'videojuegos']


def crear_grupos(apps, schema_editor):
    # Forzamos la creacion de los permisos por si esta migracion corre
    # sobre una base nueva (los permisos se crean recien en post_migrate).
    from django.apps import apps as global_apps
    from django.contrib.auth.management import create_permissions

    for app_config in global_apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=global_apps, verbosity=0)
        app_config.models_module = None

    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Grupo develop: todos los permisos de comunidad y videojuegos.
    develop, _ = Group.objects.get_or_create(name='develop')
    permisos_develop = Permission.objects.filter(
        content_type__app_label__in=APPS_DEVELOP
    )
    develop.permissions.set(permisos_develop)

    # Grupo usuario_comun: solo el subconjunto definido arriba.
    comun, _ = Group.objects.get_or_create(name='usuario_comun')
    permisos_comun = []
    for ruta in PERMISOS_USUARIO_COMUN:
        app_label, codename = ruta.split('.')
        permiso = Permission.objects.filter(
            content_type__app_label=app_label, codename=codename
        ).first()
        if permiso:
            permisos_comun.append(permiso)
    comun.permissions.set(permisos_comun)


def borrar_grupos(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.filter(name__in=['develop', 'usuario_comun']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_usuariopersonalizado_rol_usuario'),
        ('comunidad', '0002_posteo_activo_posteo_usuario'),
        ('videojuegos', '0006_oferta_precio_oferta'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(crear_grupos, borrar_grupos),
    ]
