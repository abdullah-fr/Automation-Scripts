# Import pytest for test framework and Playwright for browser automation
import pytest
from playwright.sync_api import Page, expect
import time


# Helper function to highlight elements with dynamic colors
def highlight_element(page: Page, selector: str, color: str = "red"):
    """Highlight an element with a colored border for visual feedback"""
    page.evaluate(f"""
        (selector) => {{
            const element = document.querySelector(selector);
            if (element) {{
                element.style.border = '3px solid {color}';
                element.style.boxShadow = '0 0 10px {color}';
            }}
        }}
    """, selector)
    time.sleep(0.5)  # Pause to show the highlight


@pytest.fixture
def page(browser):
    """Setup and teardown page for each test"""
    # Create a new browser page for each test
    page = browser.new_page()
    yield page
    # Close the page after test completes
    page.close()


def test_navigate_to_brave_search(page: Page):
    """Test 1: Navigate to Brave Search"""
    # Open Brave Search homepage
    page.goto("https://search.brave.com/")
    # Verify URL contains "brave.com"
    assert "brave.com" in page.url


def test_search_box_exists(page: Page):
    """Test 2: Check if search box exists"""
    # Navigate to Brave Search
    page.goto("https://search.brave.com/")
    # Locate the search input box by ID
    search_box = page.locator("#searchbox")
    # Verify search box is visible on the page (wait up to 10 seconds)
    expect(search_box).to_be_visible(timeout=10000)
    # Highlight the search box in blue
    highlight_element(page, "#searchbox", "blue")


def test_search_box_is_interactable(page: Page):
    """Test 3: Check if search box accepts input"""
    # Navigate to Brave Search
    page.goto("https://search.brave.com/")
    # Locate the search input box
    search_box = page.locator("#searchbox")
    # Highlight the search box in green before typing
    highlight_element(page, "#searchbox", "green")
    # Type text into the search box
    search_box.fill("mac repair shop")
    time.sleep(1)  # Pause to see the typed text
    # Verify the entered text matches what we typed
    expect(search_box).to_have_value("mac repair shop")


def test_search_button_exists(page: Page):
    """Test 4: Check if search button exists"""
    # Navigate to Brave Search
    page.goto("https://search.brave.com/")
    # Locate the search submit button by ID
    search_button = page.locator("#submit-llm-button")
    # Verify button is visible on the page (wait up to 10 seconds)
    expect(search_button).to_be_visible(timeout=10000)
    # Highlight the search button in orange
    highlight_element(page, "#submit-llm-button", "orange")


def test_complete_search_flow(page: Page):
    """Test 5: Complete search flow from start to finish"""
    # Navigate to Brave Search homepage
    page.goto("https://search.brave.com/")

    # Locate and fill the search box with query
    search_box = page.locator("#searchbox")
    # Highlight search box in purple
    highlight_element(page, "#searchbox", "purple")
    search_box.fill("mac repair shop")
    time.sleep(1)  # Pause to see the typed text

    # Press Enter to search instead of clicking button
    search_box.press("Enter")

    # Wait for URL to change (indicating search results loaded)
    page.wait_for_url(lambda url: url != "https://search.brave.com/", timeout=10000)
    time.sleep(2)  # Pause to see the search results

    # Verify we navigated away from the homepage
    assert page.url != "https://search.brave.com/"

    # Locate the first search result link (excluding ads)
    # Try different selectors for the first organic result
    first_result = page.locator('div[data-type="web"] a[href]:not([data-pos="ad"])').first

    # Highlight the first result in cyan before clicking
    page.evaluate("""
        () => {
            const firstLink = document.querySelector('div[data-type="web"] a[href]:not([data-pos="ad"])');
            if (firstLink) {
                firstLink.style.border = '3px solid cyan';
                firstLink.style.boxShadow = '0 0 10px cyan';
                firstLink.style.backgroundColor = 'rgba(0, 255, 255, 0.1)';
            }
        }
    """)
    time.sleep(2)  # Pause to see the highlighted result

    # Click the first search result
    first_result.click()

    # Wait for the new page to load
    time.sleep(3)  # Pause to see the opened website

    # Verify we navigated to a new page
    print(f"Opened website: {page.url}")


# Run tests when file is executed directly
if __name__ == "__main__":
    pytest.main([__file__, "-v"])

# Run tests with: python3 -m pytest test_search_playwright.py -v
