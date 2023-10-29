

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialize', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialize',
            name='image',
            field=models.ImageField(default='test', upload_to='images'),
            preserve_default=False,
        ),
    ]
