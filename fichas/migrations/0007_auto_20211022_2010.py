# Generated by Django 3.0.14 on 2021-10-22 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0006_auto_20211022_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ficha',
            old_name='date_created',
            new_name='fechacreacion',
        ),
        migrations.RenameField(
            model_name='ficha',
            old_name='date_edited',
            new_name='ultimaedicion',
        ),
        migrations.RenameField(
            model_name='tarea',
            old_name='title',
            new_name='descripcionTarea',
        ),
        migrations.RenameField(
            model_name='tarea',
            old_name='dependencia',
            new_name='idDependencia',
        ),
        migrations.AddField(
            model_name='ficha',
            name='Observaciones',
            field=models.Field(blank=True, help_text='Resumen de la denuncia', max_length=300),
        ),
        migrations.AddField(
            model_name='ficha',
            name='autoresIgnorados',
            field=models.BooleanField(default=False, help_text='Autores Ignorados'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='detenidos',
            field=models.BooleanField(default=False, help_text='Detenidos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='etapa',
            field=models.CharField(default=1, help_text='Etapa del Caso', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='fechahecho',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='ficha',
            name='flagrancia',
            field=models.BooleanField(default=False, help_text='Flagrancia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='idEstado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fichas.Estado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='idFiscalAdjunto',
            field=models.CharField(default=1, help_text='Fiscal Adjunto', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='idFiscalaCargo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fichas.Fiscale'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='idJuridiccionPolicial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fichas.JuridiccionesPoliciale'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='idViaDenuncia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fichas.OrigenDenuncia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='imputado',
            field=models.BooleanField(default=False, help_text='Tiene imputados'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='pex',
            field=models.CharField(default=1, help_text='PEX', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='resumendelaDenuncia',
            field=models.Field(blank=True, help_text='Resumen de la denuncia', max_length=300),
        ),
        migrations.AddField(
            model_name='ficha',
            name='victimaDesconocida',
            field=models.BooleanField(default=False, help_text='Victima Desconocida'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ficha',
            name='violenciadegenero',
            field=models.BooleanField(default=False, help_text='Violencia de Genero'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='estados',
            field=models.CharField(choices=[('I', 'Iniciado'), ('T', 'Terminado'), ('C', 'Cancelado')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='fechaConclusion',
            field=models.DateField(default=1, help_text='Fecha de Conclusion de la tarea'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='fechaSolicitud',
            field=models.DateField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='idAdministrativo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fichas.Administrativo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='idCaso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fichas.Ficha'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='nota',
            field=models.CharField(default=1, help_text='Nota', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='notaContextual',
            field=models.CharField(default=1, help_text='Nota contextual', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tarea',
            name='resultado',
            field=models.FileField(default=1, help_text='resultado', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ficha',
            name='fechacierre',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Descripcion del video.', max_length=50)),
                ('archivoVideo', models.FileField(help_text='Video.', upload_to='')),
                ('idCaso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichas.Ficha')),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Descripcion de la Imagen.', max_length=50)),
                ('archivoFoto', models.FileField(help_text='Foto.', upload_to='')),
                ('idCaso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichas.Ficha')),
            ],
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Descripcion del Archivo.', max_length=50)),
                ('archivoVideo', models.FileField(help_text='Video.', upload_to='')),
                ('idCaso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fichas.Ficha')),
            ],
        ),
    ]