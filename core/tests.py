from django.test import TestCase
import unittest

from core.models import Vacancy
from worker.models import Worker


class HomepageTestCase(TestCase):
    def test_open_homepage_should_success(self):
        respons = self.client.get("/")
        assert respons.status_code == 200
        #assert "Поиск работы и работников" in respons

    def test_post_request_homepage_should_405(self):
        respons = self.client.post("/")
        assert respons.status_code == 405


class VacancyTestCase(TestCase):
    def test_create_vacancy_should_success(self):
        my_data = {
            "title": "Test 1",
            "salary": "100",
            "description": "test description 1",
            "email": "test@gmail.com",
            "contacts": "@codifytest",
        }

        response = self.client.post("/add-vacancy/", data=my_data)
        self.assertEquals(response.status_code, 302)

        new_vacancy = Vacancy.objects.first()
        self.assertEqual(new_vacancy.title, my_data["title"])
        self.assertEqual(new_vacancy.salary, int(my_data["salary"]))
        self.assertEqual(new_vacancy.description, my_data["description"])
        self.assertEqual(new_vacancy.email, my_data["email"])
        self.assertEqual(new_vacancy.contacts, my_data["contacts"])

        vacancy_title = my_data["title"]
        response_homepage = self.client.get("/")
        self.assertContains(response_homepage, vacancy_title)


class WorkerTest(unittest.TestCase):
    def test_worker_init(self):
        worker = Worker()
        self.assertEqual(worker.name_w)
        self.assertEqual(worker.specialization)
        self.assertEqual(worker.w_salary)
        self.assertEqual(worker.is_searching)
    def test_worker_name_w(self):
        worker = Worker()
        worker.name_w()
        self.assertEqual(worker.name_w)

    def test_worker_specialization(self):
        worker = Worker()
        worker.specialization()
        self.assertEqual(worker.specialization)

    def test_worker_w_salary(self):
        worker = Worker()
        worker.w_salary()
        self.assertEqual(worker.w_salary)

    def test_worker_is_searching(self):
        worker = Worker()
        worker.is_searching()
        self.assertEqual(worker.is_searching)


if __name__ == '__main__':
    unittest.main()



class ResumeTestCase(TestCase):
    def test_create_resume_should_success(self):
        my_data = {
            "text ": "Test 1",
            "summary": "100",
            "skills": "test skills 1",
            "worker": "test@gmail.com",
            "title": "title",
            "created_at": "created_at",
            "profile_photo": "profile_photo"
        }

        response = self.client.post("/resume-info/<int:id/", data=my_data)
        self.assertEquals(response.status_code, 302)

