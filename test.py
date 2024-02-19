from main import StudentsInMLOps
import pytest

def test_enroll_students():
    mlops = StudentsInMLOps()
    mlops.enrollStudents(5)
    assert mlops.getTotalStrength() == 5

def test_drop_students():
    mlops = StudentsInMLOps()
    mlops.enrollStudents(10)
    mlops.dropStudents(3)
    assert mlops.getTotalStrength() == 7
