

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socialize', '0006_auto_20210706_1454'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialize',
            old_name='email_address',
            new_name='contributor',
        ),
    ]
