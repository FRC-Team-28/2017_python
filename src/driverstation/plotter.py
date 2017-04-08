import sys
from networktables import NetworkTables
import logging
import time

logging.basicConfig(level=logging.DEBUG)
NetworkTables.initialize(server="10.0.28.2")

sd = NetworkTables.getTable('SmartDashboard')


