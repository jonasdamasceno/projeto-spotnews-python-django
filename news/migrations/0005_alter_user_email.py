from django.db import migrations, models
import news.validators


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0004_alter_user_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=200,
                validators=[
                    news.validators.validate_empty,
                    news.validators.validate_max_length,
                ],
            ),
        ),
    ]
