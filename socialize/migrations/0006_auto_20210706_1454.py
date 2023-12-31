

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialize', '0005_socialize_group_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.IntegerField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='socialize',
            name='email_address',
            field=models.ManyToManyField(blank=True, null=True, to='socialize.Contributor'),
        ),
    ]
