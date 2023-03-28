# Generated by Django 4.0.2 on 2023-03-28 10:55

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_customuser_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='interest',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('AI & Robotics', 'AI & Robotics'), ('Business Analysis', 'Business Analysis'), ('Business Intelligence & Data Analytics', 'Business Intelligence & Data Analytics'), ('Business Transformation & Change', 'Business Transformation & Change'), ('Cloud & DevOps', 'Cloud & DevOps'), ('Design & Architecture', 'Design & Architecture'), ('Cyber Security', 'Cyber Security'), ('Digital, UX & UI design', 'Digital, UX & UI design'), ('ERP & CRM', 'ERP & CRM'), ('IT Support & Systems Administration', 'IT Support & Systems Administration'), ('Project Management', 'Project Management'), ('Software Development, Testing & Engineering', 'Software Development, Testing & Engineering'), ('None', 'None')], max_length=293),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='skills',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('AI & Robotics', 'AI & Robotics'), ('Business Analysis', 'Business Analysis'), ('Business Intelligence & Data Analytics', 'Business Intelligence & Data Analytics'), ('Business Transformation & Change', 'Business Transformation & Change'), ('Cloud & DevOps', 'Cloud & DevOps'), ('Design & Architecture', 'Design & Architecture'), ('Cyber Security', 'Cyber Security'), ('Digital, UX & UI design', 'Digital, UX & UI design'), ('ERP & CRM', 'ERP & CRM'), ('IT Support & Systems Administration', 'IT Support & Systems Administration'), ('Project Management', 'Project Management'), ('Software Development, Testing & Engineering', 'Software Development, Testing & Engineering'), ('None', 'None')], max_length=293),
        ),
    ]
