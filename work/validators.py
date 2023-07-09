from rest_framework import serializers

def validate_salary(value):
    try:
        value = float(value)
        return value
    except:
        raise serializers.ValidationError(f"{value} except only numbers")
    