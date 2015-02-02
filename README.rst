Investment tools
================

Three fund portfolio rebalance Vanguard funds (Work in progress)
`````````````````````````````````````````````````

Simple script to rebalance across a three fund portfolio Boglehead style.

http://www.bogleheads.org/wiki/Three-fund_portfolio

Usage
^^^^^

Download statement as csv file from Vanguard and run the script with the
following parameters:

1) -f <filename>: The csv file to parse
2) -m <money>: Amount of money to add to the portfolio. Can be 0 if portfolio is
to be rebalanced without adding new funds.

Todo
^^^^
Fix to work with more than just Vanguard funds.
Dynamically populate asset classes from ticker symbols
