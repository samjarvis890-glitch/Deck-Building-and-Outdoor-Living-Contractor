import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 900})
        
        url = 'file:///' + os.path.abspath('services.html').replace('\\', '/')
        await page.goto(url)
        await page.wait_for_timeout(1000)
        
        # Scroll to final CTA
        cta = page.locator('#service-enquiry-cta')
        if await cta.count() > 0:
            await cta.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await cta.screenshot(path='scratch/check_services_cta_light.png')
            
            # Now dark mode
            await page.evaluate("document.documentElement.setAttribute('data-theme', 'dark')")
            await page.wait_for_timeout(500)
            await cta.screenshot(path='scratch/check_services_cta_dark.png')
            print("Screenshots taken")
        else:
            print("CTA not found")
        await browser.close()

asyncio.run(main())
