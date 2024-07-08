from django.db import migrations


def create_initial_groups(apps, schema_editor):
    group = apps.get_model('auth', 'Group')

    groups = ['Admin', 'Manager', 'Security']
    for group_name in groups:
        group.objects.get_or_create(name=group_name)
        print(f"Group '{group_name}' created or already exists")


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_groups),
    ]
