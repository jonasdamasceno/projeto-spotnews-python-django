from django.db import migrations, models
import news.validators


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(
                max_length=200,
                validators=[
                    news.validators.validate_empty,
                    news.validators.validate_max_length,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(
                max_length=200,
                validators=[
                    news.validators.validate_empty,
                    news.validators.validate_max_length,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(
                max_length=200,
                validators=[
                    news.validators.validate_empty,
                    news.validators.validate_max_length,
                ],
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.EmailField(
                max_length=200,
                validators=[
                    news.validators.validate_empty,
                    news.validators.validate_max_length,
                ],
            ),
        ),
    ]
