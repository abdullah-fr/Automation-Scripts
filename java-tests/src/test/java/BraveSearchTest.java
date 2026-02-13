// Brave Search Automation Test Suite - Java with TestNG
// This test suite uses TestNG and Selenium WebDriver for browser automation

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;
import java.time.Duration;

public class BraveSearchTest {

    private WebDriver driver;
    private WebDriverWait wait;

    // Setup method - runs before each test
    @BeforeMethod
    public void setUp() {
        // Configure Chrome options to use Brave browser
        ChromeOptions options = new ChromeOptions();
        options.setBinary("/Applications/Brave Browser.app/Contents/MacOS/Brave Browser");

        // Initialize driver and maximize window
        driver = new ChromeDriver(options);
        driver.manage().window().maximize();

        // Initialize explicit wait with 10 second timeout
        wait = new WebDriverWait(driver, Duration.ofSeconds(10));
    }

    // Teardown method - runs after each test
    @AfterMethod
    public void tearDown() {
        if (driver != null) {
            driver.quit();
        }
    }

    // Test 1: Navigate to Brave Search
    @Test(priority = 1)
    public void testNavigateToBraveSearch() {
        driver.get("https://search.brave.com/");
        Assert.assertTrue(driver.getCurrentUrl().contains("brave.com"));
    }

    // Test 2: Check if search box exists
    @Test(priority = 2)
    public void testSearchBoxExists() {
        driver.get("https://search.brave.com/");

        WebElement searchBox = wait.until(
            ExpectedConditions.presenceOfElementLocated(By.id("searchbox"))
        );

        Assert.assertNotNull(searchBox);
    }

    // Test 3: Check if search box accepts input
    @Test(priority = 3)
    public void testSearchBoxIsInteractable() {
        driver.get("https://search.brave.com/");

        WebElement searchBox = wait.until(
            ExpectedConditions.elementToBeClickable(By.id("searchbox"))
        );

        searchBox.sendKeys("upwork login");
        String enteredText = searchBox.getAttribute("value");

        Assert.assertTrue(enteredText.contains("upwork login"));
    }

    // Test 4: Check if search button exists
    @Test(priority = 4)
    public void testSearchButtonExists() {
        driver.get("https://search.brave.com/");

        WebElement searchButton = wait.until(
            ExpectedConditions.presenceOfElementLocated(By.id("submit-llm-button"))
        );

        Assert.assertNotNull(searchButton);
    }

    // Test 5: Complete search flow
    @Test(priority = 5)
    public void testCompleteSearchFlow() {
        driver.get("https://search.brave.com/");
        String homepageUrl = driver.getCurrentUrl();

        // Locate and interact with search box
        WebElement searchBox = wait.until(
            ExpectedConditions.elementToBeClickable(By.id("searchbox"))
        );
        searchBox.sendKeys("upwork login");

        // Locate and click search button
        WebElement searchButton = wait.until(
            ExpectedConditions.elementToBeClickable(By.id("submit-llm-button"))
        );
        searchButton.click();

        // Wait for URL to change
        wait.until(driver -> !driver.getCurrentUrl().equals(homepageUrl));

        Assert.assertNotEquals(driver.getCurrentUrl(), homepageUrl);
    }
}
