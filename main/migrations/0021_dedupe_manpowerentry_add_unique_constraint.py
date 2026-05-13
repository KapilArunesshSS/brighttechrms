from django.db import migrations, models


def dedupe_manpower_entries(apps, schema_editor):
    ManpowerEntry = apps.get_model('main', 'ManpowerEntry')

    seen_pairs = set()
    duplicate_ids = []

    for entry in ManpowerEntry.objects.order_by('id').iterator():
        pair = (entry.date, entry.structure_id)
        if entry.structure_id is None:
            continue
        if pair in seen_pairs:
            duplicate_ids.append(entry.id)
        else:
            seen_pairs.add(pair)

    if duplicate_ids:
        ManpowerEntry.objects.filter(id__in=duplicate_ids).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_employee_status'),
    ]

    operations = [
        migrations.RunPython(dedupe_manpower_entries, migrations.RunPython.noop),
        migrations.AddConstraint(
            model_name='manpowerentry',
            constraint=models.UniqueConstraint(
                fields=('date', 'structure'),
                name='unique_manpowerentry_date_structure',
            ),
        ),
    ]
