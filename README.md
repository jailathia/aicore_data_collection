# aicore_data_collection

## Milestone 2: Decide which website you are going to colect data from

This project will be about webscraping statistics from the premier league website.

I will be analysing match results for Arsenal as they are doing very well this season. I am hoping that looking at this data will provide some insight.

## Milestone 3: Prototype finding the individual page for each entry

I have made a Scaper class with a wait time used so that the webpage fully loads.

Methods were added to accept the cookies and to scroll down the page. The method used to retrieve the Arsenal games was also added - making sure to consider both home and away fixtures.

The following code first searches for these games:

```python
fixture_list = self.driver.find_element(By.XPATH, '//*[@class="fixtures"]')
        home_games = fixture_list.find_elements(By.XPATH, '//*[@data-home="Arsenal"]')
        away_games = fixture_list.find_elements(By.XPATH, '//*[@data-away="Arsenal"]')
```


