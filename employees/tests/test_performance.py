import time
import tracemalloc

from django.test import TestCase
from django.test.utils import CaptureQueriesContext
from django.db import connection
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class PerformanceTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="admin",
            password="admin123",
            is_staff=True
        )

        self.client.force_authenticate(user=self.user)

    def test_employee_list_performance(self):
        start = time.perf_counter()
        response = self.client.get(
            "/api/v1/employees/"
        )

        end = time.perf_counter()
        execution_time = end - start
        print(f"\nEmployee API Time: {execution_time:.4f} seconds")
        self.assertEqual(response.status_code, 200)

    def test_dashboard_performance(self):
        start = time.perf_counter()
        response = self.client.get("/dashboard/")

        end = time.perf_counter()
        print(f"\nDashboard Time: {end-start:.4f}")
        self.assertEqual(response.status_code,200)

    def test_search_performance(self):
        start = time.perf_counter()
        response = self.client.get("/api/v1/employees/search/?search=john")
        end = time.perf_counter()
        print(f"\nSearch Time: {end-start:.4f}")

        self.assertEqual(response.status_code,200)

    def test_employee_query_count(self):
        with CaptureQueriesContext(connection) as queries:
            self.client.get("/api/v1/employees/")

        print(f"\nQueries Executed: {len(queries)}")

        self.assertLessEqual(len(queries),10)

    def test_memory_usage(self):
        tracemalloc.start()
        self.client.get("/api/v1/employees/")
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"\nCurrent Memory: {current / 1024:.2f} KB")

        print(f"Peak Memory: {peak / 1024:.2f} KB")