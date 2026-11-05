# Week 1.6, Session 1: Task 5

from feed import QuakeFeed
from dataset import QuakeDataset

significance = input("Please enter a significance level. ")
period = input("Please enter a time period")
Q = QuakeFeed(significance, period)
D = QuakeDataset(Q)
D.read_feed()


# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like
