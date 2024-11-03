from http import HTTPStatus

from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import HomePageView, AboutPageView


class HomepageTests(SimpleTestCase):

    def setUp(self):
        url = reverse("pages:home")
        self.res = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.res.status_code, HTTPStatus.OK)

    def test_homepage_url_name(self):
        self.assertEqual(self.res.status_code, HTTPStatus.OK)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.res, "pages/home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.res, "Homepage")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.res, "Hi there! I should't be on the page.")

    def test_homepage_url_resolves_homepage_view(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("pages:about")
        self.res = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.res.status_code, HTTPStatus.OK)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.res, "pages/about.html")

    def test_about_page_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )

