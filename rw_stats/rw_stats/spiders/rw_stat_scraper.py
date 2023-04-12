import scrapy


class RedWingStatScraper(scrapy.Spider):
    name = "rw_stat_scraper"

    def start_requests(self):
        base_url = 'https://www.hockey-reference.com/teams/DET/'
        end_year_of_season = 2023
        nhl_first_season_end_year = 1917
        while end_year_of_season >= nhl_first_season_end_year:
            url = base_url + str(end_year_of_season) + ".html#all_team_stats"
            yield scrapy.Request(url=url, callback=self.parse)
            print('CRAWLED ' + url)
            end_year_of_season -= 1


    def parse(self, response):
        print('here')
