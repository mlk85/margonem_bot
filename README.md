# Margonem Automation PoC (Python + Selenium)

> **⚠️ LEGAL DISCLAIMER**
>
> This project is a **Proof of Concept** created **strictly for educational purposes**. Using bots in Margonem violates the Terms of Service and may result in a **permanent account ban**. The author is not responsible for any consequences.

## 📌 About the Project

This is a simple automation tool for the MMORPG Margonem, built using **Selenium WebDriver**. The goal is to learn how to interact with dynamic web elements and manage session control in a real-time gaming environment.

---

## ⚙️ Key Features (Based on Current Code)

* **Anti-Detection:** Configuration to **mask the `navigator.webdriver` flag** and automated identity (via Chrome options and JavaScript injection).
* **Session Persistence:** Saves the login profile locally, maintaining cookies and settings between runs.
* **Login Handover:** Waits for the game world URL to load, allowing the user to **log in manually** before the bot takes control.
* **Target Hunting:** Locates a monster by its specific **ID** and initiates the approach.
* **Auto-Combat:** Detects the battle interface and enables the **automatic fight sequence**.

## 🚀 Installation & Usage

1.  **Requirements:** Python 3.8+ and Google Chrome.
2.  **Install Libraries:** Install all necessary dependencies listed in `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configuration:** Set `NPC_ID` and `server` variables in the main script file.

4.  **How to Run:**
    * Execute `python main.py`.
    * Log in manually in the opened Chrome window.
    * The bot automatically takes over upon entering the game world.

---

## ✨ Planned Features

* **Return to Camping Spot:** Implementing logic to return to predefined coordinates (`X, Y`) after combat or when the target is lost.

## 🔗 Recommended Addons

For better stability and to enhance the game's interface for automation, the following community add-ons are recommended:

* **Addon 1:** "Auto zamykanie walki" - Samedamci

---
*Project created for hobby and research purposes.*