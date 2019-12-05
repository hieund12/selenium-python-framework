import pytest
import allure

from pages.search_flights_form import SearchFlightsForm
from utils.read_xlsx import XlsxReader


@pytest.mark.usefixtures("setup")
class TestFlightSearch:

    @allure.title("Search flight test: from Swidnik to Oslo - one way")
    @allure.description("This is test of searching one way flight from Swidnik to Oslo")
    def test_search_flight_one_way(self):
        search_flight = SearchFlightsForm(self.driver)
        search_flight.open_page()
        search_flight.open_flights_tab()
        search_flight.set_one_way()
        search_flight.set_cabin_class("First")  # Cabin class: Economy, First, Business
        search_flight.set_loc_from("LUZ")
        search_flight.set_loc_to("OSL")
        # search_flight.set_start_month("Dec")  # month: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
        # search_flight.set_start_day("30")
        search_flight.set_start_date("2019", "Dec", "30")
        search_flight.set_adults_number(2)
        search_flight.set_kids_number(4)
        search_flight.set_infants_number(1)
        search_flight.search_perform()

    @allure.title("Search flight test: from Warsaw to Aruba")
    @allure.description("This is test of searching flight from Warsaw to Aruba and return")
    def test_search_flight_round_trip(self):
        search_flight = SearchFlightsForm(self.driver)
        search_flight.open_page()
        search_flight.open_flights_tab()
        search_flight.set_round_trip()
        search_flight.set_cabin_class("Economy")  # Cabin class: Economy, First, Business
        search_flight.set_loc_from("WAW")
        search_flight.set_loc_to("AUA")
        search_flight.set_start_year("2019", "2020")
        search_flight.set_start_month("Dec")  # month: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec
        search_flight.set_start_day("15")
        search_flight.set_end_year("2020")
        search_flight.set_end_month("Jan")
        search_flight.set_end_day("30")
        search_flight.set_adults_number(1)
        search_flight.set_kids_number(0)
        search_flight.set_infants_number(0)
        search_flight.search_perform()

    @allure.title("Search flight data-driven tests")
    @allure.description("This is data-driven tests of searching flight")
    @pytest.mark.parametrize("data", XlsxReader.get_xlsx_flights_data())
    def test_search_flight_data_driven(self, data):
        search_flight = SearchFlightsForm(self.driver)
        search_flight.open_page()
        search_flight.open_flights_tab()
        search_flight.set_round_trip()
        search_flight.set_cabin_class(data.cabin_class)
        search_flight.set_loc_from(data.location_from)
        search_flight.set_loc_to(data.location_to)
        search_flight.set_start_year(data.current_year, data.start_day)
        search_flight.set_start_month(data.start_month)
        search_flight.set_start_day(data.start_day)
        search_flight.set_end_year(data.current_year, data.end_year)
        search_flight.set_end_month(data.end_month)
        search_flight.set_end_day(data.end_day)
        search_flight.set_adults_number(data.adults_num)
        search_flight.set_kids_number(data.kids_num)
        search_flight.set_infants_number(data.infants_num)
        search_flight.search_perform()
