import pytest
from playwright.sync_api import sync_playwright
from stellar_burger_project.utils import attach
from project import Config


@pytest.fixture(autouse=True)
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,slow_mo=50)
        context = browser.new_context(
            record_video_dir="videos/",
            base_url= Config().base_url,
            viewport= {
                "width": Config().window_width,
                "height": Config().window_height
        }
        )
        page = context.new_page()
        yield page
        attach.add_screenshot(page)
        attach.add_html(page)
        context.close()
        attach.add_video(page)
        browser.close()
