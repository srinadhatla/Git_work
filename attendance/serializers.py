from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

        def validate(self, attrs):
            check_in = attrs.get("check_in")
            check_out = attrs.get("check_out")

            if check_out and check_out <= check_in:
                raise serializers.ValidationError("Check_out must be after check_in time.")
            return attrs