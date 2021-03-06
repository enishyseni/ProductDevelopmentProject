# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-01 14:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetValueLifeCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=800)),
                ('DegradationPercentage', models.FloatField()),
                ('IntervalInDays', models.IntegerField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrganisationName', models.CharField(max_length=200)),
                ('OrganisationDescription', models.CharField(max_length=800)),
                ('TotalAmount', models.FloatField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContractDefinition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=800)),
                ('Name', models.CharField(max_length=200)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.Contract')),
            ],
        ),
        migrations.CreateModel(
            name='ContractDefinitionUploadedDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=800)),
                ('DocumentPath', models.CharField(max_length=800)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ContractDefinition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.ContractDefinition')),
            ],
        ),
        migrations.CreateModel(
            name='ContractExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=800)),
                ('Amount', models.FloatField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ContractExpenseDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DocumentPath', models.CharField(max_length=800)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ContractExpense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.ContractExpense')),
            ],
        ),
        migrations.CreateModel(
            name='ContractStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(choices=[(b'OPPORTUNITY', b'Opportunity'), (b'INITIAL', b'Initial'), (b'PROCESSING', b'Processing'), (b'CONFIRMED', b'Confirmed'), (b'ACTIVE', b'Active'), (b'CANCELED', b'Canceled')], default=b'INITIAL', max_length=20)),
                ('Comment', models.CharField(max_length=800)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.Contract')),
            ],
        ),
        migrations.CreateModel(
            name='EntityAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=800)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('AssetValueLifeCycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.AssetValueLifeCycle')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.Contract')),
            ],
        ),
        migrations.CreateModel(
            name='EntityAssetLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('NaturalStabilityRate', models.IntegerField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EntityAssetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=800)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceMetaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=800)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InsurancePolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IsTemplate', models.BooleanField()),
                ('EffectiveDate', models.DateTimeField()),
                ('ExpireDate', models.DateTimeField()),
                ('Comment', models.CharField(max_length=800)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InsurancePolicyAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=800)),
                ('Name', models.CharField(max_length=200)),
                ('ExtraAmount', models.CharField(max_length=500)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('InsurancePolicy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.InsurancePolicy')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=800)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('InsuranceMetaType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.InsuranceMetaType')),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceTypeComplianceDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=800)),
                ('DocumentPath', models.CharField(max_length=800)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('InsuranceType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.InsuranceType')),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrganisationName', models.CharField(max_length=200)),
                ('OrganisationDescription', models.CharField(max_length=800)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PartnerMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('DateOfBirth', models.DateField()),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.Partner')),
            ],
        ),
        migrations.CreateModel(
            name='PartnerType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=800)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('DeletedBy', models.CharField(max_length=200)),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='partner',
            name='PartnerType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.PartnerType'),
        ),
        migrations.AddField(
            model_name='insurancepolicy',
            name='InsuranceType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.InsuranceType'),
        ),
        migrations.AddField(
            model_name='entityasset',
            name='EntityAssetLocation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.EntityAssetLocation'),
        ),
        migrations.AddField(
            model_name='entityasset',
            name='EntityAssetType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.EntityAssetType'),
        ),
        migrations.AddField(
            model_name='entityasset',
            name='Partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.Partner'),
        ),
        migrations.AddField(
            model_name='contractexpense',
            name='EntityAsset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.EntityAsset'),
        ),
        migrations.AddField(
            model_name='contractdefinitionuploadeddocument',
            name='InsuranceTypeComplianceDocument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.InsuranceTypeComplianceDocument'),
        ),
        migrations.AddField(
            model_name='contractdefinition',
            name='EntityAsset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.EntityAsset'),
        ),
        migrations.AddField(
            model_name='contractdefinition',
            name='InsurancePolicy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.InsurancePolicy'),
        ),
        migrations.AddField(
            model_name='contractdefinition',
            name='PartnerMember',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='et.PartnerMember'),
        ),
    ]
