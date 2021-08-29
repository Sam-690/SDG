# Generated by Django 3.2.2 on 2021-08-29 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('padre', models.CharField(max_length=60)),
                ('madre', models.CharField(max_length=60)),
                ('conyuge', models.CharField(max_length=60)),
                ('hijo1', models.CharField(max_length=60)),
                ('hijo2', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ResponsableInterno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('parentesco', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=120)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Interno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellidos', models.CharField(max_length=60)),
                ('fecha_nacimiento', models.DateField()),
                ('lugar_nacimiento', models.CharField(max_length=60)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(max_length=50)),
                ('profecion', models.CharField(max_length=50)),
                ('adicciones', models.CharField(max_length=50)),
                ('tiempo_adiccion', models.IntegerField()),
                ('direccion', models.CharField(max_length=120)),
                ('estado_civil', models.CharField(max_length=60)),
                ('enfermedades', models.CharField(max_length=120)),
                ('tratamiento', models.CharField(max_length=120)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('observaciones', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='internos')),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.familia')),
                ('responsableInterno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.responsableinterno')),
            ],
        ),
    ]