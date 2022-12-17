import unittest
from shiftlabapi import *


class TestShiftLabAPI(unittest.TestCase):
    def test_sign_in(self):
        self.assertEqual(sign_in().status_code, 200)
        self.assertEqual('jwt' and 'refreshToken' in sign_in().json(), True)
        self.assertEqual(type(sign_in().json().get("jwt" and "refreshToken")), str)

    def test_token_refresh(self):
        self.assertEqual(token_refresh().status_code, 200)
        self.assertEqual('jwt' and 'refreshToken' in token_refresh().json(), True)
        self.assertEqual(type(token_refresh().json().get("jwt" and "refreshToken")), str)

    def test_vacation_request_decision(self):
        self.assertEqual(vacation_request_decision().status_code, 200)

    def test_vacation_requests(self):
        self.assertEqual(vacation_requests().status_code, 200)
        self.assertEqual(type(vacation_requests().json()), list)

    def test_businesstrip_country_cities(self):
        self.assertEqual(businesstrip_country_cities().status_code, 200)

    def test_businesstrip_archive(self):
        self.assertEqual(businesstrip_archive().status_code, 200)
        self.assertEqual(type(businesstrip_archive().json()), list)

    def test_businesstrip_countries(self):
        self.assertEqual(businesstrip_countries().status_code, 200)
        self.assertEqual(type(businesstrip_countries().json()), list)

    def test_businesstrip_request(self):
        self.assertEqual(businesstrip_request().status_code, 200)

    def test_certificate_get_email(self):
        self.assertEqual(certificate_get_email().status_code, 200)

    def test_certificate_load_url(self):
        self.assertEqual(certificate_load_url().status_code, 200)

    def test_certificate_send(self):
        self.assertEqual(certificate_send().status_code, 200)

    def test_vacation_alternates(self):
        self.assertEqual(vacation_alternates().status_code, 200)
        self.assertEqual(type(vacation_alternates().json()), list)

    def test_inventory(self):
        self.assertEqual(inventory().status_code, 200)
        self.assertEqual('inventories' in inventory().json(), True)
        self.assertEqual(type(inventory().json().get("inventories")), list)

    def test_inventory_details(self):
        self.assertEqual(inventory_details().status_code, 200)

    def test_booked_booked_meeting_rooms(self):
        self.assertEqual(booked_booked_meeting_rooms().status_code, 200)

    def test_profile_get_name(self):
        self.assertEqual(profile_get_name().status_code, 200)
        self.assertEqual('name' in profile_get_name().json(), True)
        self.assertEqual(type(profile_get_name().json().get("name")), str)

    def test_sick_leave_request(self):
        self.assertEqual(sick_leave_request().status_code, 200)

    def test_tasks_feed(self):
        self.assertEqual(tasks_feed().status_code, 200)
        self.assertEqual('items' in tasks_feed().json(), True)
        self.assertEqual(type(tasks_feed().json().get("items")), list)

    def test_vacation_days_info(self):
        self.assertEqual(vacation_days_info().status_code, 200)
        self.assertEqual(
            'today' and 'onEndOfYear' and 'lastRecalculationDate' in vacation_days_info().json(), True)
        self.assertEqual(
            type(vacation_days_info().json().get("today" and "onEndOfYear" and "lastRecalculationDate")),
            int)

    def test_vacation_periods_year_month(self):
        self.assertEqual(vacation_periods_year_month().status_code, 200)

    def test_vacation_vacations_list(self):
        self.assertEqual(vacation_vacations_list().status_code, 200)

    def test_categories(self):
        self.assertEqual(categories().status_code, 200)
        self.assertEqual(type(categories().json()), list)

    def test_warehouse(self):
        self.assertEqual(warehouse().status_code, 200)
        self.assertEqual(type(warehouse().json()), list)

    def test_warehouse_requests_from_warehouse(self):
        self.assertEqual(warehouse_requests_from_warehouse().status_code, 200)
        self.assertEqual(type(warehouse_requests_from_warehouse().json()), list)


if __name__ == '__main__':
    unittest.main()
