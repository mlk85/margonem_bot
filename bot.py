import random
import time
import os

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
            time.sleep(0.1)
            npc.click()
            self.logger.log_event('NPC Found.')
            time.sleep(1.9)
            self.driver.find_element(by=By.ID, value=self.npc_to_track).click()
            time.sleep(0.1)
            self.driver.find_element(by=By.ID, value=self.npc_to_track).click()
            self.logger.log_event('NPC Attacked.')
            self._auto_battle()
            time.sleep(15)
        except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException)as e:
            if isinstance(e, StaleElementReferenceException):
                self.logger.log_event(f'Battle error: {e}')
            elif isinstance(e, ElementClickInterceptedException):
                self._auto_battle()
            time.sleep(0.5)

    def _auto_battle(self):
        try:
            time.sleep(random.uniform(4.3,5.3))
            auto_battle_button = self.driver.find_element(By.ID, "autobattleButton")
            if auto_battle_button.is_displayed():
                self.logger.log_event('Fight Started.')
                auto_battle_button.click()
                self.logger.log_event('Auto-fight enabled.')
                time.sleep(3)
        except NoSuchElementException:
            pass


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

    def solve_captcha(self):
        try:
            pre_captcha = self.driver.find_elements(By.ID, 'pre-captcha')
            if pre_captcha:
                element = pre_captcha[0]
                classes = element.get_attribute("class")
                if "show" in classes and element.is_displayed():
                    timer_element = self.driver.find_element(By.CLASS_NAME, "captcha-pre-info__time")
                    time_left = int(timer_element.text.strip())
                    if time_left < 165:
                        self.logger.log_event('Captcha displayed.')
                        self.driver.find_element(By.CLASS_NAME, 'captcha-pre-info__button').click()
                        try:
                            WebDriverWait(self.driver, 5).until(
                                ec.visibility_of_element_located((By.CLASS_NAME, "captcha__buttons"))
                            )
                            time.sleep(0.5)
                            buttons = self.driver.find_elements(By.CSS_SELECTOR, ".captcha__buttons .btn")
                            print(f"found {len(buttons)} buttons")
                            for btn in buttons:
                                span_text = btn.find_element(By.CSS_SELECTOR, ".label span").text
                                if "*" in span_text:
                                    btn.click()
                                    time.sleep(random.uniform(0.3, 0.5))
                            self.driver.find_element(By.NAME, "Potwierdzam").click()
                            self.logger.log_event("Captcha solved.")
                        except Exception as e:
                            self.logger.log_event(f'captcha error: {e}')
                            pass
        except NoSuchElementException:
            pass


