# Generated by Django 3.2.11 on 2022-01-23 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catparking',
            fields=[
                ('catid', models.AutoField(db_column='catId', primary_key=True, serialize=False)),
                ('dmslong', models.DecimalField(db_column='dmsLong', decimal_places=16, max_digits=18)),
                ('dmslat', models.DecimalField(db_column='dmsLat', decimal_places=16, max_digits=18)),
                ('type', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('categoryparking', models.CharField(db_column='categoryParking', max_length=10)),
                ('allowedvehicletype', models.CharField(db_column='allowedVehicleType', max_length=20)),
                ('totalspotnumber', models.IntegerField(db_column='totalSpotNumber')),
                ('timemodified', models.DateTimeField(auto_now=True, db_column='timeModified')),
                ('address', models.CharField(max_length=100)),
                ('requiredpermit', models.CharField(db_column='requiredPermit', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Getdata',
            fields=[
                ('dataid', models.AutoField(db_column='dataId', primary_key=True, serialize=False)),
                ('datatext', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('orgid', models.AutoField(db_column='orgId', primary_key=True, serialize=False)),
                ('orgname', models.CharField(db_column='orgName', max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('building', models.BooleanField()),
                ('buildlat', models.DecimalField(blank=True, db_column='buildLat', decimal_places=16, max_digits=18, null=True)),
                ('buildlong', models.DecimalField(blank=True, db_column='buildLong', decimal_places=16, max_digits=18, null=True)),
                ('ramp', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicUser',
            fields=[
                ('userid', models.AutoField(db_column='userId', primary_key=True, serialize=False)),
                ('useremail', models.CharField(db_column='userEmail', max_length=50)),
                ('userpassword', models.CharField(db_column='userPassword', max_length=50)),
                ('usercardcode', models.CharField(db_column='userCardCode', max_length=50)),
                ('usercardimage', models.BinaryField(db_column='userCardImage')),
            ],
        ),
        migrations.CreateModel(
            name='Parkingspot',
            fields=[
                ('spotid', models.AutoField(db_column='spotId', primary_key=True, serialize=False)),
                ('spotlong', models.DecimalField(db_column='spotLong', decimal_places=16, max_digits=18)),
                ('spotlat', models.DecimalField(db_column='spotLat', decimal_places=16, max_digits=18)),
                ('type', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('categoryspot', models.CharField(db_column='categorySpot', max_length=20)),
                ('catid', models.ForeignKey(db_column='catId', on_delete=django.db.models.deletion.DO_NOTHING, to='spots.catparking')),
            ],
        ),
        migrations.AddField(
            model_name='catparking',
            name='orgid',
            field=models.ForeignKey(db_column='orgId', on_delete=django.db.models.deletion.DO_NOTHING, to='spots.organization'),
        ),
    ]