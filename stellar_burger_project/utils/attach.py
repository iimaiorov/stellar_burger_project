import os

import allure
from allure_commons.types import AttachmentType


def add_screenshot(page):
    """Добавляет скриншот страницы в Allure"""
    screenshot = page.screenshot()
    allure.attach(
        screenshot,
        name="screenshot",
        attachment_type=AttachmentType.PNG,
        extension=".png"
    )


def add_html(page):
    """Добавляет исходный HTML страницы в Allure"""
    html = page.content()
    allure.attach(
        html,
        name="page_source",
        attachment_type=AttachmentType.HTML,
        extension=".html"
    )


def add_video(page):
    video_path = page.video.path()
    with open(video_path, "rb") as f:
        allure.attach(f.read(), name="Test Video", attachment_type=AttachmentType.MP4)

