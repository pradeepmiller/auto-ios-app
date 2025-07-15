# auto-ios-app

# This is sample Android app project which has the below:
#   - 1)  Locator IDs for automation available in the .swift files that are having name appended with '+AccessibilityIdentifiers' for each of the features.
#   - 2) A Python script - 'swift_to_java_converter.py', which reads the above mentioned swift files and convert it into a java format.
#   - 3) A yaml / yml file - 'convert_automationids_swift_to_java.yml', which auto triggers the workflow whenever there is a change in the swift file mentioned in the point-1 above and generate a java file - 'AutomationIdLocatorsIos.java' in the 'Features' directory.
