
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialize', '0007_auto_20210706_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialize',
            name='date',
            field=models.DateField(default='2021-07-06'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='socialize',
            name='supervisor_email',
            field=models.EmailField(default='2021-07-06', max_length=254),
            preserve_default=False,
        ),
    ]
