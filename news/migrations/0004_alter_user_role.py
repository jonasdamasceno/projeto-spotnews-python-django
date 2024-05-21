from django.db import migrations, models
import news.validators


class Migration(migrations.Migration):
    dependencies = [
        (
          "news",
          "0003_alter_user_email_alter_user_name_alter_user_password_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                max_length=200,
                validators=[
                    news.validators.validate_empty,
                    news.validators.validate_max_length,
                ],
            ),
        ),
    ]
