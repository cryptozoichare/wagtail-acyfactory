# Generated by Django 5.0.4 on 2024-05-21 04:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0013_commentwithtitle"),
        ("contenttypes", "0002_remove_content_type_name"),
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CommentWithTitle",
            new_name="BlogComment",
        ),
    ]