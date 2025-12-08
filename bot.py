import time
import os

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class MargonemBot:
    def __init__(self, npc_id, server, logger):
        self.logger = logger
        self.options = Options()
        self._configure_options()
        self.driver = None
        self._start_browser()
        self.npc_to_track = npc_id
        self.server = server
        self.logger.log_event('Bot started.')

    def _configure_options(self):
        base_path = os.getcwd()
        profile_path = os.path.join(base_path, "chrome_bot_profile")
        self.options.add_argument(f"--user-data-dir={profile_path}")

        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument("--disable-blink-features=AutomationControlled")

        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--start-maximized")
        self.logger.log_event('Option configured.')

    def _start_browser(self):
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })

    def go_to_main_page(self):
        self.driver.get('https://www.margonem.pl')
        self.logger.log_event('Main page displayed.')

    def log_in(self):
        while self.server not in self.driver.current_url:
            time.sleep(1)
        self.logger.log_event('Game started.')
        time.sleep(3)

    def open_game(self):
        self.driver.get(f"https://{self.server}.margonem.pl")
        self.logger.log_event('Game opened.')
        time.sleep(3)

    def hunt_npc(self):
        try:
            npc = self.driver.find_element(by=By.ID, value=self.npc_to_track)
            npc.click()
            self.logger.log_event('NPC Attacked.')
            time.sleep(1.5)
        except NoSuchElementException:
                time.sleep(1)

    def close_loot_window(self):
        try:
            loot_button = self.driver.find_element(By.ID, 'loots_button')
            if loot_button.is_displayed():
                loot_button.click()
                self.logger.log_event('Loot window closed.')
        except NoSuchElementException:
            pass


    def close_battle(self):
        try:
            close_button = self.driver.find_element(By.ID, 'battleclose')
            if close_button.is_displayed():
                close_button.click()
                self.logger.log_event('Battle window closed.')
        except NoSuchElementException:
            pass


