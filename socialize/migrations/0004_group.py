

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialize', '0003_auto_20210706_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=290)),
            ],
        ),
    ]
