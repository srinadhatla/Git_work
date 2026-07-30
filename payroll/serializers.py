from rest_framework import serializers
from .models import Payroll


class PayrollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payroll
        fields = "__all__"

    def validate(self, attrs):
        basic_salary = attrs.get("basic_salary")
        bonus = attrs.get("bonus")
        deduction = attrs.get("deduction")

        if basic_salary <= 0:
            raise serializers.ValidationError("Basic salary must be greater than zero")
        if bonus < 0:
            raise serializers.ValidationError("Bonus cannot be negative")
        if deduction < 0:
            raise serializers.ValidationError("Deduction cannot be negative")

        return attrs