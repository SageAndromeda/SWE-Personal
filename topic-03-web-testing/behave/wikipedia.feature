Feature: check inventors on invention pages

Scenario Outline:
    Given we have naviaged to the wikipedia main page
     When we enter "<invention>" and click on the search button
     Then the resulting page will include "<inventor>"

    Examples: Electronics
        | invention | inventor |
        | Telephone | Alexander Grahm Bell |
        | Transistor | Bardeen |
        | Light Bulb | Edison |
        | Phonograph | Edison |

    Examples: Transportation
        | invention | inventor |
        | airplane | Wright |
        | Helicoper | Sikorsky |