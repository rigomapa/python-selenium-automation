
Feature: tests for Target Returns and Exchanges page


  Scenario Outline: Verify Browse help drop down works and opens the correct pages
    Given user opens Returns and Exchanges page
    Then verify Returns & Exchanges page opens
    When user selects topic <topic_option> in Browse Help dropdown
    Then verify <topic_option> page opens
    Examples:
    |topic_option         |
    |Orders & Purchases   |
    |Promotions & Coupons |
    |Target Circle™       |
    |Partner Programs     |
    |Registries & Lists   |
    |Delivery & Pickup    |
    |Target Account       |
    |Payment Options      |
    |Gift Cards           |
    |Product Support & Services|
    |Product Safety & Recalls  |
    |Policies & Guidelines     |
    |Compliance                |
    |Other Services            |
    |Nutrition Information     |
    |Technical Support         |

